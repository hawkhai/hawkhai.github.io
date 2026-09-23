"""Reconstruct the supplied Fourier illustration with NumPy and Matplotlib.

No image is read: surfaces, arrows, text and the pulse are drawn from scratch.
The camera and sampling parameters are fitted, not the author's original code.
Reference: https://cloud.tencent.com/developer/article/1187502

Run: python scripts/fourier_shell/reproduce_reference.py
"""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import PathPatch, Polygon
from matplotlib.textpath import TextPath
from matplotlib.ticker import FuncFormatter, MultipleLocator
from matplotlib.transforms import Affine2D
import numpy as np

from redraw_conch import (
    DEFAULT_AMPLITUDE, DEFAULT_AZIM, DEFAULT_DPI, DEFAULT_ELEV,
    DEFAULT_FMAX, DEFAULT_NF, DEFAULT_NT, DEFAULT_TMAX, DEFAULT_WIDTH,
    SHELL_BOX_ASPECT, clean_svg, conch_surface, finite_float, positive_float, sample_count,
)


BLUE = "#1004bf"
SOURCE = "https://cloud.tencent.com/developer/article/1187502"


def chinese_font():
    available = {font.name for font in font_manager.fontManager.ttflist}
    for name in ("Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "SimSun",
                 "Arial Unicode MS"):
        if name in available:
            weight = "normal" if name in ("SimHei", "SimSun") else "bold"
            return font_manager.FontProperties(family=name, weight=weight)
    raise RuntimeError("Please install a Chinese font: Noto Sans CJK SC / SimHei / Microsoft YaHei")


def fit_text(fig, text, box, font, color=BLUE):
    """Fit outlined glyphs into a figure-relative box, as in the tall source type."""
    path = TextPath((0, 0), text, prop=font, size=1)
    bounds = path.get_extents()
    x, y, width, height = box
    transform = (Affine2D().translate(-bounds.x0, -bounds.y0)
                 .scale(width / bounds.width, height / bounds.height)
                 .translate(x, y))
    fig.add_artist(PathPatch(path, transform=transform + fig.transFigure,
                            facecolor=color, edgecolor="none"))


def down_arrow(fig, y_top):
    # Figure coordinates keep the arrow proportions independent of render DPI.
    x = 0.285
    points = [(x-.011, y_top), (x+.011, y_top),
              (x+.011, y_top-.061), (x+.063, y_top-.055),
              (x, y_top-.081), (x-.063, y_top-.055),
              (x-.011, y_top-.061)]
    fig.add_artist(Polygon(points, closed=True, transform=fig.transFigure,
                           facecolor=BLUE, edgecolor="none"))


def style_3d(ax):
    ax.set_proj_type("ortho")
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor((1, 1, 1, 1))
        axis.pane.set_edgecolor("#eeeeee")
        axis.line.set_color("#bcbcbc")
        axis._axinfo["grid"].update(color="#e3e3e3", linewidth=0.4)
        axis._axinfo["tick"].update(inward_factor=0, outward_factor=0.1)
        axis.set_major_formatter(FuncFormatter(
            lambda value, _: "0" if abs(value) < 1e-10 else f"{value:g}"))
    ax.tick_params(colors="#999999", labelsize=3.1, pad=-2)


def components(width, tmax, fmax, amplitude, nt=DEFAULT_NT, nf=DEFAULT_NF):
    """C(f,t) = amplitude*sinc(T*f) * exp(2*pi*i*f*t).

    Rows are times, columns are frequencies. Keep signed sinc side lobes.
    Upper and middle panels use the SAME samples; only coordinates differ.
    """
    f, t = np.meshgrid(np.linspace(0, fmax, nf), np.linspace(0, tmax, nt))
    c = amplitude * np.sinc(width * f) * np.exp(2j * np.pi * f * t)
    return f, t, c


def reconstruct(times, width, cutoff):
    """Integrate both frequency halves using the even, real pulse spectrum.

    Display scale does not enter the transform: x_F = 2*integral X*cos df.
    """
    df = 1 / (100 * max(width, float(np.max(np.abs(times)))))
    f = np.linspace(0, cutoff, max(2, int(np.ceil(cutoff / df)) + 1))
    result = np.empty_like(times, dtype=float)
    for start in range(0, len(times), 128):
        t = times[start:start+128, None]
        waves = width * np.sinc(width * f) * np.cos(2 * np.pi * f * t)
        result[start:start+len(t)] = 2 * np.trapezoid(waves, f, axis=1)
    return result


def draw(args):
    font = chinese_font()
    plt.rcParams.update({"axes.unicode_minus": False, "svg.fonttype": "path",
                         "savefig.facecolor": "white", "font.family": font.get_name()})
    f, t, c = components(args.width, args.tmax, args.fmax,
                         args.amplitude, args.nt, args.nf)
    shell_x, shell_y, _ = conch_surface(
        args.width, args.amplitude, args.fmax, args.tmax, args.nf, args.nt)
    radius = args.amplitude
    fig = plt.figure(figsize=(6, 9.8), facecolor="white")

    shell = fig.add_axes([-.008, .711, .610, .266], projection="3d")
    # Use the same (-Re, Im, t) orientation and camera as redraw_conch.py.
    shell.plot_surface(shell_x, shell_y, t, rstride=1, cstride=1,
                       cmap="jet", vmin=0, vmax=args.tmax, shade=False,
                       edgecolor=(0, 0, 0, .50), linewidth=.25,
                       antialiased=True, rasterized=True, clip_on=False)
    shell.set(xlim=(-radius, radius), ylim=(-radius, radius),
              zlim=(0, args.tmax))
    shell.set_box_aspect(SHELL_BOX_ASPECT)
    shell.view_init(elev=args.elev, azim=args.azim)
    style_3d(shell)
    shell.xaxis.set_major_locator(MultipleLocator(radius / 5))
    shell.yaxis.set_major_locator(MultipleLocator(radius / 5))
    shell.zaxis.set_major_locator(MultipleLocator(args.tmax / 10))
    fit_text(fig, "复频域", (.724, .786, .123, .048), font, "#aaaaaa")

    down_arrow(fig, .696)
    fit_text(fig, "投影到实数空间", (.365, .647, .282, .045), font)

    waves = fig.add_axes([-.009, .393, .661, .218], projection="3d")
    waves.plot_surface(f, t, c.real, rstride=1, cstride=1,
                       cmap="jet", vmin=-radius, vmax=radius,
                       linewidth=0, antialiased=True, shade=False,
                       rasterized=True, clip_on=False)
    waves.set(xlim=(0, args.fmax), ylim=(0, args.tmax), zlim=(-radius, radius))
    waves.set_box_aspect((2.0, 1.6, .65), zoom=1.42)
    waves.view_init(elev=24, azim=-45)
    style_3d(waves)
    fit_text(fig, "频域", (.763, .463, .080, .047), font, "#aaaaaa")

    down_arrow(fig, .368)
    fit_text(fig, "各频率成分累积", (.389, .319, .282, .045), font)

    pulse = fig.add_axes([.103, .101, .375, .118])
    w = args.width
    if args.show_reconstruction:
        times = np.linspace(-3.5*w, 3.5*w, 2401)
        pulse.plot(times, reconstruct(times, w, args.cutoff), color="#ed9429", lw=.7)
    # The source shows the infinite-bandwidth limit, not a finite partial sum.
    pulse.plot(w*np.array([-.5, -.5, .5, .5]), [0, 1, 1, 0], color=BLUE, lw=1.7)
    pulse.plot([-3.5*w, 3.5*w], [0, 0], color="black", lw=2.3)
    pulse.plot([0, 0], [-.45, 1.45], color="black", lw=2.3)
    pulse.annotate("", xy=(0, 1.58), xytext=(0, 1.35),
                   arrowprops={"arrowstyle": "->", "color": "black", "lw": 1.2})
    pulse.set(xlim=(-3.5*w, 3.5*w), ylim=(-.45, 1.58))
    pulse.set_axis_off()
    fit_text(fig, "时域", (.763, .129, .080, .047), font, "#aaaaaa")

    # Credit the visual reference without representing this as the author's code.
    fig.text(.405, .061, "原图：Heinrich（韩昊）", color=BLUE, fontsize=11)
    fig.text(.405, .038, "公式重绘：NumPy + Matplotlib", color=BLUE, fontsize=9)
    fig.text(.405, .019, "参考布局复现 · 非原作者绘图代码", color="#777777", fontsize=7)

    args.output.mkdir(parents=True, exist_ok=True)
    for suffix in ("png", "svg"):
        path = args.output / f"fourier_reference.{suffix}"
        fig.savefig(path, dpi=args.dpi)
        if suffix == "svg":
            clean_svg(path)
        print(f"Saved: {path.resolve()}")
    plt.close(fig)

    probes = w * np.array([0, .25, .5, .75, 1.0])
    metrics = {
        "reference": SOURCE,
        "provenance": "Equation-based reconstruction; fitted camera and ranges.",
        "formula": "C(f,t) = amplitude*sinc(T*f)*exp(2*pi*i*f*t)",
        "shell_axes": ["-Re C", "Im C", "t"],
        "middle_axes": ["f", "t", "Re C"],
        "width": w, "amplitude": args.amplitude,
        "scale": args.amplitude / args.width,
        "tmax": args.tmax, "fmax": args.fmax,
        "nf": args.nf, "nt": args.nt,
        "elev": args.elev, "azim": args.azim,
        "cutoff": args.cutoff,
        "sample_shape": list(c.shape),
        "probe_times": probes.tolist(),
        "reconstructed_values": reconstruct(probes, w, args.cutoff).tolist(),
        "infinite_bandwidth_limits": [1, 1, .5, 0, 0],
    }
    (args.output / "reference_parameters.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "output" / "reference")
    parser.add_argument("--dpi", type=sample_count, default=DEFAULT_DPI)
    parser.add_argument("--width", type=positive_float, default=DEFAULT_WIDTH)
    parser.add_argument("--tmax", "--duration", type=positive_float, default=DEFAULT_TMAX)
    parser.add_argument("--fmax", type=positive_float, default=DEFAULT_FMAX)
    amplitude_group = parser.add_mutually_exclusive_group()
    amplitude_group.add_argument("--amplitude", type=positive_float, default=None,
                                 help="Maximum helix radius A(0)")
    amplitude_group.add_argument("--scale", type=positive_float, default=None,
                                 help="Legacy alias: amplitude = scale * width")
    parser.add_argument("--nf", type=sample_count, default=DEFAULT_NF)
    parser.add_argument("--nt", type=sample_count, default=DEFAULT_NT)
    parser.add_argument("--elev", type=finite_float, default=DEFAULT_ELEV)
    parser.add_argument("--azim", type=finite_float, default=DEFAULT_AZIM)
    parser.add_argument("--cutoff", type=positive_float, default=40.0)
    parser.add_argument("--show-reconstruction", action="store_true",
                        help="Overlay the finite-bandwidth integral in orange")
    args = parser.parse_args()
    if args.amplitude is None:
        args.amplitude = (args.scale * args.width if args.scale is not None
                          else DEFAULT_AMPLITUDE)
    if not np.isfinite(args.amplitude) or args.amplitude <= 0:
        parser.error("amplitude must be finite and positive")
    draw(args)


if __name__ == "__main__":
    main()

"""Draw the single Fourier shell in Heinrich's illustration from equations.

This is a reconstruction, not the author's original code or exact parameters.
Only NumPy and Matplotlib are needed; the input screenshot is never sampled.
Run: python scripts/fourier_shell/reproduce_single.py
"""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

from redraw_conch import (
    DEFAULT_AMPLITUDE, DEFAULT_AZIM, DEFAULT_DPI, DEFAULT_ELEV,
    DEFAULT_FMAX, DEFAULT_NF, DEFAULT_NT, DEFAULT_TMAX, DEFAULT_WIDTH,
    SHELL_BOX_ASPECT, clean_svg, conch_surface, finite_float, positive_float, sample_count,
)


def shell_coordinates(width=DEFAULT_WIDTH, amplitude=DEFAULT_AMPLITUDE,
                      tmax=DEFAULT_TMAX, fmax=DEFAULT_FMAX,
                      nt=DEFAULT_NT, nf=DEFAULT_NF):
    """Return (-Re C, Im C, time), identical to redraw_conch.

    Here sinc(u) = sin(pi*u)/(pi*u); NumPy handles u=0 analytically.
    Keep the SIGN of sinc: negative lobes represent a phase shift of pi.
    Rows are times, columns are nonnegative frequencies (including DC).
    """
    return conch_surface(width, amplitude, fmax, tmax, nf, nt)


def draw_shell(ax, x, y, time, *, amplitude=DEFAULT_AMPLITUDE,
               elev=DEFAULT_ELEV, azim=DEFAULT_AZIM,
               labels=False):
    """Join adjacent frequencies/times into a colored quadrilateral mesh."""
    ax.plot_surface(x, y, time, rstride=1, cstride=1,
                    cmap="jet", vmin=0, vmax=float(time.max()),
                    edgecolor=(0, 0, 0, 0.50), linewidth=0.25,
                    antialiased=True, shade=False, rasterized=True)
    ax.set(xlim=(-amplitude, amplitude), ylim=(-amplitude, amplitude),
           zlim=(0, float(time.max())))
    ax.set_box_aspect(SHELL_BOX_ASPECT)
    ax.set_proj_type("ortho")
    ax.view_init(elev=elev, azim=azim)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.fill = False
        axis.pane.set_edgecolor("#eeeeee")
        axis.line.set_color("#aaaaaa")
        axis._axinfo["grid"].update(color="#dddddd", linewidth=0.6)
        axis.set_major_formatter(FuncFormatter(
            lambda value, _: "0" if abs(value) < 1e-12 else f"{value:.3g}"))
    ax.set_xticks(np.linspace(-amplitude, amplitude, 11))
    ax.set_yticks(np.linspace(-amplitude, amplitude, 11))
    ax.set_zticks(np.linspace(0, float(time.max()), 11))
    ax.tick_params(labelsize=7, colors="#888888", pad=0)
    if labels:
        ax.set(xlabel=r"$-\mathrm{Re}\,C(f,t)$", ylabel=r"$\mathrm{Im}\,C(f,t)$", zlabel=r"$t$")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).parent / "output" / "single")
    parser.add_argument("--width", type=positive_float, default=DEFAULT_WIDTH,
                        help="Rectangular pulse width T (seconds)")
    amplitude_group = parser.add_mutually_exclusive_group()
    amplitude_group.add_argument("--amplitude", type=positive_float, default=None,
                                 help="Maximum helix radius A(0), like redraw_conch.py")
    amplitude_group.add_argument("--scale", type=positive_float, default=None,
                                 help="Legacy alias: amplitude = scale * width")
    parser.add_argument("--tmax", "--duration", type=positive_float,
                        default=DEFAULT_TMAX, help="Height/time extent")
    parser.add_argument("--fmax", type=positive_float, default=DEFAULT_FMAX,
                        help="Highest displayed frequency (Hz)")
    parser.add_argument("--nf", type=sample_count, default=DEFAULT_NF)
    parser.add_argument("--nt", type=sample_count, default=DEFAULT_NT)
    parser.add_argument("--elev", type=finite_float, default=DEFAULT_ELEV)
    parser.add_argument("--azim", type=finite_float, default=DEFAULT_AZIM)
    parser.add_argument("--dpi", type=sample_count, default=DEFAULT_DPI)
    parser.add_argument("--labels", action="store_true", help="Add axis names")
    args = parser.parse_args()
    if args.amplitude is None:
        args.amplitude = (args.scale * args.width if args.scale is not None
                          else DEFAULT_AMPLITUDE)
    if not np.isfinite(args.amplitude) or args.amplitude <= 0:
        parser.error("amplitude must be finite and positive")
    x, y, time = shell_coordinates(args.width, args.amplitude, args.tmax,
                                   args.fmax, args.nt, args.nf)
    plt.rcParams.update({"font.family": "DejaVu Sans", "axes.unicode_minus": True,
                         "savefig.facecolor": "white", "svg.fonttype": "path"})
    fig = plt.figure(figsize=(8, 5.65), facecolor="white")
    ax = fig.add_axes([-.10, -.13, 1.20, 1.30], projection="3d")
    draw_shell(ax, x, y, time, amplitude=args.amplitude,
               elev=args.elev, azim=args.azim, labels=args.labels)
    args.output.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output / "fourier_shell_single.png", dpi=args.dpi)
    fig.savefig(args.output / "fourier_shell_single.svg", dpi=args.dpi)
    clean_svg(args.output / "fourier_shell_single.svg")
    plt.close(fig)
    parameters = vars(args).copy()
    parameters["output"] = str(args.output.resolve())
    parameters.update(scale=args.amplitude / args.width,
                      coordinates=["-Re(C)", "Im(C)", "t"],
                      formula="C(f,t) = amplitude * sinc(width*f) * exp(2*pi*i*f*t)",
                      sinc="sinc(u) = sin(pi*u)/(pi*u), sinc(0) = 1",
                      provenance="Reconstructed parameters; not the original source code.")
    (args.output / "parameters.json").write_text(
        json.dumps(parameters, indent=2), encoding="utf-8")
    print(f"Saved: {(args.output / 'fourier_shell_single.png').resolve()}")


if __name__ == "__main__":
    main()

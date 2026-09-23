"""Reproduce the Fourier 'shell -> waves -> rectangular pulse' illustration.

This is a mathematical reconstruction, not the unavailable original source.
Fourier convention: X(f) = integral x(t) exp(-2*pi*i*f*t) dt.
For a unit-height pulse of width T: X(f) = T * sinc(T*f).

Run: python scripts/fourier_shell/reproduce.py
Only NumPy and Matplotlib are required; no input image is used by the renderer.
"""

from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch

from redraw_conch import (
    DEFAULT_AMPLITUDE, DEFAULT_AZIM, DEFAULT_DPI, DEFAULT_ELEV,
    DEFAULT_FMAX, DEFAULT_NF, DEFAULT_NT, DEFAULT_TMAX, DEFAULT_WIDTH,
    SHELL_BOX_ASPECT, clean_svg, conch_surface, finite_float, positive_float, sample_count,
)


BLUE = "#1616e8"


def configure_fonts():
    for name in ("Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"):
        if name in {font.name for font in font_manager.fontManager.ttflist}:
            plt.rcParams["font.sans-serif"] = [name, "DejaVu Sans"]
            break
    plt.rcParams.update({"axes.unicode_minus": False, "font.size": 10,
                         "savefig.facecolor": "white", "svg.fonttype": "path"})


def spectrum(frequency, width=1.0):
    """np.sinc(u) = sin(pi*u)/(pi*u), including its limit at zero."""
    return width * np.sinc(width * frequency)


def inverse_integral(times, cutoff, width=1.0):
    """Trapezoid quadrature of BOTH frequency halves using even symmetry.

    x_F(t) = 2 * integral_0^F X(f) cos(2*pi*f*t) df.
    Blocking limits memory use; frequency sampling resolves the fastest phase.
    """
    df = min(0.0025, 1 / (80 * max(float(np.max(np.abs(times))), width)))
    f = np.linspace(0, cutoff, max(2, int(np.ceil(cutoff / df)) + 1))
    result = np.empty_like(times, dtype=float)
    for start in range(0, len(times), 128):
        t = times[start:start + 128]
        waves = spectrum(f, width)[None, :] * np.cos(2 * np.pi * t[:, None] * f)
        result[start:start + len(t)] = 2 * np.trapezoid(waves, f, axis=1)
    return result


def style_3d(ax):
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.fill = False
        axis.pane.set_edgecolor("#e5e5e5")
        axis._axinfo["grid"].update(color="#dddddd", linewidth=0.5)
        axis.line.set_color("#b7b7b7")
    ax.tick_params(colors="#777777", labelsize=6, pad=0)
    ax.set_proj_type("ortho")


def arrow(fig, y, label, formula):
    fig.add_artist(FancyArrowPatch(
        (0.27, y + 0.035), (0.27, y - 0.027), transform=fig.transFigure,
        arrowstyle="Simple,head_length=19,head_width=29,tail_width=7",
        color=BLUE, linewidth=0))
    fig.text(0.36, y + 0.005, label, fontsize=21, weight="bold", color=BLUE)
    fig.text(0.36, y - 0.022, formula, fontsize=11, color="#525274")


def draw_reproduction(output, width, amplitude, fmax, tmax, nf, nt,
                      elev, azim, cutoff, dpi):
    # Both upper panels use exactly the same complex-valued data. The shell
    # discards an explicit frequency axis; color encodes time, not amplitude.
    times = np.linspace(0, tmax, nt)
    f = np.linspace(0, fmax, nf)
    ff, tt = np.meshgrid(f, times)
    shell_x, shell_y, _ = conch_surface(width, amplitude, fmax, tmax, nf, nt)
    component_real = -shell_x

    fig = plt.figure(figsize=(8, 13), facecolor="white")
    fig.text(0.085, 0.967, "从复指数曲面到矩形脉冲", fontsize=22, weight="bold")
    fig.text(0.085, 0.939, "傅里叶逆变换 · 依据参考图重建的数学示意", fontsize=10, color="#777777")

    shell = fig.add_axes([0.025, 0.686, 0.73, 0.257], projection="3d")
    shell.plot_surface(shell_x, shell_y, tt, rstride=1, cstride=1,
                       cmap="jet", vmin=0, vmax=tmax,
                       shade=False, linewidth=0.25, edgecolor=(0, 0, 0, 0.50),
                       antialiased=True, rasterized=True)
    shell.set(xlabel=r"-Re $C(f,t)$", ylabel=r"Im $C(f,t)$", zlabel=r"$t$",
              xlim=(-amplitude, amplitude), ylim=(-amplitude, amplitude), zlim=(0, tmax))
    shell.set_box_aspect(SHELL_BOX_ASPECT)
    shell.view_init(elev=elev, azim=azim)
    style_3d(shell)
    fig.text(0.79, 0.792, "复数域", fontsize=21, color="#999999")
    fig.text(0.12, 0.665, r"$C(f,t)=a\,\mathrm{sinc}(Tf)e^{i2\pi ft},\quad X(f)=T\,\mathrm{sinc}(Tf)$", fontsize=11)
    arrow(fig, 0.614, "取实部", r"$\mathrm{Re}\, C(f,t)=a\,\mathrm{sinc}(Tf)\cos(2\pi ft)$")

    waves = fig.add_axes([0.015, 0.354, 0.75, 0.236], projection="3d")
    waves.plot_surface(ff, tt, component_real, rstride=1, cstride=1, cmap="jet",
                       vmin=-amplitude, vmax=amplitude, linewidth=0,
                       antialiased=True, rasterized=True)
    waves.set(xlabel=r"$f$", ylabel=r"$t$", zlabel=r"Re $C$",
              xlim=(0, fmax), ylim=(0, tmax), zlim=(-amplitude, amplitude))
    waves.set_box_aspect((2.0, 1.2, 0.65))
    waves.view_init(elev=24, azim=-59)
    style_3d(waves)
    fig.text(0.79, 0.466, "频率分量", fontsize=18, color="#999999")
    fig.text(0.12, 0.355, "横轴展开频率；曲面振幅已缩放，积分按原频谱归一化", fontsize=10, color="#666666")
    arrow(fig, 0.300, "沿频率积分叠加", r"$x(t)=2\int_0^\infty X(f)\cos(2\pi ft)\,df$")

    ax = fig.add_axes([0.10, 0.080, 0.64, 0.155])
    t = np.linspace(-3 * width, 3 * width, 2401)
    reconstructed = inverse_integral(t, cutoff, width)
    ax.plot(t, reconstructed, color="#eb8b23", lw=1.3,
            label=f"数值积分：0 ≤ f ≤ {cutoff:g}")
    ax.plot(width * np.array([-3, -.5, -.5, .5, .5, 3]),
            [0, 0, 1, 1, 0, 0], color=BLUE, lw=1.8, label="理想矩形脉冲")
    ax.set(xlim=(-3 * width, 3 * width), ylim=(-.25, 1.5),
           xticks=[-width/2, 0, width/2], yticks=[1])
    ax.set_xticklabels([r"$-T/2$", "0", r"$T/2$"])
    ax.spines[["right", "top"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_position("zero")
    ax.spines[["left", "bottom"]].set_linewidth(1.1)
    ax.plot(3 * width, 0, ">k", ms=5, clip_on=False)
    ax.plot(0, 1.5, "^k", ms=5, clip_on=False)
    ax.text(2.9 * width, .1, "$t$")
    ax.legend(loc="upper right", fontsize=8, frameon=False)
    fig.text(0.79, 0.142, "时域", fontsize=21, color="#999999")
    fig.text(0.10, 0.032, "有限带宽产生边缘振铃；无限带宽极限在跳变点取左右极限的平均值。",
             fontsize=9, color="#777777")
    fig.savefig(output / "fourier_shell.png", dpi=dpi)
    fig.savefig(output / "fourier_shell.svg", dpi=dpi)
    clean_svg(output / "fourier_shell.svg")
    plt.close(fig)


def draw_validation(output, width, fmax, cutoff, dpi):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.2), layout="constrained")
    f = np.linspace(-fmax, fmax, 1601)
    axes[0].plot(f, spectrum(f, width), color=BLUE, lw=1.7)
    axes[0].set(title="矩形脉冲的频谱（有正负号）", xlabel="频率 f", ylabel="X(f)")
    t = np.linspace(-1.5 * width, 1.5 * width, 1601)
    ideal = (np.abs(t) < width / 2).astype(float)
    axes[1].plot(t, ideal, "--", color="#333333", lw=1.2, label="理想矩形")
    for frequency_cutoff in sorted({min(fmax / 4, cutoff), min(fmax, cutoff), cutoff}):
        axes[1].plot(t, inverse_integral(t, frequency_cutoff, width), lw=1.1,
                     label=f"截止频率 {frequency_cutoff:g}")
    axes[1].set(title="增加频率分量，积分逼近矩形脉冲", xlabel="时间 t", ylabel="x(t)")
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.grid(alpha=.2)
        ax.axhline(0, color="#aaaaaa", lw=.6)
        ax.spines[["right", "top"]].set_visible(False)
    fig.savefig(output / "fourier_validation.png", dpi=dpi)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "output")
    parser.add_argument("--width", type=positive_float, default=DEFAULT_WIDTH, help="Pulse width T")
    parser.add_argument("--amplitude", type=positive_float, default=DEFAULT_AMPLITUDE,
                        help="Maximum displayed helix radius A(0)")
    parser.add_argument("--fmax", type=positive_float, default=DEFAULT_FMAX)
    parser.add_argument("--tmax", type=positive_float, default=DEFAULT_TMAX)
    parser.add_argument("--nf", type=sample_count, default=DEFAULT_NF)
    parser.add_argument("--nt", type=sample_count, default=DEFAULT_NT)
    parser.add_argument("--elev", type=finite_float, default=DEFAULT_ELEV)
    parser.add_argument("--azim", type=finite_float, default=DEFAULT_AZIM)
    parser.add_argument("--cutoff", type=positive_float, default=40.0,
                        help="Integration cutoff in Hz")
    parser.add_argument("--dpi", type=sample_count, default=DEFAULT_DPI)
    args = parser.parse_args()
    configure_fonts()
    args.output.mkdir(parents=True, exist_ok=True)
    draw_reproduction(args.output, args.width, args.amplitude, args.fmax,
                      args.tmax, args.nf, args.nt, args.elev, args.azim,
                      args.cutoff, args.dpi)
    draw_validation(args.output, args.width, args.fmax, args.cutoff, args.dpi)
    probes = args.width * np.array([0, .25, .5, .75, 1.0])
    metrics = {"width": args.width, "amplitude": args.amplitude,
               "fmax": args.fmax, "tmax": args.tmax,
               "nf": args.nf, "nt": args.nt,
               "elev": args.elev, "azim": args.azim,
               "cutoff": args.cutoff,
               "probe_times": probes.tolist(),
               "reconstructed_values": inverse_integral(probes, args.cutoff, args.width).tolist(),
               "infinite_bandwidth_limits": [1, 1, .5, 0, 0]}
    (args.output / "numerical_check.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))
    print(f"Images saved to: {args.output.resolve()}")


if __name__ == "__main__":
    main()

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
from matplotlib.ticker import FuncFormatter, MultipleLocator
import numpy as np


def shell_coordinates(width=2.0, scale=0.025, duration=5.0, fmax=6.0,
                      nt=361, nf=601):
    """Return Im(C), Re(C), time, for C = scale*T*sinc(T*f)*exp(2j*pi*f*t).

    Here sinc(u) = sin(pi*u)/(pi*u); NumPy handles u=0 analytically.
    Keep the SIGN of sinc: negative lobes represent a phase shift of pi.
    Rows are times, columns are nonnegative frequencies (including DC).
    """
    frequency, time = np.meshgrid(np.linspace(0, fmax, nf),
                                  np.linspace(0, duration, nt))
    amplitude = scale * width * np.sinc(width * frequency)
    component = amplitude * np.exp(2j * np.pi * frequency * time)
    # The reference orientation is reproduced by putting Im on the first axis.
    return component.imag, component.real, time


def draw_shell(ax, x, y, time, *, width=2.0, scale=0.025, elev=7, azim=135,
               labels=False):
    """Join adjacent frequencies/times into a colored quadrilateral mesh."""
    ax.plot_surface(x, y, time, rstride=max(1, (time.shape[0] - 1) // 120),
                    cstride=1,
                    cmap="jet", vmin=0, vmax=float(time.max()),
                    edgecolor=(0, 0, 0, 0.38), linewidth=0.22,
                    antialiased=True, shade=False, rasterized=True)
    radius = scale * width
    limit = 1.05 * radius
    ax.set(xlim=(-limit, limit), ylim=(-limit, limit),
           zlim=(0, float(time.max())))
    # Display aspect is intentionally independent of the data units.
    ax.set_box_aspect((1.33, 1.33, 1.1), zoom=1.30)
    ax.set_proj_type("ortho")
    ax.view_init(elev=elev, azim=azim)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor((1, 1, 1, 1))
        axis.pane.set_edgecolor("#dddddd")
        axis.line.set_color("#aaaaaa")
        axis._axinfo["grid"].update(color="#dddddd", linewidth=0.55)
        axis._axinfo["tick"].update(inward_factor=0, outward_factor=0.12)
        axis.set_major_formatter(FuncFormatter(
            lambda value, _: "0" if abs(value) < 1e-12 else f"{value:g}"))
    ax.xaxis.set_major_locator(MultipleLocator(radius / 5))
    ax.yaxis.set_major_locator(MultipleLocator(radius / 5))
    ax.zaxis.set_major_locator(MultipleLocator(float(time.max()) / 10))
    ax.zaxis.set_ticks_position("upper")
    ax.zaxis.set_label_position("upper")
    ax.tick_params(labelsize=7, colors="#777777", pad=0)
    if labels:
        ax.set(xlabel=r"Im $C(f,t)$", ylabel=r"Re $C(f,t)$", zlabel=r"Time $t$")


def positive_float(value):
    result = float(value)
    if not np.isfinite(result) or result <= 0:
        raise argparse.ArgumentTypeError("must be finite and positive")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).parent / "output" / "single")
    parser.add_argument("--width", type=positive_float, default=2.0,
                        help="Rectangular pulse width T (seconds)")
    parser.add_argument("--scale", type=positive_float, default=0.025,
                        help="Display scale of the complex plane")
    parser.add_argument("--duration", type=positive_float, default=5.0)
    parser.add_argument("--fmax", type=positive_float, default=6.0,
                        help="Highest displayed frequency (Hz)")
    parser.add_argument("--elev", type=float, default=7)
    parser.add_argument("--azim", type=float, default=135)
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--labels", action="store_true", help="Add axis names")
    args = parser.parse_args()
    if args.dpi <= 0 or not np.isfinite([args.elev, args.azim]).all():
        parser.error("dpi must be positive and camera angles must be finite")
    # Resolve even the fastest rotation with at least 12 samples per cycle.
    nt = max(151, int(np.ceil(12 * args.fmax * args.duration)) + 1)
    nf = max(601, int(np.ceil(20 * args.fmax * max(args.duration, args.width))) + 1)
    x, y, time = shell_coordinates(args.width, args.scale, args.duration,
                                   args.fmax, nt, nf)
    plt.rcParams.update({"font.family": "DejaVu Sans", "axes.unicode_minus": True,
                         "savefig.facecolor": "white", "svg.fonttype": "path"})
    fig = plt.figure(figsize=(8, 6.2), facecolor="white")
    ax = fig.add_axes([-0.01, 0.025, 0.97, 0.96], projection="3d")
    draw_shell(ax, x, y, time, width=args.width, scale=args.scale,
               elev=args.elev, azim=args.azim, labels=args.labels)
    args.output.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output / "fourier_shell_single.png", dpi=args.dpi)
    fig.savefig(args.output / "fourier_shell_single.svg", dpi=args.dpi)
    plt.close(fig)
    parameters = vars(args).copy()
    parameters["output"] = str(args.output.resolve())
    parameters.update(nt=nt, nf=nf,
                      coordinates=["Im(C)", "Re(C)", "t"],
                      formula="C(f,t) = scale * width * sinc(width*f) * exp(2*pi*i*f*t)",
                      sinc="sinc(u) = sin(pi*u)/(pi*u), sinc(0) = 1",
                      provenance="Reconstructed parameters; not the original source code.")
    (args.output / "parameters.json").write_text(
        json.dumps(parameters, indent=2), encoding="utf-8")
    print(f"Saved: {(args.output / 'fourier_shell_single.png').resolve()}")


if __name__ == "__main__":
    main()

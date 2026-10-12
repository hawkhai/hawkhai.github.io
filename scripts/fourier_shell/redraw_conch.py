"""Redraw the Fourier conch surface using NumPy and Matplotlib.

Reference: https://blog.csdn.net/Ciellee/article/details/108304531
The article supplies an illustration, not source code or sampling parameters.
Defaults below are a visual reconstruction; no reference image is loaded.

Run: python scripts/fourier_shell/redraw_conch.py
"""

import argparse
from pathlib import Path

import matplotlib
import numpy as np

# Canonical conch settings. The companion renderers import these defaults so
# the same frequency/time grid and camera are used throughout the examples.
DEFAULT_WIDTH = 2.0
DEFAULT_AMPLITUDE = 0.05
DEFAULT_FMAX = 8.0
DEFAULT_TMAX = 5.0
DEFAULT_NF = 1201
DEFAULT_NT = 101
DEFAULT_ELEV = 8.0
DEFAULT_AZIM = -135.0
DEFAULT_DPI = 200
SHELL_BOX_ASPECT = (1, 1, .78)

def clean_svg(path):
    """Remove Matplotlib's SVG path-line trailing spaces for clean diffs."""
    svg = path.read_text(encoding="utf-8")
    path.write_text("\n".join(line.rstrip() for line in svg.splitlines()) + "\n",
                    encoding="utf-8")

def positive_float(value):
    number = float(value)
    if not np.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be finite and positive")
    return number

def sample_count(value):
    number = int(value)
    if number < 2:
        raise argparse.ArgumentTypeError("must be at least 2")
    return number

def finite_float(value):
    number = float(value)
    if not np.isfinite(number):
        raise argparse.ArgumentTypeError("must be finite")
    return number

def conch_surface(width, amplitude, fmax, tmax, nf, nt):
    """Return (-Re C, Im C, t), with positive frequency as the other parameter.

    A(f) = amplitude * sinc(width * f)
    C(f,t) = A(f) * exp(2*pi*i*f*t)

    np.sinc(u) = sin(pi*u)/(pi*u), including sinc(0) = 1.
    A is the spectrum of a centered rectangular pulse of width `width`
    and height `amplitude / width`. Its negative lobes MUST keep their sign.
    The minus sign on the displayed real coordinate matches the reference's
    orientation; it does not change the positive-frequency convention.
    """
    frequency = np.linspace(0, fmax, nf)
    time = np.linspace(0, tmax, nt)
    ff, tt = np.meshgrid(frequency, time)
    radius = amplitude * np.sinc(width * ff)
    phase = 2 * np.pi * ff * tt
    return -radius * np.cos(phase), radius * np.sin(phase), tt

def draw(args):
    # Select the backend before importing pyplot; --show enables a GUI window.
    if not args.show:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter

    x, y, z = conch_surface(args.width, args.amplitude, args.fmax,
                            args.tmax, args.nf, args.nt)
    fig = plt.figure(figsize=(8, 5.65), facecolor="white")
    ax = fig.add_axes([-.10, -.13, 1.20, 1.30], projection="3d")

    # Explicit strides avoid plot_surface's default downsampling to 50 x 50.
    # Colors follow height/time, as in the screenshot, rather than radius.
    ax.plot_surface(
        x, y, z, rstride=1, cstride=1,
        cmap="jet", vmin=0, vmax=args.tmax, shade=False,
        edgecolor=(0, 0, 0, .50), linewidth=.25, antialiased=True,
        rasterized=True,
    )
    ax.set(xlim=(-args.amplitude, args.amplitude),
           ylim=(-args.amplitude, args.amplitude), zlim=(0, args.tmax))
    ax.set_box_aspect(SHELL_BOX_ASPECT)
    ax.set_proj_type("ortho")
    ax.view_init(elev=args.elev, azim=args.azim)

    # Explicit positions also avoid tiny floating-point values at the zero tick.
    ax.set_xticks(np.linspace(-args.amplitude, args.amplitude, 11))
    ax.set_yticks(np.linspace(-args.amplitude, args.amplitude, 11))
    ax.set_zticks(np.linspace(0, args.tmax, 11))
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.fill = False
        axis.pane.set_edgecolor("#eeeeee")
        axis.line.set_color("#aaaaaa")
        axis._axinfo["grid"].update(color="#dddddd", linewidth=.6)
        axis.set_major_formatter(FuncFormatter(
            lambda value, position: "0" if value == 0 else f"{value:.3g}"))
    ax.tick_params(colors="#888888", labelsize=7, pad=0)
    if args.labels:
        ax.set(xlabel=r"$-\mathrm{Re}\,C(f,t)$",
               ylabel=r"$\mathrm{Im}\,C(f,t)$", zlabel=r"$t$")

    # The SVG keeps axes/text as vectors and embeds the dense surface as a
    # raster layer, avoiding hundreds of thousands of SVG polygon elements.
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=args.dpi, facecolor="white")
    fig.savefig(output.with_suffix(".svg"), dpi=args.dpi, facecolor="white")
    clean_svg(output.with_suffix(".svg"))
    print(f"PNG: {output}")
    print(f"SVG: {output.with_suffix('.svg')}")
    print(f"Surface: {args.nt} time samples x {args.nf} frequency samples")
    if args.show:
        plt.show()
    plt.close(fig)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).parent / "output" / "conch.png",
                        help="PNG path; an SVG with the same stem is also saved")
    parser.add_argument("--width", type=positive_float, default=DEFAULT_WIDTH,
                        help="Rectangle width; controls how tightly the shell curls")
    parser.add_argument("--amplitude", type=positive_float, default=DEFAULT_AMPLITUDE,
                        help="Maximum helix radius A(0)")
    parser.add_argument("--fmax", type=positive_float, default=DEFAULT_FMAX,
                        help="Largest displayed positive frequency in Hz")
    parser.add_argument("--tmax", type=positive_float, default=DEFAULT_TMAX,
                        help="Height/time extent")
    parser.add_argument("--nf", type=sample_count, default=DEFAULT_NF,
                        help="Frequency samples (mesh columns)")
    parser.add_argument("--nt", type=sample_count, default=DEFAULT_NT,
                        help="Time samples (mesh rows)")
    parser.add_argument("--elev", type=finite_float, default=DEFAULT_ELEV,
                        help="Camera elevation in degrees")
    parser.add_argument("--azim", type=finite_float, default=DEFAULT_AZIM,
                        help="Camera azimuth in degrees")
    parser.add_argument("--dpi", type=sample_count, default=DEFAULT_DPI)
    parser.add_argument("--labels", action="store_true", help="Label the three axes")
    parser.add_argument("--show", action="store_true",
                        help="Open an interactive Matplotlib window after saving")
    args = parser.parse_args()
    if args.output.suffix.lower() != ".png":
        parser.error("--output must end in .png")
    draw(args)

if __name__ == "__main__":
    main()

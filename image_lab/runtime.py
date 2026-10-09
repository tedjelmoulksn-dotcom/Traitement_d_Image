"""Resolve shared inputs and save figures without requiring a desktop GUI."""
import argparse
from pathlib import Path
import sys
import matplotlib
import numpy as np

if "--show" not in sys.argv:
    matplotlib.use("Agg")

ROOT = Path(__file__).resolve().parents[1]
_figure_index = 0

def data_path(name):
    path = ROOT / "data" / "input" / name
    if not path.is_file():
        raise FileNotFoundError(f"Missing input image: {path}")
    return path

def michelson(image):
    minimum, maximum = float(np.min(image)), float(np.max(image))
    denominator = minimum + maximum
    return (maximum - minimum) / denominator if denominator else 0.0

def finish(script):
    """Save all current figures, optionally display, then release them."""
    global _figure_index
    import matplotlib.pyplot as plt
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "outputs")
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()
    script = Path(script)
    folder = args.output_dir / script.parent.parent.name / script.stem
    folder.mkdir(parents=True, exist_ok=True)
    for number in plt.get_fignums():
        _figure_index += 1
        path = folder / f"figure_{_figure_index:02d}.png"
        plt.figure(number).savefig(path, dpi=120, bbox_inches="tight")
        print(f"Saved {path}")
    if args.show:
        plt.show()
    plt.close("all")

"""Plot real Week 1 episode returns and survival steps from CSV."""
import argparse
import csv
from pathlib import Path

def load_records(csv_path):
    if not csv_path.exists():
        raise FileNotFoundError(f"Run the random-agent script first: {csv_path}")
    with csv_path.open(newline="", encoding="utf-8") as handle:
        records = list(csv.DictReader(handle))
    if not records:
        raise ValueError("CSV is empty")
    return ([int(r["episode"]) for r in records],
            [float(r["total_reward"]) for r in records],
            [int(r["steps"]) for r in records])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=Path("results/week01/random_baseline.csv"))
    parser.add_argument("--out", type=Path, default=Path("results/week01/random_baseline.png"))
    args = parser.parse_args()
    x, returns, steps = load_records(args.csv)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(x, returns, marker="o")
    axes[0].set_title("Random-policy baseline — not a trained agent")
    axes[0].set_ylabel("Episode return")
    axes[1].plot(x, steps, marker="o")
    axes[1].set_ylabel("Survival steps")
    axes[1].set_xlabel("Episode")
    fig.tight_layout()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.out, dpi=150)
    plt.close(fig)
    print("Graph saved:", args.out)

if __name__ == "__main__":
    main()

"""Reproducible analysis for Hong Kong fertility trends, 1991–2021."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "hk_fertility_1991_2021.csv"
OUTPUT = ROOT / "outputs"


def main() -> None:
    df = pd.read_csv(DATA)
    OUTPUT.mkdir(exist_ok=True)

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax1 = plt.subplots(figsize=(10, 5.8))
    ax1.plot(df["year"], df["tfr"], color="#1f77b4", linewidth=2.5, label="Total fertility rate")
    ax1.axhline(2100, color="#d62728", linestyle="--", linewidth=1.5, label="Replacement level (2,100)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Live births per 1,000 women")
    ax1.set_title("Hong Kong total fertility rate, 1991–2021")
    ax1.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(OUTPUT / "tfr_trend.png", dpi=180)
    plt.close(fig)

    fig, ax1 = plt.subplots(figsize=(10, 5.8))
    ax1.plot(df["year"], df["live_births"], color="#2ca02c", linewidth=2.5, label="Live births")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Number of live births")
    ax1.set_title("Hong Kong live births and crude birth rate, 1991–2021")
    ax2 = ax1.twinx()
    ax2.plot(df["year"], df["crude_birth_rate"], color="#ff7f0e", linewidth=2, label="Crude birth rate")
    ax2.set_ylabel("Crude birth rate per 1,000 population")
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc="upper right")
    fig.tight_layout()
    fig.savefig(OUTPUT / "births_and_crude_rate.png", dpi=180)
    plt.close(fig)

    first = df.iloc[0]
    last = df.iloc[-1]
    print(f"TFR change: {first.tfr:.0f} -> {last.tfr:.0f} per 1,000 women")
    print(f"Live births change: {first.live_births:,.0f} -> {last.live_births:,.0f}")
    print(f"Lowest TFR year: {int(df.loc[df.tfr.idxmin(), 'year'])}")


if __name__ == "__main__":
    main()

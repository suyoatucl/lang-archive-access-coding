"""Draw the three figures from the tables in analysis/.

Usage:
    python3 scripts/build_tables.py
    python3 scripts/figures.py

Outputs, each as PNG (300 dpi), SVG and PDF in analysis/:
    figure1_states      items by archives: answered, deferred, not stated
    figure2_authority   who decides: parties by acts, one panel for each archive
    figure3_provenance  items by archives: the kind of document behind each answer

The figures are static and made for print. The tables in analysis/ hold the same
data in text form. Colours come from a validated palette: one hue in two steps for
the ordered states of figure 1, one hue for figure 2, and three hues that stay
distinct for colour-blind readers for figure 3. Every tile that is not a plain
answer carries a text label, so no figure depends on colour alone.

Requires matplotlib.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "analysis"
ARCHIVES = ["AILLA", "ELAR", "PARADISEC"]

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
NEUTRAL = "#f0efec"
BLUE_DARK = "#1c5cab"   # answered
BLUE_LIGHT = "#86b6ef"  # deferred
BLUE = "#2a78d6"        # one-hue marks in figure 2
GENRE = {"deposit document": "#2a78d6", "terms or policy": "#eb6834", "help or information page": "#1baf7a"}
GENRE_SHORT = {"deposit document": "deposit", "terms or policy": "terms", "help or information page": "help"}

LABEL = {
    "DM1": "Who can set a restriction",
    "DM2": "Who can change it",
    "DM3": "Who can lift it",
    "DM4": "Who decides on access requests",
    "GR1": "Form in which reasons are given",
    "GR2": "Reasons named",
    "LV1": "Number of access levels",
    "LV2": "Names of access levels",
    "RV1": "Expiry",
    "RV2": "Review period",
    "RV3": "Appeal",
    "RV4": "Takedown or withdrawal",
    "RV5": "Succession",
}
ACT = {"DM1": "set", "DM2": "change", "DM3": "lift", "DM4": "decide on\nrequests"}
PARTIES = ["depositor", "speaker or community", "archive", "steward or controller"]

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 8,
    "figure.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "svg.fonttype": "none",
    "svg.hashsalt": "delaman-access-coding",
})


def read(name):
    with open(OUT / name, encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def save(fig, stem):
    # No creation dates in the files, so that the same data give the same files.
    metadata = {"png": {}, "svg": {"Date": None}, "pdf": {"CreationDate": None}}
    for ext in ("png", "svg", "pdf"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=300, bbox_inches="tight", pad_inches=0.08,
                    metadata=metadata[ext])
    plt.close(fig)


def grid_axes(rows, height):
    """Axes for an items-by-archives grid, with field and item labels on the left."""
    fig, ax = plt.subplots(figsize=(6.3, height))
    ax.set_xlim(-4.15, 3.0)
    ax.set_ylim(len(rows) + 0.15, -0.95)
    ax.axis("off")
    for column, archive in enumerate(ARCHIVES):
        ax.text(column + 0.5, -0.3, archive, ha="center", va="center", color=INK, fontsize=8, fontweight="bold")
    previous = None
    for index, row in enumerate(rows):
        if row["field"] != previous:
            if previous is not None:
                ax.plot([-4.15, 3.0], [index, index], color=GRID, linewidth=0.8, solid_capstyle="butt")
            ax.text(-4.15, index + 0.5, row["field"], ha="left", va="center", color=INK, fontsize=8, fontweight="bold")
            previous = row["field"]
        ax.text(-0.12, index + 0.5, LABEL[row["item"]], ha="right", va="center", color=INK2, fontsize=8)
    return fig, ax


def tile(ax, column, index, colour):
    gap = 0.035
    ax.add_patch(Rectangle((column + gap, index + gap * 2.2), 1 - 2 * gap, 1 - 4.4 * gap,
                           facecolor=colour, edgecolor="none"))


def figure1():
    states = read("states.csv")
    final = {(r["archive"], r["item"]): r for r in csv.DictReader(open(ROOT / "coding" / "final.csv", encoding="utf-8"))}
    fig, ax = grid_axes(states, 4.5)
    fill = {"answered": BLUE_DARK, "deferred": BLUE_LIGHT, "not public": NEUTRAL, "not stated": NEUTRAL}
    for index, row in enumerate(states):
        for column, archive in enumerate(ARCHIVES):
            state = row[archive]
            tile(ax, column, index, fill[state])
            if state != "answered":
                ax.text(column + 0.5, index + 0.5, state, ha="center", va="center",
                        color=INK if state == "deferred" else INK2, fontsize=7.5)
            if final[(archive, row["item"])]["agreement"] == "resolved":
                ax.plot(column + 0.88, index + 0.5, marker="o", markersize=4.2, color=SURFACE,
                        markeredgecolor=SURFACE, linestyle="none")
    handles = [
        Patch(facecolor=BLUE_DARK, label="answered in a public document"),
        Patch(facecolor=BLUE_LIGHT, label="deferred to item records or deposit conditions"),
        Patch(facecolor=NEUTRAL, label="not stated"),
        Line2D([], [], marker="o", markersize=7.5, markerfacecolor=SURFACE, markeredgecolor=BLUE_DARK,
               markeredgewidth=2.6, linestyle="none", label="the two coders differed; resolved"),
    ]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.01), ncol=2, frameon=False,
              fontsize=7.5, handlelength=1.4, columnspacing=1.6, labelcolor=INK2)
    save(fig, "figure1_states")


def figure2():
    authority = read("authority.csv")
    states = {(r["item"], a): r[a] for r in read("states.csv") for a in ARCHIVES}
    items = ["DM1", "DM2", "DM3", "DM4"]
    # Space and a vertical rule between the panels keep the three archives apart.
    fig, axes = plt.subplots(1, 3, figsize=(6.3, 2.5), sharey=True,
                             gridspec_kw={"wspace": 0.26, "left": 0.235, "right": 0.995, "top": 0.70, "bottom": 0.2})
    for ax, archive in zip(axes, ARCHIVES):
        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(3.5, -0.5)
        ax.set_facecolor(SURFACE)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.tick_params(length=0)
        ax.set_xticks(range(4))
        ax.set_xticklabels([ACT[i] for i in items], color=INK2, fontsize=7.5)
        ax.xaxis.tick_top()
        ax.set_yticks(range(4))
        ax.set_yticklabels(PARTIES, color=INK2, fontsize=8)
        for y in range(4):
            ax.plot([-0.5, 3.5], [y, y], color=GRID, linewidth=0.8, zorder=0)
        ax.set_title(archive, color=INK, fontsize=8.5, fontweight="bold", pad=19)
        for x, item in enumerate(items):
            if states[(item, archive)] != "answered":
                ax.add_patch(Rectangle((x - 0.36, -0.42), 0.72, 3.84, facecolor=NEUTRAL, edgecolor="none", zorder=1))
                ax.text(x, 1.5, states[(item, archive)], rotation=90, ha="center", va="center", color=INK2, fontsize=7.5)
        for row in authority:
            if row["archive"] != archive:
                continue
            x, y = items.index(row["item"]), PARTIES.index(row["party"])
            if row["basis"] == "fallback":
                ax.plot(x, y, marker="o", markersize=7.5, markerfacecolor=SURFACE, markeredgecolor=BLUE,
                        markeredgewidth=1.6, linestyle="none", zorder=3)
            else:
                ax.plot(x, y, marker="o", markersize=8.5, markerfacecolor=BLUE, markeredgecolor=SURFACE,
                        markeredgewidth=1.2, linestyle="none", zorder=3)
    fig.canvas.draw()
    for left, right in zip(axes[:-1], axes[1:]):
        x = (left.get_position().x1 + right.get_position().x0) / 2
        fig.add_artist(Line2D([x, x], [0.17, 0.97], transform=fig.transFigure, color=MUTED, linewidth=0.9))
    handles = [
        Line2D([], [], marker="o", markersize=7, markerfacecolor=BLUE, markeredgecolor=SURFACE, linestyle="none",
               label="named as deciding"),
        Line2D([], [], marker="o", markersize=6.4, markerfacecolor=SURFACE, markeredgecolor=BLUE, markeredgewidth=1.5,
               linestyle="none", label="decides only if the depositor cannot be reached"),
        Patch(facecolor=NEUTRAL, label="left to item records or deposit conditions"),
    ]
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.0, -0.03), ncol=3, frameon=False, fontsize=7.5,
               handlelength=1.2, columnspacing=1.4, labelcolor=INK2)
    save(fig, "figure2_authority")


def figure3():
    provenance = read("provenance.csv")
    cell = {(r["archive"], r["item"]): r for r in provenance}
    rows, seen = [], set()
    for r in provenance:
        if r["item"] not in seen:
            seen.add(r["item"])
            rows.append({"field": r["field"], "item": r["item"]})
    fig, ax = grid_axes(rows, 4.5)
    for index, row in enumerate(rows):
        for column, archive in enumerate(ARCHIVES):
            entry = cell[(archive, row["item"])]
            if entry["state"] == "answered":
                tile(ax, column, index, GENRE[entry["genre"]])
                ax.text(column + 0.5, index + 0.5, GENRE_SHORT[entry["genre"]], ha="center", va="center",
                        color="#ffffff", fontsize=7.5, fontweight="bold")
            else:
                tile(ax, column, index, NEUTRAL)
                ax.text(column + 0.5, index + 0.5, entry["state"], ha="center", va="center", color=INK2, fontsize=7.5)
    handles = [
        Patch(facecolor=GENRE["deposit document"], label="deposit agreement, form or instructions"),
        Patch(facecolor=GENRE["terms or policy"], label="terms, conditions or policy for users"),
        Patch(facecolor=GENRE["help or information page"], label="help, FAQ or information page"),
        Patch(facecolor=NEUTRAL, label="no answer in a public document"),
    ]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.01), ncol=2, frameon=False,
              fontsize=7.5, handlelength=1.4, columnspacing=1.6, labelcolor=INK2)
    save(fig, "figure3_provenance")


if __name__ == "__main__":
    figure1()
    figure2()
    figure3()
    print("wrote figure1_states, figure2_authority and figure3_provenance (png, svg, pdf) in analysis/")

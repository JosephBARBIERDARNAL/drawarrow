import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects
from matplotlib.patches import Circle
from drawarrow import fig_arrow
from pypalettes import get_hex

colors = get_hex("Acadia")

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.set_axis_off()
fig.patch.set_alpha(0)
circle = Circle(
    (0.5, 0.5),
    0.34,
    facecolor=colors[4],
    edgecolor=colors[4],
    linewidth=40,
    alpha=0.9,
    transform=fig.transFigure,
)
ax.add_artist(circle)
font = FontProperties(fname="logo/OPERATINGINSTRUCTIONS.ttf")
text = fig.text(
    x=0.5,
    y=0.5 + 0.03,
    s="Draw\nArrow",
    fontsize=150,
    ha="center",
    va="center",
    font=font,
    color=colors[0],
    zorder=10,
)
text.set_path_effects(
    [path_effects.Stroke(linewidth=3, foreground=colors[1]), path_effects.Normal()]
)
shadow = fig.text(
    x=0.506,
    y=0.494 + 0.03,
    s="Draw\nArrow",
    fontsize=150,
    ha="center",
    va="center",
    font=font,
    color=colors[1],
    alpha=0.3,
    zorder=1,
)

plt.savefig("logo/logo.png", dpi=300, bbox_inches="tight", pad_inches=0.1)

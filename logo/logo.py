import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects
from drawarrow import fig_arrow
from pypalettes import get_hex, load_cmap
import numpy as np
from PIL import Image, ImageDraw

colors = get_hex("Acadia")
cmap = load_cmap("Alosa_fallax", type="continuous", type_warning=False)

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.set_axis_off()

# Create gradient background
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.repeat(gradient, 256, axis=0)
ax.imshow(gradient, cmap=cmap, aspect="auto", extent=[0, 1, 0, 1])

font = FontProperties(fname="logo/OPERATINGINSTRUCTIONS.ttf")
text = fig.text(
    x=0.5,
    y=0.5,
    s="Draw\nArrow",
    fontsize=180,
    ha="center",
    va="center",
    font=font,
    color=colors[0],
    zorder=10,
)
text.set_path_effects(
    [path_effects.Stroke(linewidth=4, foreground=colors[1]), path_effects.Normal()]
)
shadow = fig.text(
    x=0.506,
    y=0.494,
    s="Draw\nArrow",
    fontsize=180,
    ha="center",
    va="center",
    font=font,
    color=colors[1],
    alpha=0.3,
    zorder=1,
)

# Save the figure without displaying it
plt.savefig(
    "logo/temp_logo.png", dpi=300, bbox_inches="tight", pad_inches=0, transparent=True
)
plt.close(fig)

# Open the saved image
img = Image.open("logo/temp_logo.png")

# Create a mask
mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + img.size, fill=255)

# Apply the mask
output = Image.new("RGBA", img.size, (0, 0, 0, 0))
output.paste(img, (0, 0), mask)

# Save the final circular logo
output.save("logo/logo.png", "PNG")

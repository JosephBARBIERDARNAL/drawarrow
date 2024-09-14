import matplotlib.pyplot as plt
from drawarrow import fig_arrow, ax_arrow

path_for_imgs = "tests/manual_checks"


def save_arrow(arrow_code, count):
    fig, ax = plt.subplots()
    exec(arrow_code)
    fig.text(x=0.7, y=0.2, s=arrow_code, size=8, backgroundcolor="beige")
    ax.scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], s=100)
    ax.spines[["top", "right"]].set_visible(False)
    plt.savefig(f"{path_for_imgs}/example-{count}.png", dpi=300, bbox_inches="tight")
    plt.close()


arrow_codes = [
    """
fig_arrow(
    head_position=(0.5, 0.5),
    tail_position=(0.2, 0.7),
    radius=0.1,
    color="red"
)
    """,
    """
fig_arrow(
   (0.2,0.3),
   (0.5,0.8),
   head_width=4,
   head_length=10,
   linewidth=1.2,
   double_headed=True,
   fill_head=False
)
    """,
]

for count, arrow_code in enumerate(arrow_codes):
    save_arrow(arrow_code=arrow_code, count=count + 1)

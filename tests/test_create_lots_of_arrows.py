"""
This script generates lots of images when running tests for manual validation.
The images must either not change (according to Git), or be manually validated.
"""

import matplotlib.pyplot as plt
from drawarrow import fig_arrow, ax_arrow

path_for_imgs = "tests/manual_checks"


def save_arrow(arrow_code, count):
    fig, ax = plt.subplots()
    exec(arrow_code)
    fig.text(
        x=0.6,
        y=0.2,
        s=arrow_code,
        size=8,
        bbox={"edgecolor": "black", "facecolor": "beige"},
    )
    ax.scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], s=100)
    ax.spines[["top", "right"]].set_visible(False)
    plt.savefig(f"{path_for_imgs}/example-{count}.png", dpi=300, bbox_inches="tight")
    plt.close()


arrow_codes = [
    """
fig_arrow(
    tail_position=(0.2, 0.7),
    head_position=(0.5, 0.5),
    radius=0.1,
    color='red'
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   head_width=4,
   head_length=10,
   double_headed=True,
   fill_head=False
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   head_width=4,
   head_length=10,
   width=2,
   fill_head=False,
   color='blue'
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   inflection_position=(0.25, 0.7),
   head_width=4,
   head_length=10,
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   inflection_position=(0.25, 0.7),
   double_headed=True,
   head_width=4,
   head_length=10,
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   inflection_position=(0.25, 0.7),
   shadow_style={
    'shadow_color':'blue',
    'alpha':0.4,
    'offset':(-4,4)
    },
   double_headed=True,
   color='black',
   head_width=4,
   head_length=10,
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   shadow_style={'offset':(2,-5)},
   double_headed=True,
   fill_head=False,
   head_width=4,
   head_length=10,
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   double_headed=True,
   radius=0.8,
   fill_head=False,
   head_width=4,
   head_length=10,
)
    """,
    """
fig_arrow(
   tail_position=(0.2,0.3),
   head_position=(0.5,0.8),
   inflection_position=(0.25, 0.7),
   double_headed=True,
   radius=2,
   fill_head=False,
   head_width=4,
   head_length=10,
)
    """,
]

for count, arrow_code in enumerate(arrow_codes):
    save_arrow(arrow_code=arrow_code, count=count + 1)

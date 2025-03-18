import matplotlib.pyplot as plt
from drawarrow import ax_arrow


def arrow_spines(ax=None, **arrow_style):
    """
    Remove spines in a matplotlib Axes and add arrows (left to right and bottom to top) instead.

    Parameters:

    - `ax`: The matplotlib axes to draw the arrow on. If None, uses the current axes
    - `arrow_style`: any additional arguments passed to `ax_arrow`
    """
    if ax is None:
        ax = plt.gca()

    ax.spines[["top", "bottom", "right", "left"]].set_visible(False)

    default_arrow_style = dict(
        ax=ax,
        clip_on=False,
        zorder=10,
        color="black",
        fill_head=False,
        transform=ax.transAxes,
    )
    default_arrow_style.update(arrow_style)

    # left to right arrow
    ax_arrow([0 - 0.005, 0], [1.02, 0], **default_arrow_style)

    # bottom to top arrow
    ax_arrow([0, 0 - 0.005], [0, 1.02], **default_arrow_style)


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])
    arrow_spines(ax, color="red")
    fig.savefig("cache.png", dpi=300)

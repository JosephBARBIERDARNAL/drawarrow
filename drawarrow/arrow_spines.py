import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from typing import Union
from drawarrow import ax_arrow


def arrow_spines(
    bottom="toright",
    left="totop",
    right=None,
    top=None,
    ax: Union[Axes, None] = None,
    **arrow_style,
) -> Axes:
    """
    Replace matplotlib spines with arrows instead. By default it adds an arrow at the bottom spine (to the right) and an arrow at the left spine (to the top), but it can customized. See examples below.

    Parameters:

    - `bottom`: direction of the arrow (either 'toright' or 'toleft'). No arrow if `None`
    - `top`: direction of the arrow (either 'toright' or 'toleft'). No arrow if `None` (default)
    - `left`: direction of the arrow (either 'totop' or 'tobottom'). No arrow if `None`
    - `right`: direction of the arrow (either 'totop' or 'tobottom'). No arrow if `None` (default)
    - `ax`: The matplotlib axes to draw the arrow on. If None, uses the current axes
    - `arrow_style`: any additional arguments passed to [`ax_arrow()`](ax_arrow.md)

    Returns:

    - `Axes`: the matplotlib axes

    Usage

    ```python
    import matplotlib.pyplot as plt
    from drawarrow import arrow_spines

    fig, ax = plt.subplots()
    arrow_spines(ax=ax, color="red")
    plt.show()
    ```
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

    if bottom is not None:
        if bottom == "toright":
            # left to right arrow
            ax_arrow([0 - 0.005, 0], [1.02, 0], **default_arrow_style)
        elif bottom == "toleft":
            # right to left arrow
            ax_arrow([1 + 0.005, 0], [0 - 0.005, 0], **default_arrow_style)
        else:
            raise ValueError(
                f"bottom must be one of: 'toright', 'toleft', None, not '{bottom}'"
            )

    if left is not None:
        if left == "totop":
            # bottom to top arrow
            ax_arrow([0, 0 - 0.005], [0, 1.02], **default_arrow_style)
        elif left == "tobottom":
            # top to bottom arrow
            ax_arrow([0, 1], [0, 0 - 0.005], **default_arrow_style)
        else:
            raise ValueError(
                f"left must be one of: 'totop', 'tobottom', None, not '{left}'"
            )

    if top is not None:
        if top == "toleft":
            # right to left arrow
            ax_arrow([1 + 0.005, 1], [0 - 0.005, 1], **default_arrow_style)
        elif top == "toright":
            # left to right arrow
            ax_arrow([0 - 0.005, 1], [1 + 0.005, 1], **default_arrow_style)
        else:
            raise ValueError(
                f"top must be one of: 'toright', 'toleft', None, not '{top}'"
            )

    if right is not None:
        if right == "tobottom":
            # top to bottom arrow
            ax_arrow([1, 1], [1, 0 - 0.005], **default_arrow_style)
        elif right == "totop":
            # bottom to top arrow
            ax_arrow([1, 0 - 0.005], [1, 1.02], **default_arrow_style)
        else:
            raise ValueError(
                f"right must be one of: 'totop', 'tobottom', None, not '{right}'"
            )

    return ax


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])
    arrow_spines(ax=ax, color="red")
    fig.savefig("cache.png", dpi=300)

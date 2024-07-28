import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import warnings


def _create_arrow(
    tail_position,
    head_position,
    invert: bool = False,
    radius: float = 0.1,
    tail_width: float = 0.5,
    head_width: float = 4,
    head_length: float = 8,
    **FAPargs,
):
    """
    Create a FancyArrowPatch object.

    Parameters:
    - `tail_position` (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - `head_position` (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - `invert` (bool, default to False): whether to invert or not the angle of the arrow (only used if `radius`!=0)
    - `radius` (float, default to 0.1):
    - `tail_width` (float, default to 0.5): Width of the tail of the arrow
    - `head_width` (float, default to 4): Head width of the tail of the arrow
    - `head_length` (float, default to 8): Head length of the tail of the arrow
    - `FAPargs`: FancyArrowPatch additional arguments (color, linewidth, alpha...)

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """

    if invert and radius == 0:
        warnings.warn(
            "`invert` argument is ignored when radius is 0. Use `invert=False` to remove this warning."
        )

    kw = dict(
        arrowstyle=f"Simple, tail_width={tail_width}, head_width={head_width}, head_length={head_length}",
        **FAPargs,
    )
    connectionstyle = f"arc3,rad={-radius if invert else radius}"
    return FancyArrowPatch(
        tail_position, head_position, connectionstyle=connectionstyle, **kw
    )


def fig_arrow(
    tail_position, head_position, fig: Figure | None = None, **kwargs
) -> None:
    """
    Draw an arrow on a Matplotlib Figure using a FancyArrowPatch.

    Parameters:
    - `tail_position` (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - `head_position` (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - fig (Figure): The matplotlib figure to draw the arrow on.

    Returns:
    - None
    """
    if fig is None:
        fig = plt.gcf()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    arrow.set_transform(fig.transFigure)
    fig.patches.append(arrow)


def ax_arrow(tail_position, head_position, ax: Axes | None = None, **kwargs) -> None:
    """
    Draw an arrow on a Matplotlib Axes using a FancyArrowPatch.

    Parameters:
    - `tail_position` (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - `head_position` (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - ax (Axes): The matplotlib axes to draw the arrow on. If None, uses the current axes.

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """
    if ax is None:
        ax = plt.gca()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    ax.add_patch(arrow)

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
    [... same as before ...]

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
    - fig (Figure): The matplotlib figure to draw the arrow on.
    [... other parameters same as _create_arrow ...]

    Returns:
    - None
    """
    if fig is None:
        fig = plt.gcf()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    arrow.set_transform(fig.transFigure)
    fig.patches.append(arrow)


def ax_arrow(
    tail_position, head_position, ax: Axes | None = None, **kwargs
) -> FancyArrowPatch:
    """
    Draw an arrow on a Matplotlib Axes using a FancyArrowPatch.

    Parameters:
    - ax (Axes): The matplotlib axes to draw the arrow on. If None, uses the current axes.
    [... other parameters same as _create_arrow ...]

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """
    if ax is None:
        ax = plt.gca()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    ax.add_patch(arrow)

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def _create_arrow(
    tail_position,
    head_position,
    invert=False,
    radius=0.1,
    color="black",
    tail_width=0.5,
    head_width=4,
    head_length=8,
    linewidth=0.5,
):
    """
    Create a FancyArrowPatch object.

    Parameters:
    [... same as before ...]

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """
    kw = dict(
        arrowstyle=f"Simple, tail_width={tail_width}, head_width={head_width}, head_length={head_length}",
        color=color,
        lw=linewidth,
    )
    connectionstyle = f"arc3,rad={-radius if invert else radius}"
    return FancyArrowPatch(
        tail_position, head_position, connectionstyle=connectionstyle, **kw
    )


def fig_arrow(tail_position, head_position, fig=None, **kwargs):
    """
    Draw an arrow on a Matplotlib Figure.

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


def ax_arrow(tail_position, head_position, ax=None, **kwargs):
    """
    Draw an arrow on a Matplotlib Axes.

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
    return arrow

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import Union

from .arrow_patch import _create_arrow


def fig_arrow(
    tail_position, head_position, fig: Union[Figure, None] = None, **kwargs
) -> FancyArrowPatch:
    """
    Draws an arrow on a Matplotlib Figure using a FancyArrowPatch.

    Parameters:
    - tail_position (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - head_position (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - fig (Figure): The matplotlib figure to draw the arrow on.

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """
    if fig is None:
        fig = plt.gcf()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    arrow.set_transform(fig.transFigure)
    fig.patches.append(arrow)

    return arrow


def ax_arrow(
    tail_position, head_position, ax: Union[Axes, None] = None, **kwargs
) -> FancyArrowPatch:
    """
    Draws an arrow on a Matplotlib Axes using a FancyArrowPatch.

    Parameters:
    - tail_position (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - head_position (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - ax (Axes): The matplotlib axes to draw the arrow on. If None, uses the current axes.

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """
    if ax is None:
        ax = plt.gca()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    ax.add_patch(arrow)

    return arrow

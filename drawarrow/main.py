import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib.patheffects as path_effects
from typing import Union

from .arrow_patch import _create_arrow


def fig_arrow(
    tail_position,
    head_position,
    fig: Union[Figure, None] = None,
    shadow_style: Union[dict, None] = None,
    **kwargs,
) -> FancyArrowPatch:
    """
    Draws an arrow on a Matplotlib Figure using a FancyArrowPatch.

    Parameters:
    - tail_position (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - head_position (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - fig (Figure): matplotlib figure to draw the arrow on. If it is not supplied, it will use `matplotlib.pyplot.gcf()`.
    - shadow_style (dict): dictionary with arguments passed to `matplotlib.patheffects.SimpleLineShadow`. The main
    useful arguments are:
        - `offset` (array-like of length 2, default to (2, -2)): the offset between the arrow and its shadow.
        - `shadow_color` (any matplotlib color, default to 'black'): the color of the shadow
        - `alpha` (float between 0 and 1, default to 0.3): the opacity of the shadow
    - **kwargs: any additional arguments passed to `matplotlib.patches.FancyArrowPatch`.

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """
    if fig is None:
        fig = plt.gcf()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    arrow.set_transform(fig.transFigure)
    fig.patches.append(arrow)

    if shadow_style is not None:
        arrow.set_path_effects(
            [path_effects.SimpleLineShadow(**shadow_style), path_effects.Normal()]
        )

    return arrow


def ax_arrow(
    tail_position,
    head_position,
    ax: Union[Axes, None] = None,
    shadow_style: Union[dict, None] = None,
    **kwargs,
) -> FancyArrowPatch:
    """
    Draws an arrow on a Matplotlib Axes using a FancyArrowPatch.

    Parameters:
    - tail_position (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - head_position (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - ax (Axes): The matplotlib axes to draw the arrow on. If None, uses the current axes.
    - shadow_style (dict): dictionary with arguments passed to `matplotlib.patheffects.SimpleLineShadow`:
        - `offset` (array-like of length 2, default to (2, -2)): the offset between the arrow and its shadow.
        - `shadow_color` (any matplotlib color, default to 'black'): the color of the shadow
        - `alpha` (float between 0 and 1, default to 0.3): the opacity of the shadow
    - **kwargs: any additional arguments passed to `matplotlib.patches.FancyArrowPatch`.

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """
    if ax is None:
        ax = plt.gca()

    arrow = _create_arrow(tail_position, head_position, **kwargs)
    ax.add_patch(arrow)

    if shadow_style is not None:
        arrow.set_path_effects(
            [path_effects.SimpleLineShadow(**shadow_style), path_effects.Normal()]
        )

    return arrow

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
    inflection_position=None,
    double_headed: bool = False,
    fill_head: bool = True,
    invert: bool = False,
    radius: float = 0,
    width: float = 1,
    head_width: float = 4,
    head_length: float = 8,
    fig: Union[Figure, None] = None,
    shadow_style: Union[dict, None] = None,
    **kwargs,
) -> FancyArrowPatch:
    """
    Draws an arrow on a Matplotlib Figure using a FancyArrowPatch.

    Parameters:
    - tail_position (array-like of length 2): Position of the tail of the arrow (on the figure/axes)
    - head_position (array-like of length 2): Position of the head of the arrow (on the figure/axes)
    - inflection_position (array-like of length 2): Optional position of the inflection point (on the figure/axes)
    - double_headed (bool): Whether the arrow has two heads or not.
    - fill_head (bool): Whether the arrowhead is filled or not.
    - invert (bool): Whether to invert or not the angle of the arrow (only used if `radius`!=0)
    - radius (float): Rounding radius of the edge. If `inflection_position` is not None, then
    it's the rounding radius at the inflection point.
    - width (float): Width of the tail of the arrow
    - head_width (float): Head width of the tail of the arrow
    - head_length (float): Head length of the tail of the arrow
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

    arrow = _create_arrow(
        tail_position=tail_position,
        head_position=head_position,
        inflection_position=inflection_position,
        double_headed=double_headed,
        fill_head=fill_head,
        invert=invert,
        radius=radius,
        width=width,
        head_width=head_width,
        head_length=head_length,
        **kwargs,
    )
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
    inflection_position=None,
    double_headed: bool = False,
    fill_head: bool = True,
    invert: bool = False,
    radius: float = 0,
    width: float = 1,
    head_width: float = 4,
    head_length: float = 8,
    ax: Union[Axes, None] = None,
    shadow_style: Union[dict, None] = None,
    **kwargs,
) -> FancyArrowPatch:
    """
    Draws an arrow on a Matplotlib Axes using a FancyArrowPatch.

    Parameters:
    - tail_position (array-like of length 2): Position of the tail of the arrow (on the figure/axes)
    - head_position (array-like of length 2): Position of the head of the arrow (on the figure/axes)
    - inflection_position (array-like of length 2): Optional position of the inflection point (on the figure/axes)
    - double_headed (bool): Whether the arrow has two heads or not.
    - fill_head (bool): Whether the arrowhead is filled or not.
    - invert (bool): Whether to invert or not the angle of the arrow (only used if `radius`!=0)
    - radius (float): Rounding radius of the edge. If `inflection_position` is not None, then
    it's the rounding radius at the inflection point.
    - width (float): Width of the tail of the arrow
    - head_width (float): Head width of the tail of the arrow
    - head_length (float): Head length of the tail of the arrow
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

    arrow = _create_arrow(
        tail_position=tail_position,
        head_position=head_position,
        inflection_position=inflection_position,
        double_headed=double_headed,
        fill_head=fill_head,
        invert=invert,
        radius=radius,
        width=width,
        head_width=head_width,
        head_length=head_length,
        **kwargs,
    )
    ax.add_patch(arrow)

    if shadow_style is not None:
        arrow.set_path_effects(
            [path_effects.SimpleLineShadow(**shadow_style), path_effects.Normal()]
        )

    return arrow

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
    Draw an arrow on a Matplotlib figure using a `FancyArrowPatch`. The coordinate system used is that of a Matplotlib Figure (from 0 to 1).

    This function is very similar to what `ax_arrow()` does: only the change of coordinate system and the `fig/ax` arguments. You can find out more about how coordinate systems work in Matplotlib [here](https://python-graph-gallery.com/589-how-to-change-coordinate-system/).

    Parameters

    - `tail_position`: Position of the tail of the arrow
    - `head_position`: Position of the head of the arrow
    - `inflection_position`: Current behavior may be unexpected and will probably change in the future. Optional position of the inflection point
    - `double_headed`: Whether the arrow has two heads or not
    - `fill_head`: Whether the arrowhead is filled or not
    - `invert`: Whether to invert or not the angle of the arrow (only used if `radius`!=0)
    - `radius`: Rounding radius of the edge. If `inflection_position` is not None, then
    it's the rounding radius at the inflection point
    - `width`: Width of the tail of the arrow
    - `head_width`: Head width of the tail of the arrow
    - `head_length`: Head length of the tail of the arrow
    - `fig`: matplotlib figure to draw the arrow on. If it is not supplied, it will use `matplotlib.pyplot.gcf()`.
    - `shadow_style`: dictionary with arguments passed to `matplotlib.patheffects.SimpleLineShadow`. The main
    useful arguments are:
        - `offset`: the offset between the arrow and its shadow
        - `shadow_color`: the color of the shadow
        - `alpha`: the opacity of the shadow
    - `kwargs`: any additional arguments passed to `matplotlib.patches.FancyArrowPatch`

    Returns

    - `FancyArrowPatch`: The arrow patch object

    Usage

    ```python
    import matplotlib.pyplot as plt
    from drawarrow import fig_arrow

    fig, ax = plt.subplots()

    fig_arrow([0.1, 0.7], [0.1, 0.5], radius=0.3, color="red", ax=ax)

    plt.show()
    ```
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
    Draw an arrow on a Matplotlib axes using a `FancyArrowPatch`. The coordinate system used is that of a Matplotlib axes (data coordinates).

    This function is very similar to what `fig_arrow()` does: only the change of coordinate system and the `fig/ax` arguments. You can find out more about how coordinate systems work in Matplotlib [here](https://python-graph-gallery.com/589-how-to-change-coordinate-system/).

    Parameters

    - `tail_position`: Position of the tail of the arrow
    - `head_position`: Position of the head of the arrow
    - `inflection_position`: Current behavior may be unexpected and will probably change in the future. Optional position of the inflection point
    - `double_headed`: Whether the arrow has two heads or not
    - `fill_head`: Whether the arrowhead is filled or not
    - `invert`: Whether to invert or not the angle of the arrow (only used if `radius`!=0)
    - `radius`: Rounding radius of the edge. If `inflection_position` is not None, then
    it's the rounding radius at the inflection point
    - `width`: Width of the tail of the arrow
    - `head_width`: Head width of the tail of the arrow
    - `head_length`: Head length of the tail of the arrow
    - `ax`: The matplotlib axes to draw the arrow on. If None, uses the current axes
    - `shadow_style`: dictionary with arguments passed to `matplotlib.patheffects.SimpleLineShadow`:
        - `offset`: the offset between the arrow and its shadow
        - `shadow_color`: the color of the shadow
        - `alpha`: the opacity of the shadow
    - `kwargs`: any additional arguments passed to `matplotlib.patches.FancyArrowPatch`

    Returns

    - `FancyArrowPatch`: The arrow patch object

    Usage

    ```python
    import matplotlib.pyplot as plt
    from drawarrow import ax_arrow

    fig, ax = plt.subplots()

    ax_arrow([0.1, 0.7], [0.1, 0.5], radius=0.3, color="red", ax=ax)

    plt.show()
    ```
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

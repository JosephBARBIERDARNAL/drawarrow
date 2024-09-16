"""
Module with the main (private) function for creating custom arrow patches using Matplotlib.
"""

from matplotlib.patches import FancyArrowPatch, ArrowStyle, ConnectionStyle
import warnings

from .utils import (
    _angles_from_positions,
    _find_stylename_arrowstyle,
    _find_stylename_connectionstyle,
)


def _create_arrow(
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
    **FAPargs,
) -> FancyArrowPatch:
    """
    Creates a FancyArrowPatch object with customized connection and arrow style.

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
    - **FAPargs: FancyArrowPatch additional arguments (color, zorder, alpha...)

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """

    if invert and radius == 0:
        warnings.warn(
            "`invert` argument is ignored when radius is 0. "
            "Delete `invert=True` to remove this warning."
        )

    rad = -radius if invert else radius

    if "linewidth" in FAPargs.keys():
        warnings.warn(
            "The `linewidth` property is overwritten by the `width` property. "
            "Please use `width` instead."
        )
    FAPargs["linewidth"] = width

    stylename = _find_stylename_arrowstyle(double_headed, fill_head)
    arrowstyle_args = dict(
        stylename=stylename, head_width=head_width, head_length=head_length
    )
    arrowstyle = ArrowStyle(**arrowstyle_args)

    stylename, rad = _find_stylename_connectionstyle(inflection_position, rad)
    connectionstyle_args = dict(stylename=stylename, rad=rad)
    if inflection_position is not None:
        angleA, angleB = _angles_from_positions(
            tail_position, inflection_position, head_position
        )
        connectionstyle_args["angleA"] = angleA
        connectionstyle_args["angleB"] = angleB
    connectionstyle = ConnectionStyle(**connectionstyle_args)

    return FancyArrowPatch(
        tail_position,
        head_position,
        connectionstyle=connectionstyle,
        arrowstyle=arrowstyle,
        **FAPargs,
    )

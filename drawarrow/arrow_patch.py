"""
Module with private functions for creating custom arrow patches using Matplotlib.
"""

from matplotlib.patches import FancyArrowPatch, ArrowStyle
import warnings


def _create_arrow(
    tail_position,
    head_position,
    double_headed: bool = False,
    fill_head: bool = True,
    invert: bool = False,
    radius: float = 0.1,
    tail_width: float = 1,
    head_width: float = 4,
    head_length: float = 8,
    **FAPargs,
) -> FancyArrowPatch:
    """
    Creates a FancyArrowPatch object.

    Parameters:
    - `tail_position` (array-like of length 2): position of the tail of the arrow (on the figure/axes)
    - `head_position` (array-like of length 2): position of the head of the arrow (on the figure/axes)
    - `invert` (bool, default to False): whether to invert or not the angle of the arrow (only used if `radius`!=0)
    - `radius` (float, default to 0.1):
    - `tail_width` (float, default to 1): Width of the tail of the arrow
    - `head_width` (float, default to 4): Head width of the tail of the arrow
    - `head_length` (float, default to 8): Head length of the tail of the arrow
    - `FAPargs`: FancyArrowPatch additional arguments (color, zorder, alpha...)

    Returns:
    - FancyArrowPatch: The arrow patch object.
    """

    if invert and radius == 0:
        warnings.warn(
            "`invert` argument is ignored when radius is 0. Use `invert=False` to remove this warning."
        )
    FAPargs["linewidth"] = tail_width

    if double_headed:
        if fill_head:
            stylename = "<|-|>"
        else:
            stylename = "<->"
    else:
        if fill_head:
            stylename = "-|>"
        else:
            stylename = "->"

    arrowstyle = ArrowStyle(
        stylename=stylename, head_width=head_width, head_length=head_length
    )

    kw = dict(
        arrowstyle=arrowstyle,
        **FAPargs,
    )
    connectionstyle = f"arc3,rad={-radius if invert else radius}"
    return FancyArrowPatch(
        tail_position, head_position, connectionstyle=connectionstyle, **kw
    )

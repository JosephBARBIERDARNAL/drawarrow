"""
Module containing utility functions for:

- finding the valid stylename when defining the `matplotlib.patches.ArrowStyle`
and `matplotlib.patches.ConnectionStyle` for the `matplotlib.patches.FancyArrowPatch`.
- calculating angles between positions for arrows with an inflection point.
"""

import math


def _find_stylename_arrowstyle(double_headed: bool, fill_head: bool):
    """
    Finds the valid stylename when defining the `matplotlib.patches.ArrowStyle`
    for the `matplotlib.patches.FancyArrowPatch`.

    Parameters:
    - double_headed (bool): If True, the arrow will have two heads.
    - fill_head (bool): If True, the arrow head will be filled.

    Returns:
    - str: The valid stylename for the arrow style.
    """
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
    return stylename


def _find_stylename_connectionstyle(inflection_position, rad):
    """
    Determines the stylename and adjusts the radius for the connection style based on the inflection position.

    Parameters:
    - inflection_position (None or any): The position of the inflection point. If None, it indicates no inflection point.
    - rad (float): The initial radius for the connection style.

    Returns:
    - tuple: A tuple containing the stylename and the adjusted radius for the connection style.
    """
    if inflection_position is None:
        stylename = "arc3"
    else:
        stylename = "angle"
        # For some reason, this type of connection style requires
        # a much larger radius to be sufficiently visible.
        # I don't know why, but multiplying it by 100 seems to
        # solve the problem.
        rad = rad * 100
    return stylename, rad


def _magnitude(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)


def _dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def _angle_with_x_axis(v):
    return math.degrees(math.atan2(v[1], v[0]))


def _angles_from_positions(pos_A, pos_B, pos_C):
    """
    Calculates the angles between three positions in a 2D space.

    This function calculates the angles between the vectors AB and BC, where A, B, and C
    are positions in a 2D space. It returns the angles of these vectors with respect to
    the x-axis. It is used to create an arrow with an inflection point because it needs
    angles to define it.

    Parameters:
    - pos_A (tuple of length 2): The position of point A.
    - pos_B (tuple of length 2): The position of point B.
    - pos_C (tuple of length 2): The position of point C.

    Returns:
    - tuple of two floats: The angles of vectors AB and BC with respect to the x-axis in degrees.
    """

    invalid_inputs_msg = "The position of the inflection point appears to be invalid. Please try another value"

    AB = (pos_B[0] - pos_A[0], pos_B[1] - pos_A[1])
    BC = (pos_C[0] - pos_B[0], pos_C[1] - pos_B[1])

    magnitude_AB = _magnitude(AB)
    magnitude_BC = _magnitude(BC)

    dot_AB_BC = _dot_product(AB, BC)

    try:
        cos_theta = dot_AB_BC / (magnitude_AB * magnitude_BC)
    except ZeroDivisionError:
        raise ValueError(invalid_inputs_msg)
    cos_theta = max(-1, min(1, cos_theta))

    angle_between_AB_BC = math.degrees(math.acos(cos_theta))

    angleA = _angle_with_x_axis(AB)
    angleB = _angle_with_x_axis(BC)

    if abs(angleA - angleB) < 0.5:
        raise ValueError(invalid_inputs_msg)

    return angleA, angleB

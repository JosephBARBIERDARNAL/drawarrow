"""
Module containing utility functions for calculating angles between positions.
"""

import math


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

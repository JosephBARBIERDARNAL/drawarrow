import pytest
import math
from drawarrow.utils import (
    _magnitude,
    _angle_with_x_axis,
    _dot_product,
    _angles_from_positions,
)


def test_magnitude_positive():
    assert math.isclose(_magnitude((3, 4)), 5, rel_tol=1e-9)


def test_magnitude_negative():
    assert math.isclose(_magnitude((-3, -4)), 5, rel_tol=1e-9)


def test_magnitude_zero():
    assert math.isclose(_magnitude((0, 0)), 0, rel_tol=1e-9)


def test_magnitude_large_numbers():
    assert math.isclose(_magnitude((1e6, 1e6)), math.sqrt(2) * 1e6, rel_tol=1e-9)


def test_dot_product_positive():
    assert math.isclose(_dot_product((1, 2), (3, 4)), 11, rel_tol=1e-9)


def test_dot_product_negative():
    assert math.isclose(_dot_product((-1, -2), (3, 4)), -11, rel_tol=1e-9)


def test_dot_product_zero():
    assert math.isclose(_dot_product((0, 0), (3, 4)), 0, rel_tol=1e-9)


def test_dot_product_perpendicular():
    assert math.isclose(_dot_product((1, 0), (0, 1)), 0, rel_tol=1e-9)


def test_angle_with_x_axis_positive():
    assert math.isclose(_angle_with_x_axis((1, 1)), 45, rel_tol=1e-9)


def test_angle_with_x_axis_negative():
    assert math.isclose(_angle_with_x_axis((-1, -1)), -135, rel_tol=1e-9)


def test_angle_with_x_axis_zero():
    assert math.isclose(_angle_with_x_axis((1, 0)), 0, rel_tol=1e-9)


def test_angle_with_x_axis_90_degrees():
    assert math.isclose(_angle_with_x_axis((0, 1)), 90, rel_tol=1e-9)


def test_angle_with_x_axis_180_degrees():
    assert math.isclose(_angle_with_x_axis((-1, 0)), 180, rel_tol=1e-9)


def test_angle_with_x_axis_270_degrees():
    assert math.isclose(_angle_with_x_axis((0, -1)), -90, rel_tol=1e-9)


def test_angles_from_positions_right_angle():
    pos_A = (0, 0)
    pos_B = (1, 0)
    pos_C = (1, 1)
    angleA, angleB = _angles_from_positions(pos_A, pos_B, pos_C)
    assert math.isclose(angleA, 0, rel_tol=1e-9)
    assert math.isclose(angleB, 90, rel_tol=1e-9)


def test_angles_from_positions_acute_angle():
    pos_A = (0, 0)
    pos_B = (1, 1)
    pos_C = (2, 1)
    angleA, angleB = _angles_from_positions(pos_A, pos_B, pos_C)
    assert math.isclose(angleA, 45, rel_tol=1e-9)
    assert math.isclose(angleB, 0, rel_tol=1e-9)


def test_angles_from_positions_obtuse_angle():
    pos_A = (0, 0)
    pos_B = (1, 1)
    pos_C = (0, 2)
    angleA, angleB = _angles_from_positions(pos_A, pos_B, pos_C)
    assert math.isclose(angleA, 45, rel_tol=1e-9)
    assert math.isclose(angleB, 135, rel_tol=1e-9)


def test_angles_from_positions_straight_line():
    pos_A = (0, 0)
    pos_B = (1, 1)
    pos_C = (2, 2)
    with pytest.raises(ValueError):
        _angles_from_positions(pos_A, pos_B, pos_C)


def test_angles_from_positions_negative_coordinates():
    pos_A = (-1, -1)
    pos_B = (0, 0)
    pos_C = (1, -1)
    angleA, angleB = _angles_from_positions(pos_A, pos_B, pos_C)
    assert math.isclose(angleA, 45, rel_tol=1e-9)
    assert math.isclose(angleB, -45, rel_tol=1e-9)


def test_angles_from_positions_large_coordinates():
    pos_A = (0, 0)
    pos_B = (1e6, 1e6)
    pos_C = (2e6, 1e6)
    angleA, angleB = _angles_from_positions(pos_A, pos_B, pos_C)
    assert math.isclose(angleA, 45, rel_tol=1e-9)
    assert math.isclose(angleB, 0, rel_tol=1e-9)


def test_angles_from_positions_same_point():
    pos_A = (0, 0)
    pos_B = (0, 0)
    pos_C = (1, 1)
    with pytest.raises(ValueError):
        _angles_from_positions(pos_A, pos_B, pos_C)


def test_angles_from_positions_edge_case():
    pos_A = (0, 0)
    pos_B = (1, 0)
    pos_C = (1, 1e-10)
    angleA, angleB = _angles_from_positions(pos_A, pos_B, pos_C)
    assert math.isclose(angleA, 0, rel_tol=1e-9)
    assert math.isclose(angleB, 90, rel_tol=1e-9)
    assert angleB > 0


@pytest.mark.parametrize(
    "vector, expected",
    [
        ((3, 4), 5),
        ((-3, -4), 5),
        ((0, 0), 0),
        ((1e6, 1e6), math.sqrt(2) * 1e6),
    ],
)
def test_magnitude_parameterized(vector, expected):
    assert math.isclose(_magnitude(vector), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        ((1, 2), (3, 4), 11),
        ((-1, -2), (3, 4), -11),
        ((0, 0), (3, 4), 0),
        ((1, 0), (0, 1), 0),
    ],
)
def test_dot_product_parameterized(v1, v2, expected):
    assert math.isclose(_dot_product(v1, v2), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "vector, expected",
    [
        ((1, 1), 45),
        ((-1, -1), -135),
        ((1, 0), 0),
        ((0, 1), 90),
        ((-1, 0), 180),
        ((0, -1), -90),
    ],
)
def test_angle_with_x_axis_parameterized(vector, expected):
    assert math.isclose(_angle_with_x_axis(vector), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "pos_A, pos_B, pos_C, expected_A, expected_B",
    [
        ((0, 0), (1, 0), (1, 1), 0, 90),
        ((0, 0), (1, 1), (2, 1), 45, 0),
        ((0, 0), (1, 1), (0, 2), 45, 135),
        ((-1, -1), (0, 0), (1, -1), 45, -45),
    ],
)
def test_angles_from_positions_parameterized(
    pos_A, pos_B, pos_C, expected_A, expected_B
):
    angleA, angleB = _angles_from_positions(pos_A, pos_B, pos_C)
    assert math.isclose(angleA, expected_A, rel_tol=1e-9)
    assert math.isclose(angleB, expected_B, rel_tol=1e-9)

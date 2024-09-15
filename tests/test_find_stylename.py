import pytest
import math
from drawarrow.utils import _find_stylename_arrowstyle, _find_stylename_connectionstyle


@pytest.mark.parametrize(
    "double_headed, fill_head, stylename",
    [
        (True, True, "<|-|>"),
        (True, False, "<->"),
        (False, True, "-|>"),
        (False, False, "->"),
    ],
)
def test_find_stylename_arrowstyle(double_headed, fill_head, stylename):
    assert _find_stylename_arrowstyle(double_headed, fill_head) == stylename


@pytest.mark.parametrize(
    "inflection_position, rad, expected_stylename, expected_rad",
    [
        (None, 1, "arc3", 1),
        ((0, 0), 1, "angle", 100),
        ((1, 1), 2, "angle", 200),
    ],
)
def test_find_stylename_connectionstyle(
    inflection_position, rad, expected_stylename, expected_rad
):
    stylename, rad_result = _find_stylename_connectionstyle(inflection_position, rad)
    assert stylename == expected_stylename
    assert rad_result == expected_rad

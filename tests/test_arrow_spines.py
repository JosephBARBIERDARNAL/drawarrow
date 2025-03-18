import pytest
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from unittest.mock import patch
from drawarrow import arrow_spines


@pytest.fixture
def mock_ax_arrow():
    """Fixture to mock the ax_arrow function for testing."""
    with patch("drawarrow.arrow_spines.ax_arrow") as mock:
        yield mock


@pytest.fixture
def test_ax():
    """Fixture to create a test axes object."""
    fig, ax = plt.subplots()
    yield ax
    plt.close(fig)


def test_arrow_spines_default_parameters(test_ax, mock_ax_arrow):
    """Test arrow_spines with default parameters."""
    result = arrow_spines(ax=test_ax)
    assert result == test_ax
    for spine in ["top", "bottom", "right", "left"]:
        assert not test_ax.spines[spine].get_visible()

    assert mock_ax_arrow.call_count == 2

    bottom_call = None
    left_call = None
    for call in mock_ax_arrow.call_args_list:
        args = call[0]
        if args[0] == [0 - 0.005, 0]:
            bottom_call = call
        elif args[0] == [0, 0 - 0.005]:
            left_call = call

    assert bottom_call is not None
    assert left_call is not None


def test_arrow_spines_custom_directions(test_ax, mock_ax_arrow):
    """Test arrow_spines with custom arrow directions."""
    result = arrow_spines(
        bottom="toleft", left="tobottom", top="toright", right="totop", ax=test_ax
    )
    assert result == test_ax
    assert mock_ax_arrow.call_count == 4


def test_arrow_spines_none_values(test_ax, mock_ax_arrow):
    """Test arrow_spines with None values to disable specific arrows."""
    result = arrow_spines(bottom=None, left=None, top=None, right=None, ax=test_ax)
    assert result == test_ax
    assert mock_ax_arrow.call_count == 0


def test_arrow_spines_custom_style(test_ax, mock_ax_arrow):
    """Test arrow_spines with custom arrow style parameters."""
    custom_style = {"color": "red", "width": 2, "head_length": 10, "head_width": 5}

    result = arrow_spines(ax=test_ax, **custom_style)
    assert result == test_ax

    for call in mock_ax_arrow.call_args_list:
        kwargs = call[1]
        for key, value in custom_style.items():
            assert kwargs[key] == value


def test_arrow_spines_default_ax(mock_ax_arrow):
    """Test arrow_spines with default ax (gca)."""
    result = arrow_spines()
    assert isinstance(result, Axes)


def test_arrow_spines_invalid_direction_bottom(test_ax):
    """Test arrow_spines with invalid bottom direction."""
    with pytest.raises(ValueError) as excinfo:
        arrow_spines(bottom="invalid_direction", ax=test_ax)

    assert "bottom must be one of: 'toright', 'toleft', None" in str(excinfo.value)


def test_arrow_spines_invalid_direction_left(test_ax):
    """Test arrow_spines with invalid left direction."""
    with pytest.raises(ValueError) as excinfo:
        arrow_spines(left="invalid_direction", ax=test_ax)

    assert "left must be one of: 'totop', 'tobottom', None" in str(excinfo.value)


def test_arrow_spines_invalid_direction_top(test_ax):
    """Test arrow_spines with invalid top direction."""
    with pytest.raises(ValueError) as excinfo:
        arrow_spines(top="invalid_direction", ax=test_ax)

    assert "top must be one of: 'toright', 'toleft', None" in str(excinfo.value)


def test_arrow_spines_invalid_direction_right(test_ax):
    """Test arrow_spines with invalid right direction."""
    with pytest.raises(ValueError) as excinfo:
        arrow_spines(right="invalid_direction", ax=test_ax)

    assert "right must be one of: 'totop', 'tobottom', None" in str(excinfo.value)


def test_arrow_spines_integration(mock_ax_arrow):
    """Test full integration with matplotlib."""
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    result = arrow_spines(ax=ax, color="blue", width=2)
    assert result == ax
    assert mock_ax_arrow.call_count > 0

    plt.close(fig)

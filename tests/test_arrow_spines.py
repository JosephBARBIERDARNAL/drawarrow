import pytest
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from drawarrow import arrow_spines


@pytest.fixture
def test_ax():
    """Fixture to create a test axes object."""
    fig, ax = plt.subplots()
    yield ax
    plt.close(fig)


def test_arrow_spines_default_parameters(test_ax):
    """Test arrow_spines with default parameters."""
    result = arrow_spines(ax=test_ax)
    assert result == test_ax
    for spine in ["top", "bottom", "right", "left"]:
        assert not test_ax.spines[spine].get_visible()


def test_arrow_spines_custom_directions(test_ax):
    """Test arrow_spines with custom arrow directions."""
    result = arrow_spines(
        bottom="toleft", left="tobottom", top="toright", right="totop", ax=test_ax
    )
    assert result == test_ax


def test_arrow_spines_none_values(test_ax):
    """Test arrow_spines with None values to disable specific arrows."""
    result = arrow_spines(bottom=None, left=None, top=None, right=None, ax=test_ax)
    assert result == test_ax


def test_arrow_spines_custom_style(test_ax):
    """Test arrow_spines with custom arrow style parameters."""
    custom_style = {"color": "red", "width": 2, "head_length": 10, "head_width": 5}

    result = arrow_spines(ax=test_ax, **custom_style)
    assert result == test_ax


def test_arrow_spines_default_ax():
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


def test_arrow_spines_integration():
    """Test full integration with matplotlib."""
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    result = arrow_spines(ax=ax, color="blue", width=2)
    assert result == ax

    plt.close(fig)

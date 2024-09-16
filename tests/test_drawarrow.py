import pytest
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
from drawarrow import fig_arrow, ax_arrow
from drawarrow.arrow_patch import _create_arrow


def test_create_arrow():
    tail = (0, 0)
    head = (1, 1)
    arrow = _create_arrow(tail, head)
    assert isinstance(arrow, FancyArrowPatch)


def test_create_arrow_invert_warning():
    tail = (0, 0)
    head = (1, 1)
    with pytest.warns(UserWarning):
        _create_arrow(tail, head, invert=True, radius=0)


def test_create_arrow_linewidth_warning():
    tail = (0, 0)
    head = (1, 1)
    with pytest.warns(UserWarning):
        _create_arrow(tail, head, linewidth=1.2)


def test_fig_arrow():
    fig = plt.figure()
    tail = (0.1, 0.1)
    head = (0.9, 0.9)
    arrow = fig_arrow(tail, head, fig=fig)
    assert isinstance(arrow, FancyArrowPatch)
    assert arrow in fig.patches


def test_fig_arrow_default_figure():
    plt.figure()
    tail = (0.1, 0.1)
    head = (0.9, 0.9)
    arrow = fig_arrow(tail, head)
    assert isinstance(arrow, FancyArrowPatch)
    assert arrow in plt.gcf().patches


def test_ax_arrow():
    fig, ax = plt.subplots()
    tail = (0.1, 0.1)
    head = (0.9, 0.9)
    arrow = ax_arrow(tail, head, ax=ax)
    assert isinstance(arrow, FancyArrowPatch)
    assert arrow in ax.patches


def test_ax_arrow_default_axes():
    plt.figure()
    ax = plt.gca()
    tail = (0.1, 0.1)
    head = (0.9, 0.9)
    arrow = ax_arrow(tail, head)
    assert isinstance(arrow, FancyArrowPatch)
    assert arrow in ax.patches


def test_create_arrow_connection_style():
    tail = (0, 0)
    head = (1, 1)
    arrow = _create_arrow(tail, head, radius=0.2)
    assert arrow.get_connectionstyle().rad == 0.2

    arrow_inverted = _create_arrow(tail, head, radius=0.2, invert=True)
    assert arrow_inverted.get_connectionstyle().rad == -0.2

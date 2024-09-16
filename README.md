# drawarrow

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/drawarrow/image.png?raw=true" alt="drawarrow logo" align="right" width="200px"/>

Drawing arrows for `matplotlib` made easy.

Check out [the online documentation](https://python-graph-gallery.com/drawarrow/).

<br><br>

# Installation

_Note: drawarrow requires **Python 3.9** or above._

You can install `drawarrow` directly from PyPI with:

```
pip install drawarrow
```

<br><br>

# Quick Start

```python
import matplotlib.pyplot as plt
from drawarrow import fig_arrow

fig, ax = plt.subplots()

ax.scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], s=100)

fig_arrow(
    head_position=(0.5, 0.5),
    tail_position=(0.2, 0.7),
    width=2,
    radius=0.3,
    color="darkred",
    fill_head=False,
    mutation_scale=2,
)

plt.show()
```

![](https://github.com/JosephBARBIERDARNAL/drawarrow/blob/main/quick-start.png?raw=true)

<br><br>

# Usage guide

Check out [the online documentation](https://python-graph-gallery.com/drawarrow/).

Features overview:

![](overview.png)

<br><br>

# Contributions

Contributions (and feedback) are welcome.

There's not much that needs to be implemented at the moment. If you've found a bug or want to request a new feature, open an [issue](https://github.com/JosephBARBIERDARNAL/drawarrow/issues).

<br><br><br>

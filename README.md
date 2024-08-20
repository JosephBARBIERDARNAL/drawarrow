# drawarrow

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/drawarrow/image.png?raw=true" alt="drawarrow logo" align="right" width="200px"/>

Drawing arrows for matplotlib made easy.

Check out [the online documentation](https://python-graph-gallery.com/drawarrow/).

<br><br>

# Installation

You can install `drawarrow` directly from PyPI with:

```
pip install drawarrow
```

Alternatively you can install the **development version** with:

```
pip install git+https://github.com/JosephBARBIERDARNAL/drawarrow.git
```

<br><br>

# Quick Start

```python
import matplotlib.pyplot as plt
from drawarrow import fig_arrow

fig, ax = plt.subplots()

ax.scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], s=100)

fig_arrow(head_position=(0.5, 0.5), tail_position=(0.2, 0.7), fig=fig, color="r")

plt.show()
```

![](https://github.com/JosephBARBIERDARNAL/drawarrow/blob/main/quick-start.png?raw=true)

<br><br>

# Usage guide

Check out [the online documentation](https://python-graph-gallery.com/drawarrow/).

<br><br>

# Contributions

Contributions (and feedback) are welcome.

TODO features:

- add a `return_patch: bool` argument to specify whether the code should output the fancyarrowpatch object
- draw arrow with an inflection point (see [this](https://python-graph-gallery.com/web-stacked-area-with-inflexion-arrows/))
- check the [issues](https://github.com/JosephBARBIERDARNAL/drawarrow/issues) for more ideas
- suggest something (:

#### Installation for contributions

_Note: the following steps are for Mac, but not very different in other OS._

- Fork this repo
- `git clone https://github.com/yourusername/drawarrow.git`
- `cd drawarrow`
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install -e .`
- `git checkout -b feature-name`
- start coding!

<br><br><br>

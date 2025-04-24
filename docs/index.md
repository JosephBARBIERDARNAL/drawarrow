# `drawarrow`

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/drawarrow/image.png?raw=true" alt="drawarrow logo" align="right" width="150px"/>

`drawarrow` is a Python package that simplifies (a lot) the process of creating and customising arrows in Matplotlib.

It provides everything you need to create **any** arrow you can imagine:

- double-headed
- curved
- wide or thin
- with an inflection point
- with a shadow
- And so on...

[View examples](https://python-graph-gallery.com/drawarrow/)



<br><br>

## Quick Start

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

![](https://github.com/JosephBARBIERDARNAL/drawarrow/blob/main/img/quick-start.png?raw=true)

<br><br>


## Installation

```
pip install drawarrow
```

<br><br>

## Next steps

You can have a look at this [tutorial](https://python-graph-gallery.com/drawarrow/) or see the [examples](reference/ax_arrow.md).


<br><br>

# fig_arrow

::: drawarrow.main.fig_arrow

<br>

## Examples

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import fig_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

fig_arrow(
    head_position=[0.6, 0.7],
    tail_position=[0.2, 0.2],
    radius=0.3,
    color="red",
    fill_head=False, # don't fill head
    fig=fig,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import fig_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

fig_arrow(
    head_position=[0.6, 0.7],
    tail_position=[0.2, 0.2],
    radius=0.3,
    color="black",
    double_headed=True, # arrow with 2 heads
    fig=fig,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import fig_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

fig_arrow(
    head_position=[0.6, 0.7],
    tail_position=[0.2, 0.2],
    radius=0.9, # bended arrow
    color="blue",
    fig=fig,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import fig_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

fig_arrow(
    head_position=[0.6, 0.7],
    tail_position=[0.2, 0.2],
    head_length=20, # head length
    head_width=10, # head width
    color="#3a46a4",
    fig=fig,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import fig_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

fig_arrow(
    head_position=[0.6, 0.7],
    tail_position=[0.2, 0.2],
    head_length=20, # head length
    head_width=10, # head width
    width=3,
    radius=0.1,
    shadow_style={"offset": (2.5, -4)},
    color="#3aa484",
    fig=fig,
)
```

<br>

[Going further](https://python-graph-gallery.com/drawarrow/)
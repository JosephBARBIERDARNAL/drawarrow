# ax_arrow

::: drawarrow.main.ax_arrow

<br>

## Examples

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import ax_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

ax_arrow(
    head_position=[6, 7],
    tail_position=[1, 1],
    radius=0.3,
    color="red",
    fill_head=False, # don't fill head
    ax=ax,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import ax_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

ax_arrow(
    head_position=[6, 7],
    tail_position=[1, 1],
    radius=0.3,
    color="black",
    double_headed=True, # arrow with 2 heads
    ax=ax,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import ax_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

ax_arrow(
    head_position=[6, 7],
    tail_position=[1, 1],
    radius=0.9, # bended arrow
    color="blue",
    ax=ax,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import ax_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

ax_arrow(
    head_position=[6, 7],
    tail_position=[1, 1],
    head_length=20, # head length
    head_width=10, # head width
    color="#3a46a4",
    ax=ax,
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import ax_arrow

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

ax_arrow(
    head_position=[6, 7],
    tail_position=[1, 1],
    head_length=20, # head length
    head_width=10, # head width
    width=3,
    radius=0.1,
    shadow_style={"offset": (2.5, -4)},
    color="#3aa484",
    ax=ax,
)
```

<br>

[Going further](https://python-graph-gallery.com/drawarrow/)
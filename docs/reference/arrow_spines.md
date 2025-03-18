# arrow_spines

::: drawarrow.arrow_spines.arrow_spines

<br>

## Examples

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import arrow_spines

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

arrow_spines(ax=ax, color="red")
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import arrow_spines

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

arrow_spines(
   right="totop",
   bottom="toleft",
   left=None, # remove left spine
   ax=ax,
   color="red",
)
```

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import arrow_spines

fig, ax = plt.subplots()

ax.scatter([1, 2, 3, 8, 6, 10], [2, 5, 3, 9, 2, 10])

arrow_spines(
   ax=ax,
   color="#7b2e8e", # purple
   width=3,
   head_length=15,
   head_width=10,
)

ax.tick_params(size=0, pad=15) # remove ticks and add padding
```

<br>

[Going further](https://python-graph-gallery.com/drawarrow/)
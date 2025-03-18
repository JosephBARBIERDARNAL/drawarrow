# ax_arrow

::: drawarrow.main.ax_arrow

<br>

## Examples

```python
# mkdocs: render
import matplotlib.pyplot as plt
from drawarrow import ax_arrow

fig, ax = plt.subplots()

ax_arrow(
    head_position=[0.1, 0.7],
    tail_position=[0.1, 0.5],
    radius=0.3,
    color="red",
    fill_head=False,
    ax=ax,
)
```

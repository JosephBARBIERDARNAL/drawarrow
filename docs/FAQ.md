# Frequently Asked Questions

<br>

### Why a package just to make arrows?

Matplotlib has many built-in features for creating arrows. But there are too many: did you know that there are 5 different ways of making an arrow in Matplotlib!

- `ax.arrow()`
- `ax.annotate()`
- `patches.Arrow()`
- `patches.FancyArrow()`
- `patches.FancyArrowPatch()`

All these functions behave differently and have their own features.

The problem is that you have to change functions when you want to style your arrow differently, which makes customising an arrow quite difficult.

Also, to create an arrow with an inflection point in matplotlib, you have to specify the angles of the inflection, which makes it almost impossible to guess where the inflection point will be.

`drawarrow` is simply a wrapper around these functions. It makes more sense (at least to me) to have 1 (actually 2, but with a lot in common) function with clear and explicit arguments that behaves simply.

- Want to bend your arrow? Just use the `radius` argument?
- Want an empty arrowhead? Use `fill_head=False`.
- Want an arrow with 2 heads? Set `double_headed=True`.
- And so on...

With `drawarrow`, you can create virtually any arrow you want with a single function.

<br>

### What's the difference between `ax_arrow` and `fig_arrow`?

`ax_arrow` and `fig_arrow` are 99% identical: the only difference lies in the coordinate systems they use.

- With `fig_arrow`, the position of the arrow is relative to the Figure (from 0 to 1).
- With `ax_arrow`, the position of the arrow is relative to your data (if your x-axis goes from 1 to 50 and you want an arrow in the middle, place it around 25 on the x-axis).

The reason `drawarrow` does this is to follow a pattern in matplotlib. For example, matplotlib does the same thing with `fig.text()` and `ax.text()`. The [highlight_text](https://github.com/znstrider/highlight_text) package does the same.

It is more flexible if you want an arrow in a specific place, or if you want to add it automatically (e.g. in a for loop) without too much trial and error.

<br>

### Are there many dependencies?

`drawarrow` only relies on Matplotlib.

<br>

### Other

Having another question? Feel free to [open an issue](https://github.com/JosephBARBIERDARNAL/drawarrow/issues).

<br><br><br>

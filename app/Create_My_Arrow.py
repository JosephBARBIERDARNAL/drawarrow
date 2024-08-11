import streamlit as st
from ui import st_footer, st_header, st_spacing
from drawarrow import fig_arrow, ax_arrow
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 200

st_header()
st_spacing(3)

st.markdown("Create and preview your dream arrow!")

col1, col2, col3, col4 = st.columns(4)
x_tail = col1.slider("x tail position", min_value=-0.4, max_value=1.4, value=0.3)
y_tail = col2.slider("y tail position", min_value=-0.4, max_value=1.4, value=0.3)
x_head = col3.slider("x head position", min_value=-0.4, max_value=1.4, value=0.7)
y_head = col4.slider("y head position", min_value=-0.4, max_value=1.4, value=0.7)

col1, col2, col3 = st.columns(3)
head_length = col1.slider("Head length", min_value=1, max_value=100, value=25)
head_width = col2.slider("Head width", min_value=1, max_value=100, value=20)
tail_width = col3.slider("Tail width", min_value=1, max_value=50, value=5)

col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
facecolor = col1.color_picker("Arrow facecolor", value="#a83246")
edgecolor = col2.color_picker("Arrow edgecolor", value="#a83246")
alpha = col4.slider(
    "Opacity (alpha)", min_value=0.0, max_value=1.0, value=1.0, step=0.1
)
available_hatchs = [None, "/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"]
hatch = col3.selectbox("Pattern to fill the arrow", options=available_hatchs, index=0)
if hatch != available_hatchs[0]:
    hatch_display = "'" + hatch + "'"
else:
    hatch_display = hatch

col1, col2 = st.columns(2)
linewidth = col1.slider("Linewidth", min_value=0.1, max_value=5.0, value=1.0)
radius = col2.slider("Radius", min_value=-3.0, max_value=3.0, value=0.2)

if st.toggle("Auto update chart", value=True):

    fig, ax = plt.subplots(figsize=(8, 8))
    fig_arrow(
        tail_position=(x_tail, y_tail),
        head_position=(x_head, y_head),
        head_length=head_length,
        head_width=head_width,
        tail_width=tail_width,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        radius=radius,
        alpha=alpha,
        hatch=hatch,
    )
    st.pyplot(fig)

st_spacing(5)
st.markdown("## Get the code")
st.markdown(
    f"""
   ```python
   from drawarrow import fig_arrow
   import matplotlib.pyplot as plt

   fig, ax = plt.subplots(figsize=(8, 8))
   fig_arrow(
       tail_position=({x_tail}, {y_tail}),
       head_position=({x_head}, {y_head}),
       head_length={head_length},
       head_width={head_width},
       tail_width={tail_width},
       facecolor={facecolor},
       edgecolor={edgecolor},
       linewidth={linewidth},
       radius={radius},
       alpha={alpha},
       hatch={hatch_display},
   )
   plt.show()
   ```
   """
)


st_spacing(5)
st_footer()

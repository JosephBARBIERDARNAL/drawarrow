import streamlit as st


def st_header():
    st.html(
        f"""
      <center><h1>DrawArrow</h1></center>
      <center><h3>Drawing arrows for matplotlib made easy</h3></center>
      """
    )


def st_footer():
    st.html(
        f"""
      <center><a href='https://github.com/JosephBARBIERDARNAL/drawarrow'>Github</a> (give it a star ⭐)</center>
      <center>DrawArrow, by <a href='https://barbierjoseph.com/'>Joseph Barbier</a></center>
      """
    )


def st_spacing(n: int):
    for _ in range(n):
        st.text("")

import streamlit as st

st.title("CSS Shape Generator")
bgcolor = st.color_picker("Pick a Background color")
border_color = st.color_picker("Pick a Border Color", "#654FEF")
height = st.sidebar.slider("Height Size", 50, 200, 50)
width = st.sidebar.slider("Width Size", 50, 200, 50)
top_left_border = st.sidebar.number_input("Top Left Border", 10, 50, 10)
top_right_border = st.sidebar.number_input("Top Right Border", 10, 50, 10)
bottom_left_border = st.sidebar.number_input("Bottom Left Border", 10, 50, 10)
bottom_right_border = st.sidebar.number_input("Bottom Right Border", 10, 50, 10)
border_style = st.selectbox(
    "Border Style",
    [
        "dotted",
        "dashed",
        "solid",
        "double",
        "groove",
        "ridge",
        "inset",
        "outset",
        "none",
        "hidden",
    ],
)

html_design = """
<div style="height:{}px;width:{}px;background-color:{};border-radius:{}px {}px {}px {}px;border-style:{};border-color:{}">
</div>
"""
st.markdown(
    html_design.format(
        height,
        width,
        bgcolor,
        top_left_border,
        top_right_border,
        bottom_left_border,
        bottom_right_border,
        border_style,
        border_color,
    ),
    unsafe_allow_html=True,
)
st.subheader("Result")
result_of_design = html_design.format(
    height,
    width,
    bgcolor,
    top_left_border,
    top_right_border,
    bottom_left_border,
    bottom_right_border,
    border_style,
    border_color,
)
st.code(result_of_design)

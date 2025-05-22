import streamlit as st
import pandas as pd

with st.sidebar:
    name = st.text_input("你是?")
    if name:
        st.write(name)

l1, l2 = st.columns([2,1])


with l1:
    "shabi"
with l2:
    ("xialiangyu")

st.divider()


if "aa" not in st.session_state:
    st.session_state.aa = 0
click = st.button("加1")

if click:
    st.session_state.aa += 1
st.write(st.session_state.aa)

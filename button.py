import streamlit as st
st.title("Interactive steamlit app")
mame = st.text_input("enter your name : ")
if st.bottom("submit"):
    st.write(f"Hello,{name}!Welcome to Streamlit.")

import streamlit as st
st.title("Interactive steamlit app")
name = st.text_input("enter your name : ")
if st.button("submit"):
    st.write(f"Hello,{name}!Welcome to Streamlit.")



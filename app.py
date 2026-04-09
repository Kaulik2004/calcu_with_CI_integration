import streamlit as st

st.title("Power Calculator")
st.write("Enter the base ")

n=st.number_input("Base", value=1, step=1)

#calculate results
sq=n**2
cube=n**3
five=n**5

st.write(f"{n} squared is {sq}")
st.write(f"{n} cubed is {cube}")
st.write(f"{n} to the power of 5 is {five}")
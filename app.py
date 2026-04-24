import streamlit as st

# Streamlit doesn't use @app.route or app.run()
st.set_page_config(page_title="My New Site")

st.title("Welcome to my Website")
st.write("This is running on Streamlit Cloud!")

if st.button("Say Hello"):
    st.balloons()
    st.success("Hello there!")

import streamlit as st 
from PIL import Image
st.set_page_config(
    page_title="Recognition",
    page_icon="👁️‍🗨️"
)

st.subheader("Please take a snapshot and we'll recognize who it is.")

st.sidebar.success("Recognition")

st.divider()

image = st.camera_input("smile")

if 'pic' not in st.session_state:
    st.session_state.pic = []

if image is not None:
    st.session_state.pic = Image.open(image)

#image to run on model:
image_for_recognition = image


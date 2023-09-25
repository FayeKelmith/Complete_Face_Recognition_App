import streamlit as st 

st.set_page_config(
    page_title="Recognition",
    page_icon="👁️‍🗨️"
)

st.title("Please take a snapshot and we'll recognize who it is.")

st.sidebar.success("Recognition")

st.session_state.key = st.camera_input('pic',key='pic')

if 'key' in st.session_state:
    st.write(st.session_state.pic)
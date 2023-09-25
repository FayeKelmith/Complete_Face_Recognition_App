import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Load",
    page_icon="🔂"
)

st.header("Add a new face")
st.sidebar.success("Load your images")

st.info("Who do you wish to add to the dataset?")

name = st.text_input("Name: ",key='name')

if name:
    st.write("Alright, let us Get ",name," aboard!")

st.divider()

#This section is to add the picture.

st.subheader("Please add 20 photos of thesame person, with different perspectives.")


#==========================
#    PICTURES
#==========================

#FIXME: to modify number_of_images to 20
number_of_images  = 5 


# Initializing session to store images
if 'gallery' not in st.session_state:
    st.session_state.gallery = []

#FIXME: Attempt to remove image from screen when picture is clicked
if 'visible' not in st.session_state:
    st.session_state.visible = "disabled"
    
while(len(st.session_state.gallery) < number_of_images):
    value = "pic" + str(len(st.session_state.gallery)+1)
    image = st.camera_input('Smile',key=value)
    
    if image:
        st.session_state.gallery.append(image)

st.write(st.session_state.gallery)

    
        
    
    
    




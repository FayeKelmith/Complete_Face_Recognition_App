import streamlit as st
import numpy as np
from PIL import Image
import os

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

number_of_images  = 20 


# Initializing session to store images
if 'gallery' not in st.session_state:
    st.session_state.gallery = []

#Initializing session to end data collection when need arises

if 'stop' not in st.session_state:
    st.session_state.stop = False
# while(len(st.session_state.gallery) < number_of_images):

def stop_recording():
    st.session_state.stop = True
    
while( (not st.session_state.stop) and (len(st.session_state.gallery) < number_of_images)):
     
     
    image = st.camera_input('Smile',key= f"pic_{ str(len(st.session_state.gallery)+1) }" )
    
    if image is not None:
        #To end data collection
        st.button("Stop", on_click=stop_recording)
        #converting to PIL image
        pic = Image.open(image)
        
        #final_pic = np.array(pic)
        
        st.session_state.gallery.append(pic)


#incase the limit is attained, it should default to true.
st.session_state.stop = True 

st.info(f"{len(st.session_state.gallery)} Pictures Taken!")
#Get the pictures and upload send them to data set
image_gallery = st.session_state.gallery
  
done = st.session_state.stop

#=========FOLDER CREATION======
if done:
    #make new path
    dataset = "../../dataset"
   
    new_path = os.path.join(dataset,name)
    
    #FIXME:
    os.makedirs(new_path)
    
    #navigate to the new path
    os.chdir(new_path)
    
        #populate the new directory with images
    for ind in range(len(image_gallery)):
        image_gallery[ind].save(fp=f'{name}_{ind}.jpg',format='JPEG')









#NOTE: To display the taken picture.
# for image in image_gallery:
#     st.image(image,caption="Pic")


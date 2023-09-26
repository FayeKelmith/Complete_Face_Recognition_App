from fastapi import FastAPI 
from PIL import Image
import os



app = FastAPI()

@app.get("/")
async def root():
    #NOTE: this is a temporary folder to represent images that would otherwise be imported from interface
    
    path = "./temp"
    
    #FIXME:  To import name from interface
    name = "faye"
    
    #FIXME: To import gallery from interface
    gallery = []
    
    # images = os.listdir(path=path)
    # images = [img.lower() for img in images]
  
    # try:
    #     for image in images:
    #         link = f'{path}/{image}'
    #         img = Image.open(link)
    #         gallery.append(img)
            
    #     #where we have to make a new directory
    #     dataset = "../dataset"
    #     #creating the new path with the name 
    #     new_path = os.path.join(dataset,name)
    
    #     #making the new directory
    #     os.mkdir(new_path)  
        
    #     os.chdir(new_path)
    #     for idx in range(len(gallery)):
    #         gallery[idx].save(fp=f'kelm_{idx}.jpg',format='JPEG')
    # except:
    #     #os.rmdir(new_path)
    #     pass
    
    
    
    return {"message": "works"}
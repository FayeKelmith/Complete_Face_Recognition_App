from fastapi import FastAPI 
from PIL import Image



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}
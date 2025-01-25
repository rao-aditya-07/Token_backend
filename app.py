from fastapi import FastAPI, File, UploadFile
from fastapi.responses import PlainTextResponse
import shutil
import os

# Create an instance of the FastAPI class
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/upload")
async def handle_upload(file: UploadFile = File(...)):
    # Define the local path where the file will be saved
    file_location = f"./uploads/{file.filename}"
    
    # Create the uploads directory if it doesn't exist
    import os
    os.makedirs(os.path.dirname(file_location), exist_ok=True)

    # Save the uploaded file locally
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"File {file.filename} uploaded successfully!", "file_location": file_location}

@app.get("/display_file")
async def display_file():
    file_path = f"./uploads/taylorswift.txt"

    # Check if the file exists
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    # Read the contents of the file
    with open(file_path, "r") as file:
        file_content = file.read()

    # Return the file content as a plain text response
    return PlainTextResponse(content=file_content)
from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    """
    Description:

    .
    """
    #load data from json file 
    with open("patient.json" , "r") as f:
        data = json.load(f)

    return data 


@app.get("/")
def hello():
    """
    Description:

    .
    """
    return {"message": "Patient Managment System API!"}

@app.get("/about")
def about():
    """
    Description:

    .
    """
    return {"message": "This is a simple API for managing patient records."}

#view 
@app.get("/view")
def view_data():
    """
    Description:

    .
    """
    data = load_data()
    return data
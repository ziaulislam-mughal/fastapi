from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    #load data from json file 
    with open("patient.json" , "r") as f:
        data = json.load(f)

    return data 


@app.get("/")
def hello():
    return {"message": "Patient Managment System API!"}

@app.get("/about")
def about():
    return {"message": "This is a simple API for managing patient records."}

#view 
@app.get("/view")
def view_data():
    data = load_data()
    return data

#view specific patient data 
@app.get('/patient/{patient_id}')
def view_patient_id(patient_id: str):
    data = load_data()
    patient = next(
        (p for p in data if p["patient_id"] == patient_id),
        None
    )
    if patient:
        return patient
    return {"error": "Patient not found."}
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import pickle
import pandas as pd

tags = [
    {
        'name': 'Maths',
        'description': 'Operations related to mathematical calculations'
    },
    {
        'name': 'Models',
        'description': 'Operations related to models'
    }
]

app = FastAPI(
    title="My First FastAPI",
    description="This is my first FastAPI",
    version="0.0.1",
    openapi_tags=tags,
)


class Data(BaseModel):
    name: str='Mathis'
    city: str='Lyon'


@app.get("/", tags=['Model'])
def default_root():
    return "Hello World"

@app.get("/square", tags=['Maths'])
def square(n:int=1) -> int:
    return n*n

@app.post('/formulaire')
def formulaire(data:Data):

    data = dict(data)

    # Name
    name = data['name']

    # City
    city = data['city']

    return {'message': 'Formulaire envoyé'}

@app.post('/upload')
def upload_file(file: UploadFile=File(...)):
    return file.filename

# 0 charger modèle 
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

class Data_predict(BaseModel):
    Gender: str
    Age: int
    Graduated: str
    Profession: str
    Work_Experience: int
    Spending_Score: str
    Family_Size: int
    Segmentation: str

# 1 créer endpoint
@app.post('/predict', tags=["Model"])
def predict(data: Data_predict):
    data = dict(data)

    # Prédictions
    prediction = model.predict(pd.DataFrame([data]))

    return int(prediction)

@app.post('/predict_file', tags=["Model"])
def predict_file(file: UploadFile=File(...)):
    df = pd.read_csv(file.file)

    if 'Gender' not in df.columns or 'Gratuated' not in df.columns:
        return False
    else :
        X = df.drop(["Ever_Married"], axis=1).dropna()
        predictions = model.predict(X)
        return [int(n) for n in predictions]

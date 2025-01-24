from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

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
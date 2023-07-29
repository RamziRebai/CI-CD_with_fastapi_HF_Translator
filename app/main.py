from fastapi import FastAPI, Response
import uvicorn
from pydantic import BaseModel

from transformers import pipeline

app= FastAPI(title="Deployment of HuggingFace Translator EN to DE")

class Phrase(BaseModel):
    text: str
translate= pipeline('translation', model='Helsinki-NLP/opus-mt-en-de')

@app.on_event("startup")
def load_model():
    global translate
    translate= pipeline('translation', model='Helsinki-NLP/opus-mt-en-de')

@app.get("/")
def home():
    return Response ("Everything is going well! Please head over http://localhost:8088/docs")

@app.post("/translate")
def translate(phrase: Phrase):
    result= translate(phrase.text)
    return result[0]

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port="8088")

from fastapi import FastAPI, Response
import uvicorn
from pydantic import BaseModel


from transformers import FSMTForConditionalGeneration, FSMTTokenizer

app= FastAPI(title="Deployment of HuggingFace Translator EN to DE")

class Phrase(BaseModel):
    text: str

@app.get("/")
def home():
    return Response ("Everything is going well, please head over http://localhost:80/docs")

@app.post("/predict")
def predict(phrase: Phrase):
    mname = "facebook/wmt19-en-de"
    tokenizer = FSMTTokenizer.from_pretrained(mname)
    model = FSMTForConditionalGeneration.from_pretrained(mname)

    input_ids = tokenizer.encode(phrase.text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port="8080")

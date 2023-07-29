from app.main import translate
from pydantic import BaseModel

class Phrase(BaseModel):
    text: str

def test_func():
    phrase = Phrase(text="Machine learning is great, isn't it?")
    result = translate(phrase.text)
    assert isinstance(result, str)

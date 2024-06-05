from translate import Translator
from flask import Flask, request

app = Flask(__name__)

def translate_to_spanish(text):
    translator = Translator(from_lang='pt', to_lang='es')
    translation = translator.translate(text)
    return translation

def translate_to_portuguese(text):
    translator = Translator(from_lang='es', to_lang='pt')
    translation = translator.translate(text)
    return translation


@app.post("/portuguese")
def translate_pt():
    text = request.json['text']
    translation = translate_to_portuguese(text)
    return {"translation": translation}

@app.post("/spanish")
def translate_es():
    text = request.json['text']
    translation = translate_to_spanish(text)
    return {"translation": translation}










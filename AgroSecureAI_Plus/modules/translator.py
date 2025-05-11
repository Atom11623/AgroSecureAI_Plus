from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    return detect(text)

def translate_to_english(text):
    return GoogleTranslator(source='auto', target='en').translate(text)

def translate_to_hausa(text):
    return GoogleTranslator(source='auto', target='ha').translate(text)


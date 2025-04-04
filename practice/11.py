from googletrans import Translator

translator = Translator()

text = input("Enter text: ")
language = input("Enter source language code (e.g., 'en' for English): ")
translate_to = input("Enter target language code (e.g., 'es' for Spanish): ")

try:
    translated = translator.translate(text, src=language, dest=translate_to)
    print(f"Translated text: {translated.text}")
except Exception as e:
    print(f"An error occurred: {e}")
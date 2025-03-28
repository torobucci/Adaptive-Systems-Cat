from translate import Translator

def translate_text(text, target_lang):
    """Translates text between English and Swahili."""
    if target_lang not in ['sw', 'en']:
        raise ValueError("Supported languages: 'sw' (Swahili), 'en' (English)")
    
    translator = Translator(to_lang=target_lang)
    translation = translator.translate(text)
    return translation

# Testing the translation
examples = [
    ("Hello, how are you?", "sw"),  # English to Swahili
    ("Habari, hujambo?", "en")      # Swahili to English
]

for text, lang in examples:
    translated_text = translate_text(text, lang)
    print(f"Original: {text} | Translated ({lang}): {translated_text}")

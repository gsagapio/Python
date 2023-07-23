from translate import Translator

print('Hello World for everyone!')
def translate_text(text, target_languages):
    translations = {}

    for target_language in target_languages:
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        translations[target_language] = translation

    return translations

# Idiomas alvo desejados
target_languages = ["en", "ja", "zh", "ru", "fr", "es", "pt"]

# Texto a ser traduzido
text = "Hello World! I'm a programming student excited about the tools and technologies in this field. I really want to evolve in this profession, learn and perfect myself. And to do that, I know that good communication with my fellow programmers will be of great help! So here's my 'Hello World' for some of the most popular languages!"

# Uso da função de tradução
translations = translate_text(text, target_languages)

# Exibindo as traduções
for lang, translation in translations.items():
    print(f"{lang}: {translation}")

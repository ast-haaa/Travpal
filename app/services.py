from deep_translator import GoogleTranslator
import openai

# OpenAI API Key (Replace with your actual key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Translator Service
def get_supported_languages():
    return GoogleTranslator().get_supported_languages()

def translate_text(text, target_lang="en"):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

# Chatbot Service
def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

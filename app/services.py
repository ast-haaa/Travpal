from deep_translator import GoogleTranslator
import openai

# OpenAI API Key (Replace with your actual key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Get Supported Languages
def get_supported_languages():
    return GoogleTranslator().get_supported_languages()

# Translate Text
def translate_text(text, target_lang="en"):
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Error during translation: {str(e)}"

# Chatbot Service
def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

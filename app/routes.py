from flask import Blueprint, request, jsonify
from app.services import translate_text, get_supported_languages, chatbot_response

translator_bp = Blueprint("translator", __name__)

# Translator API
@translator_bp.route('/supported-languages', methods=['GET'])
def get_languages():
    return jsonify({"languages": get_supported_languages()})

@translator_bp.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    translated_text = translate_text(text, target_lang)
    return jsonify({"translated_text": translated_text})

# Chatbot API
@translator_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    target_lang = data.get("lang", "en")  # Default to English if no language is specified

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Step 1: Translate the user's message to English if needed
    translated_message = translate_text(user_message, "en" if target_lang != "en" else target_lang)

    # Step 2: Get the chatbot's response in English
    bot_response = chatbot_response(translated_message)

    # Step 3: If the target language is not English, translate the bot's response
    if target_lang != "en":
        bot_response = translate_text(bot_response, target_lang)

    return jsonify({"response": bot_response})

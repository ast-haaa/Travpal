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

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    bot_response = chatbot_response(user_message)
    return jsonify({"response": bot_response})

import os

from flask import Flask, jsonify, render_template, request
from googletrans import Translator
import google.generativeai as genai

app = Flask(__name__)
translator = Translator()


def get_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask_gemini():
    data = request.get_json(silent=True) or {}
    question = str(data.get("question", "")).strip()
    lang_code = str(data.get("lang", "en")).strip() or "en"

    if not question:
        return jsonify({"error": "question is required"}), 400

    try:
        response = get_model().generate_content(question)
        answer = (response.text or "").strip()
        translated = translator.translate(answer, src="en", dest=lang_code).text
        return jsonify({"answer": translated})
    except RuntimeError as error:
        return jsonify({"error": str(error)}), 503
    except Exception:
        app.logger.exception("The assistant request failed")
        return jsonify({"error": "The assistant request failed"}), 502


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0") == "1",
    )

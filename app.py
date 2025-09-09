from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyCtO-IMk2xMXBT9-eROp-HLnaNzTJ8oPuc")  # Replace with your Gemini key

# Initialize Translator
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_gemini():
    data = request.json
    question = data.get('question')
    lang_code = data.get('lang')

    try:
        # Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question)
        answer_english = response.text.strip()

        # Translate response
        translation = translator.translate(answer_english, src='en', dest=lang_code)
        translated_response = translation.text

        return jsonify({
            'answer': translated_response
        })

    except Exception as e:
        print("❌ Error in /ask:", e)
        return jsonify({
            'answer': f"Error: {str(e)}"
        })

if __name__ == '__main__':
    app.run(debug=True)

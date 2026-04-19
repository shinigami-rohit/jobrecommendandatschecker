from flask import Flask, request, jsonify
import PyPDF2

app = Flask(__name__)

def extract_text(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.route('/recommend', methods=['POST'])
def recommend():
    file = request.files['resume']
    text = extract_text(file)

    # TEMP response (to test route first)
    return jsonify({
        "message": "API working",
        "text_length": len(text)
    })

@app.route('/')
def home():
    return "ATS Checker running successfully"

if __name__ == '__main__':
    app.run()

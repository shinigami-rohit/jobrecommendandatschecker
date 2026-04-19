from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return "ATS Checker running successfully 🚀"

@app.route("/ats", methods=["POST"])
def ats_score():
    data = request.get_json()

    resume = data.get("resume", "")
    job = data.get("job", "")

    resume_words = set(resume.lower().split())
    job_words = set(job.lower().split())

    match = resume_words.intersection(job_words)
    score = (len(match) / len(job_words)) * 100 if job_words else 0

    return jsonify({
        "score": round(score, 2),
        "matched_words": list(match)
    })
@app.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files.get("resume")

    if not file:
        return {"error": "No file uploaded"}, 400

    return {"message": "File received successfully"}
    import PyPDF2

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    try:
        file = request.files.get("resume")
        job = request.form.get("job", "")

        if not file:
            return {"error": "No file uploaded"}, 400

        if not job:
            return {"error": "Job description missing"}, 400

        reader = PyPDF2.PdfReader(file)
        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:   # prevents crash
                resume_text += text

        if not resume_text:
            return {"error": "Could not extract text from PDF"}, 400

        resume_words = set(resume_text.lower().split())
        job_words = set(job.lower().split())

        if not job_words:
            return {"error": "Invalid job description"}, 400

        match = resume_words.intersection(job_words)
        score = (len(match) / len(job_words)) * 100

        return jsonify({
            "score": round(score, 2),
            "matched_words": list(match)
        })

    except Exception as e:
        return {"error": str(e)}, 500
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

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
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

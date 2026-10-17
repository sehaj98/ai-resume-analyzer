from flask import Flask, render_template, request
from analyzer import extract_text_from_pdf, analyze_resume
from pathlib import Path
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = Path("uploads")
ALLOWED_EXTENSIONS = {"pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024

app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

UPLOAD_FOLDER.mkdir(exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        resume = request.files.get("resume")
        job_description = request.form.get(
            "job_description", ""
        ).strip()

        if not resume or not resume.filename:
            error = "Please upload your resume PDF."
        elif not allowed_file(resume.filename):
            error = "Only PDF resumes are supported."
        elif not job_description:
            error = "Please enter the job description."
        else:
            filename = secure_filename(resume.filename)

            if not filename:
                error = "Please use a valid PDF filename."
            else:
                file_path = UPLOAD_FOLDER / filename

                try:
                    resume.save(file_path)

                    resume_text = extract_text_from_pdf(file_path)

                    if not resume_text:
                        error = (
                            "No readable text found. "
                            "Please upload a text-based PDF resume."
                        )
                    else:
                        result = analyze_resume(
                            resume_text, job_description
                        )

                except Exception:
                    error = (
                        "Unable to read this PDF. "
                        "Please try another valid PDF resume."
                    )
                finally:
                    if file_path.exists():
                        file_path.unlink()

    return render_template(
        "index.html",
        result=result,
        error=error,
    )


@app.errorhandler(413)
def file_too_large(error):
    return (
        "File too large. Please upload a PDF smaller than 5 MB.",
        413,
    )


if __name__ == "__main__":
    app.run(debug=True)
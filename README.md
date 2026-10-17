# AI Resume Analyzer

A Python Flask web application that analyzes a PDF resume and compares its skills with a target job description. It calculates a skill match percentage and displays matching and missing skills.

## Features

- Upload resumes in PDF format
- Extract text from PDF files
- Automatically detect supported skills
- Compare resume skills with job requirements
- Calculate a skill match percentage
- Display matching and missing skills
- Visual progress bar for the match score
- Validate uploaded files and limit file size
- Automated testing with pytest

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- pypdf
- pytest

## Project Structure

```text
ai-resume-analyzer/
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
└── tests/
    └── test_analyzer.py
```

## Getting Started

### 1. Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username after uploading the project.

```bash
git clone https://github.com/YOUR-USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5000

## How to Use

1. Open the AI Resume Analyzer in your browser.
2. Upload a text-based PDF resume.
3. Paste the target job description.
4. Click **Analyze Resume**.
5. Review the match percentage, detected skills, matching skills, and missing skills.

## Run Automated Tests

Run the following command from the project directory:

```bash
python -m pytest -v
```

The tests check skill extraction, resume analysis, and empty job descriptions.

## How It Works

The application extracts text from the uploaded PDF using `pypdf`. It identifies skills from a predefined skills list in both the resume and job description. It then compares the detected skills and calculates the percentage of required skills found in the resume.

## Limitations

- The analyzer only recognizes skills included in its predefined list.
- The match percentage is based on detected skills, not a complete assessment of qualifications.
- Scanned PDFs without extractable text may not work.
- The score does not guarantee job suitability or hiring success.

## Future Improvements

- Expand the supported skills database.
- Add resume improvement suggestions.
- Improve the results dashboard.
- Add more automated tests.
- Introduce more advanced resume and job-description matching.

## Author

Built as a Python portfolio project.

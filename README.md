# 🩺 AI Medical Report Analyzer

AI Medical Report Analyzer is an intelligent Natural Language Processing (NLP) based healthcare application that analyzes uploaded medical reports and automatically extracts important patient information along with generating a concise AI summary.

The system is built using **FastAPI, Python, Regular Expressions, Pandas, and HTML frontend** to simulate an AI-assisted clinical report understanding tool.

---

## 🚀 Features

- Upload patient medical report files
- Automatically extract important medical entities such as:
  - Age
  - Gender
  - Diseases/Conditions
  - Medications
- Generate AI-based concise medical report summary
- REST API powered by FastAPI
- Cross-Origin enabled frontend-backend integration
- Lightweight and fast medical text analysis

---

## 🧠 Technologies Used

- Python
- FastAPI
- Uvicorn
- Pandas
- Regex (NLP Entity Extraction)
- HTML
- JavaScript
- CSS

---

## 📁 Project Structure

```bash
AI-MEDICAL-ANAIYZER/
│
├── app.py                # FastAPI backend server
├── requirements.txt      # Required dependencies
│
├── data/
│   ├── mtsamples.csv
│   └── sample_report.txt
│
└── frontend/
    └── index.html        # User interface
⚙️ Installation Guide
1 Clone the Repository
git clone https://github.com/your-username/AI-MEDICAL-ANAIYZER.git
cd AI-MEDICAL-ANAIYZER
2 Install Dependencies
pip install -r requirements.txt
3 Run the FastAPI Server
uvicorn app:app --reload
🌐 Open in Browser

After server starts, open:

http://127.0.0.1:8000

FastAPI root status endpoint will show:

{"status":"AI Medical Report Analyzer is running"}
📡 API Endpoint for Medical Report Analysis
POST /analyze

Upload a medical text file and get:

Extracted entities
AI generated summary
Original report word count
🔍 Core Functionalities Implemented
✅ Medical Entity Extraction

Using Regular Expressions, the system identifies:

Patient Age
Patient Gender
Existing Medical Conditions
Mentioned Medicines
✅ AI Report Summarization

Important clinical sentences are ranked based on medical keywords such as:

diagnosis
treatment
blood pressure
sugar
medication
infection
symptoms

Top scored sentences are selected to generate an automatic summary.

🎯 Objective of the Project

This project demonstrates how Artificial Intelligence and Natural Language Processing can assist in understanding unstructured medical reports and generating quick patient insights automatically.

It serves as an academic mini project for AI in healthcare applications.

⚠️ Disclaimer

This tool is developed only for educational and demonstration purposes.
It is not intended for real medical diagnosis or professional healthcare decisions.

👩‍💻 Author

Developed by Kreetika Kishore

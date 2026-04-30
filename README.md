# 🩺 AI Medical Report Analyzer

> An intelligent FastAPI-based healthcare text analysis system that extracts important patient medical entities and generates an AI-based summary from uploaded medical reports.

## 1. Project Overview

AI Medical Report Analyzer is a mini healthcare intelligence application designed to process unstructured patient medical text reports and automatically identify useful clinical information.

The uploaded report is analyzed using Python-based Natural Language Processing logic, where:

- patient details are extracted,
- disease names are identified,
- medication mentions are detected,
- and an AI-generated concise medical summary is produced.

This project demonstrates the practical use of Artificial Intelligence in healthcare documentation analysis.
## 2. Key Features

✅ Upload patient medical text report file  
✅ Automatic extraction of:
- Age
- Gender
- Medical Conditions
- Prescribed Medications

✅ AI-based summary generation  
✅ FastAPI REST API backend  
✅ Frontend medical dashboard  
✅ Word count calculation of original report  
✅ Cross-Origin enabled browser communication

---

## 3. Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming |
| FastAPI | Backend API framework |
| Uvicorn | ASGI server |
| Regex | Medical entity extraction |
| Pandas | Data handling |
| HTML/CSS/JS | Frontend development |
| Python Multipart | File upload handling |

---
4. Folder Structure
   AI-MEDICAL-ANAIYZER/
│
├── app.py                  # Main FastAPI backend server
├── requirements.txt        # Required dependencies
├── README.md               # Project documentation
│
├── data/
│   ├── mtsamples.csv
│   └── sample_report.txt
│
└── frontend/
    └── index.html          # Frontend medical dashboard

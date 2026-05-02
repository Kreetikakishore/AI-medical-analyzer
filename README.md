# 🏥 AI Medical Report Analyzer

> A lightweight, full-stack web application that analyzes plain-text medical reports and returns a patient-friendly summary along with extracted medical entities — powered by the Claude AI API and a FastAPI backend.

---

## 📸 Demo

**Input — Upload Medical Report:**

![Input](https://raw.githubusercontent.com/Kreetikakishore/ai-medical-analyzer/main/assets/input.png)

**Output — Analysis Result:**

![Output](https://raw.githubusercontent.com/Kreetikakishore/ai-medical-analyzer/main/assets/output.png)

---

## ✨ Features

- 📄 Upload any `.txt` medical report
- 🔍 Extracts key entities: age, gender, conditions, and medications
- 🧠 Generates a patient-friendly AI summary using Claude API
- ⚠️ Includes a medical disclaimer on every result
- 📊 Displays word count and total entities found
- 🎨 Clean, minimal frontend — no frameworks required

---

## 📌 Executive Summary

Medical reports are often written in complex clinical language that patients struggle to understand. This project bridges that gap by building an AI-powered medical report analyzer that:

- Extracts structured medical entities from unstructured text
- Generates plain-language summaries using Claude AI
- Delivers results through a clean, accessible web interface
- Runs entirely locally with no database or cloud dependency

---

## 🧠 How It Works

1. User uploads a `.txt` medical report via the frontend
2. File is sent to the FastAPI backend via POST request
3. Backend extracts medical entities using regex patterns
4. Claude AI API generates a patient-friendly summary
5. Results are returned and displayed instantly on the UI

---

## ⚙️ Entity Extraction Logic

| Entity | Method |
|--------|--------|
| Age | Regex — e.g., "45 years old", "45-year-old" |
| Gender | Keyword matching — pronouns and gender terms |
| Conditions | Predefined list — diabetes, hypertension, fever, etc. |
| Medications | Predefined drug list — Metformin, Aspirin, etc. |

---

## 🧰 Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | Python, FastAPI |
| AI | Anthropic Claude API |
| Server | Uvicorn |
| Data | python-multipart, Pandas |

---

## 📂 Repository Structure

```
ai-medical-analyzer/
│
├── frontend/
│   └── index.html
│
├── data/
│   ├── sample_report.txt
│   └── mtsamples.csv
│
├── assets/
│   ├── input.png
│   └── output.png
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/Kreetikakishore/ai-medical-analyzer.git
cd ai-medical-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Anthropic API Key

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

Get your API key at [console.anthropic.com](https://console.anthropic.com)

### 4. Start the Backend Server

```bash
uvicorn app:app --reload
```

### 5. Open Frontend

Open `frontend/index.html` in your browser — no build step needed.

---

## 🔌 API Reference

### POST /analyze

Accepts a `.txt` file upload and returns analysis results.

**Request:** `multipart/form-data` with a `file` field

**Response:**
```json
{
  "entities": {
    "age": "45 years",
    "gender": "Male",
    "conditions": ["Hypertension", "Diabetes", "Fever", "Infection"],
    "medications": ["Metformin", "Lisinopril"]
  },
  "summary": "Patient-friendly summary here... ⚠️ Disclaimer: ...",
  "original_length": 87
}
```

### GET /
Health check endpoint.
```json
{ "status": "AI Medical Report Analyzer is running" }
```

---

## 🧪 Sample Report

```
Patient: John Doe
Age: 45 years old
Gender: Male

The patient presents with hypertension and type 2 diabetes.
He has been prescribed Metformin and Lisinopril.
Blood pressure is 145/90 mmHg. Blood sugar levels are elevated at 180 mg/dL.
Patient is advised to follow a low-sugar diet and exercise regularly.
Follow-up appointment scheduled in 2 weeks.
```

---

## 🌍 Real-World Applications

- Patient report simplification in hospitals
- Healthcare accessibility tools
- Clinical documentation assistants
- Medical education platforms
- Telemedicine pre-consultation tools

---

## 📈 Key Impact

- ✅ Converts complex clinical language into plain English
- ✅ Extracts structured entities from unstructured text
- ✅ Powered by state-of-the-art Claude AI
- ✅ Zero database dependency — fully lightweight

---

## 💡 Future Improvements

- Support PDF medical report uploads
- Add multi-language summary generation
- Deploy on cloud platforms (Render / Railway)
- Expand entity extraction with advanced NLP models
- Add doctor vs patient view toggle

---

## 🛡️ Disclaimer

This tool is for educational and informational purposes only. AI-generated summaries are not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

---

## ⚠️ Note

This project was developed as an AI portfolio case study to demonstrate end-to-end API development, NLP entity extraction, and Claude AI integration in the healthcare domain.

---

## 👤 Author

**Kreetika Kishore**
Data Analytics & AI Portfolio Project | 2026

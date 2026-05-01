# 🏥 AI Medical Report Analyzer

A lightweight, full-stack web app that analyzes plain-text medical reports and returns a **patient-friendly summary** along with extracted medical entities — powered by the **Claude AI API** and a **FastAPI** backend.

---

## ✨ Features

- 📄 Upload any `.txt` medical report
- 🔍 Extracts key entities: age, gender, conditions, and medications
- 🧠 Generates a patient-friendly AI summary using Claude
- ⚠️ Includes a medical disclaimer on every result
- 📊 Displays word count and total entities found
- 🎨 Clean, minimal frontend — no frameworks required

---

## 🗂️ Project Structure

```
ai-medical-analyzer/
├── app.py                  # FastAPI backend
├── requirements.txt        # Python dependencies
├── frontend/
│   └── index.html          # Frontend UI
└── data/
    ├── sample_report.txt   # Sample medical report for testing
    └── mtsamples.csv       # Medical transcription dataset (optional)
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-medical-analyzer.git
cd ai-medical-analyzer
```

### 2. Install Dependencies

Make sure you have **Python 3.8+** installed, then run:

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**
```
fastapi
uvicorn
pandas
anthropic
python-multipart
```

### 3. Set Your Anthropic API Key

The backend uses the Anthropic Claude API. Export your API key as an environment variable:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

> Get your API key at [console.anthropic.com](https://console.anthropic.com)

### 4. Start the Backend Server

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### 5. Open the Frontend

Simply open `frontend/index.html` in your browser — no build step needed.

---

## 🧪 Usage

1. Open `frontend/index.html` in your browser
2. Click the upload area and select a `.txt` medical report
3. Click **ANALYZE REPORT**
4. View extracted entities and your patient-friendly summary

### Sample Report (`data/sample_report.txt`)

```
Patient: John Doe
Age: 45 years old
Gender: Male

The patient presents with hypertension and type 2 diabetes.
He has been prescribed Metformin and Lisinopril.
Patient also reports mild fever and infection in the lower respiratory tract.
Blood pressure is 145/90 mmHg. Blood sugar levels are elevated at 180 mg/dL.
Patient is advised to follow a low-sugar diet and exercise regularly.
Follow-up appointment scheduled in 2 weeks.
```

---

## 🔌 API Reference

### `POST /analyze`

Accepts a `.txt` file upload and returns analysis results.

**Request:** `multipart/form-data` with a `file` field.

**Response:**
```json
{
  "entities": {
    "age": "45 years",
    "gender": "Male",
    "conditions": ["Hypertension", "Diabetes", "Fever", "Infection"],
    "medications": ["Metformin", "Lisinopril"]
  },
  "summary": "The patient presents with hypertension and type 2 diabetes...\n\n⚠️ Disclaimer: ...",
  "original_length": 87
}
```

### `GET /`

Health check endpoint.

```json
{ "status": "AI Medical Report Analyzer is running" }
```

---

## ⚙️ How It Works

### Entity Extraction (`extract_entities`)
Uses **regex patterns** to identify:
- **Age** — e.g., "45 years old", "45-year-old"
- **Gender** — based on pronouns and keywords
- **Conditions** — from a predefined list (diabetes, hypertension, fever, etc.)
- **Medications** — from a predefined drug list (Metformin, Aspirin, etc.)

### Summarization (`summarize_report`)
Uses a **keyword scoring** approach to identify the most medically relevant sentences, selects the top 4, and appends a standard medical disclaimer.

---

## 🛡️ Disclaimer

> This tool is for **educational and informational purposes only**. The AI-generated summaries are **not a substitute for professional medical advice, diagnosis, or treatment**. Always consult a qualified healthcare provider.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | Python, FastAPI |
| AI | Anthropic Claude API |
| Server | Uvicorn |
| Data | python-multipart, pandas |

---

## 📄 Author

Kreetika Kishore

---
📸 Demo
<img width="1112" height="585" alt="Screenshot 2026-05-01 093924" src="https://github.com/user-attachments/assets/05071fcf-06f3-4c90-9b98-d539c5ed0b6a" />
<img width="674" height="1024" alt="Screenshot 2026-05-01 093958" src="https://github.com/user-attachments/assets/8254c215-70cc-4209-8811-1a77ea2aada6" />


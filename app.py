from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_entities(text):
    entities = {}
    age = re.findall(r'\b(\d+)[\s-]*(year|yr|y/o|years)[\s-]*(old)?\b', text, re.IGNORECASE)
    if age:
        entities["age"] = age[0][0] + " years"
    if re.search(r'\b(male|man|boy|he|his)\b', text, re.IGNORECASE):
        entities["gender"] = "Male"
    elif re.search(r'\b(female|woman|girl|she|her)\b', text, re.IGNORECASE):
        entities["gender"] = "Female"
    conditions = re.findall(r'\b(diabetes|hypertension|asthma|cancer|infection|fever|pneumonia|fracture|anemia|depression|anxiety|covid|tuberculosis|arthritis)\b', text, re.IGNORECASE)
    if conditions:
        entities["conditions"] = list(set([c.capitalize() for c in conditions]))
    meds = re.findall(r'\b(aspirin|metformin|insulin|paracetamol|ibuprofen|amoxicillin|lisinopril|atorvastatin|omeprazole|prednisone)\b', text, re.IGNORECASE)
    if meds:
        entities["medications"] = list(set([m.capitalize() for m in meds]))
    return entities

def summarize_report(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    
    keywords = [
        "diagnosis", "prescribed", "treatment", "condition", "patient",
        "blood", "pressure", "sugar", "advised", "symptoms", "reports",
        "presents", "follow", "medication", "infection", "fever"
    ]
    
    scored = []
    for sentence in sentences:
        score = sum(1 for word in keywords if word.lower() in sentence.lower())
        scored.append((score, sentence))
    
    scored.sort(reverse=True)
    top_sentences = [s[1] for s in scored[:4]]
    
    summary = " ".join(top_sentences)
    
    disclaimer = "\n\n⚠️ Disclaimer: This summary is AI-generated and is not a medical diagnosis. Please consult a qualified doctor for medical advice."
    
    return summary + disclaimer

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    entities = extract_entities(text)
    summary = summarize_report(text)
    return {
        "entities": entities,
        "summary": summary,
        "original_length": len(text.split()),
    }

@app.get("/")
def root():
    return {"status": "AI Medical Report Analyzer is running"}
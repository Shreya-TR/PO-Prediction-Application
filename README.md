# PO L1–L2–L3 Classifier 🧾
Turn Purchase Order descriptions into structured category labels — fast and clean.

PO L1–L2–L3 Classifier is a lightweight AI utility that transforms messy PO descriptions into structured, taxonomy-based categories.

It’s designed for procurement teams, analysts, and operations professionals who need clarity and consistency in classification.

🚀 Live Application  
👉 https://poclassifier.streamlit.app/
🎯 Why This Tool?
PO descriptions are often:

Vague or inconsistent  
Hard to standardize  
Time-consuming to classify  
Error-prone across teams  

This tool helps you move from manual guessing → clear taxonomy → actionable data.

This is not a chatbot.  
It is a classification utility.

✨ Core Features
1️⃣ PO Text → L1/L2/L3 Categories  
Classify a single PO into:
- L1 category  
- L2 category  
- L3 category  
- JSON output  

2️⃣ Batch Classification (CSV)  
Upload a CSV and get:
- Auto-classified rows  
- Error handling  
- Downloadable results  

3️⃣ Strict Output Format  
Model outputs are forced into valid JSON with:
- Deterministic formatting  
- “Not sure” fallback for ambiguity  

🧠 How It Works
User provides PO description  
AI reads taxonomy + rules  
Prompt-engineered logic enforces structure  
Output is normalized JSON  

Uses deterministic LLM output with strict formatting rules.

🛠 Tech Stack
Python  
Streamlit (Frontend)  
Groq LLM API  
Prompt Engineering  
JSON-based output contracts  

📂 Project Structure
po-classifier/  
│  
├── app.py # Streamlit UI  
├── classifier.py # Groq API client  
├── prompts.py # System prompts  
├── taxonomy.py # Fixed taxonomy  
├── requirements.txt  
└── README.md  

Run Locally
pip install -r requirements.txt  
streamlit run app.py  

Add your API key in  
.streamlit/secrets.toml  
GROQ_API_KEY = ""  

Author  
Shreya T R

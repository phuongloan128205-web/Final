📝 AI Writing Feedback System
📌 Description

This project is an AI-powered writing feedback system that analyzes English text and provides intelligent suggestions to improve writing quality.

The system detects grammar errors, evaluates vocabulary level, analyzes coherence, and generates an overall score, along with automated feedback similar to a teacher.

🎯 Research Question

Can AI automatically detect grammatical errors and improve English writing quality?

⚙️ Methodology

The system applies the following techniques:

Grammar checking using LanguageTool
Vocabulary analysis based on word length
Coherence detection using linking words (e.g., however, therefore)
Rule-based scoring system based on grammar errors
Automated feedback generation based on writing performance
🚀 Features
✨ Core Features
✏️ Input paragraph and analyze writing quality
❌ Detect grammar errors
💡 Provide corrected version of the text
🧠 Evaluate vocabulary level (Basic / Intermediate / Advanced)
🔗 Analyze coherence using linking words
📊 Assign a score (0–10)
🔥 Advanced Features (NEW)
🌙 Dark Mode Toggle
📂 Upload .txt file for analysis
🤖 AI-style automatic feedback (like a teacher)
📊 Dashboard with metrics (Score, Errors, Vocabulary, Coherence)
📈 Score progress chart
📥 Download results as CSV
🧠 Technologies Used
Python
Streamlit
LanguageTool
Pandas
Matplotlib
📂 Project Structure
ai-writing-feedback/
│
├── app.py              # Main Streamlit application
├── history.csv         # Saved results (auto-generated)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
▶️ How to Run the Project
1. Install dependencies
pip install -r requirements.txt
2. Run the application
streamlit run app.py
3. Open in browser
http://localhost:8501
📊 How It Works
User inputs text or uploads a .txt file
The system checks grammar using LanguageTool
Errors are detected and corrected automatically
Vocabulary complexity is calculated
Coherence is evaluated using linking words
A score is generated based on errors
AI-style feedback is provided
Results are saved and visualized
📈 Example Output
Score: 7.5 / 10
Grammar errors detected
Corrected version provided
Vocabulary level: Intermediate
Coherence: Good

AI Feedback:

"Your writing is average but needs improvement. There are some grammar errors to fix."

📊 Evaluation

The system was tested with multiple essays of varying difficulty levels:

Essays with more grammatical errors received lower scores
Well-written essays achieved higher scores

This demonstrates the system’s effectiveness in improving writing quality.

💡 Future Improvements
Integrate AI models (e.g., GPT, BERT) for smarter correction
Add IELTS band estimation
Highlight errors directly in text (like Grammarly)
Support multiple languages
User authentication system
Deploy online (Streamlit Cloud)
👨‍💻 Author
Student Project – AI Writing Feedback System
⭐ Notes

This project demonstrates the application of:

Natural Language Processing (NLP)
Rule-based AI systems
Interactive Web Apps using Streamlit

in a real-world writing assistant system.

🚀 Project Level

This version includes advanced UI and intelligent feedback features, making it comparable to a mini Grammarly-like system.
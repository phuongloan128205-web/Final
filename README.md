# 📝 AI Writing Feedback System

## 📌 Description

This project is an **AI-powered writing feedback system** that analyzes English text and provides suggestions to improve writing quality.

It detects **grammar errors**, evaluates **vocabulary level**, checks **coherence**, and assigns an overall **score**.

---

## 🎯 Research Question

Can AI automatically detect grammatical errors and improve English writing quality?

---

## ⚙️ Methodology

The system applies the following techniques:

* Grammar checking using **LanguageTool**
* Vocabulary analysis based on word length
* Coherence detection using linking words (e.g., however, therefore)
* Scoring based on number of grammatical errors

---

## 🚀 Features

* ✏️ Input paragraph and analyze writing quality
* ❌ Detect grammar errors
* 💡 Provide corrected version of the text
* 🧠 Evaluate vocabulary level (Basic / Intermediate / Advanced)
* 🔗 Analyze coherence using linking words
* 📊 Assign a score (0–10)
* 📈 Track writing history
* 📥 Download results as CSV
* 📉 Display score progress chart

---

## 🧠 Technologies Used

* Python
* Streamlit
* LanguageTool
* Pandas
* Matplotlib

---

## 📂 Project Structure

```id="6r1v7m"
ai-writing-feedback/
│
├── app.py              # Main Streamlit application
├── history.csv         # Saved results (auto-generated)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ▶️ How to Run the Project

### 1. Install dependencies

```id="gkpl6y"
pip install -r requirements.txt
```

### 2. Run the application

```id="r4c8jm"
streamlit run app.py
```

### 3. Open in browser

```id="h9r4bz"
http://localhost:8501
```

---

## 📊 How It Works

1. User inputs a paragraph
2. System checks grammar using LanguageTool
3. Text is corrected automatically
4. Vocabulary level is calculated based on word complexity
5. Coherence is detected using linking words
6. Final score is generated
7. Results are saved for tracking and analysis

---

## 📈 Example Output

* Score: 7.5 / 10
* Grammar errors detected
* Corrected version provided
* Vocabulary level: Intermediate
* Coherence: Good

---

## 📊 Evaluation

The system was tested with multiple essays of varying difficulty levels.

* Essays with more grammatical errors received lower scores
* Well-written essays achieved higher scores

This demonstrates the effectiveness of the system in improving writing quality.

---

## 💡 Future Improvements

* Add AI-based deep learning models (e.g., NLP transformers)
* Improve grammar correction accuracy
* Add support for multiple languages
* Enhance UI/UX design
* Deploy online (Streamlit Cloud)

---

## 👨‍💻 Author

* Student Project – AI Writing Feedback System

---

## ⭐ Notes

This project demonstrates the application of **Natural Language Processing (NLP)** and **Machine Learning concepts** in real-world writing assistance systems.

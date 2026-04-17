# 📝 AI Writing Feedback System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![NLP](https://img.shields.io/badge/Field-NLP-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Description

This project is an **AI-powered writing feedback system** that analyzes English text and provides intelligent suggestions to improve writing quality.

The system detects **grammar errors**, evaluates **vocabulary level**, analyzes **coherence**, and generates an overall **score**, along with **AI-style feedback** similar to a teacher.

---

## 🎯 Research Question

> Can AI automatically detect grammatical errors and improve English writing quality?

---

## ⚙️ Methodology

The system applies the following techniques:

* Grammar checking using **LanguageTool**
* Vocabulary analysis based on word complexity
* Coherence detection using linking words *(e.g., however, therefore)*
* Rule-based scoring system
* Automated feedback generation

---

## 🚀 Features

### ✨ Core Features

* ✏️ Input paragraph and analyze writing quality
* ❌ Detect grammar errors
* 💡 Provide corrected version
* 🧠 Evaluate vocabulary level *(Basic / Intermediate / Advanced)*
* 🔗 Analyze coherence
* 📊 Assign score *(0–10)*

### 🔥 Advanced Features

* 🌙 Dark Mode
* 📂 Upload `.txt` file
* 🤖 AI-style automatic feedback
* 📊 Dashboard with metrics
* 📈 Score progress chart
* 📥 Export results to CSV

---

## 📊 How It Works

1. User inputs text or uploads a `.txt` file
2. System checks grammar using LanguageTool
3. Text is corrected automatically
4. Vocabulary level is calculated
5. Coherence is evaluated
6. Score is generated
7. AI feedback is provided
8. Results are saved and visualized

---

## 📈 Example Output

* **Score:** 7.5 / 10
* **Grammar errors detected**
* **Corrected version provided**
* **Vocabulary level:** Intermediate
* **Coherence:** Good

💡 Feedback:

> Your writing is average but needs improvement. There are some grammar errors to fix.

---

## 🧠 Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| Streamlit    | Web interface             |
| LanguageTool | Grammar checking          |
| Pandas       | Data processing           |
| Matplotlib   | Data visualization        |

---

## 📂 Project Structure

```
ai-writing-feedback/
│
├── app.py              # Main application
├── history.csv         # Stored results
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

### 3. Open browser

```
http://localhost:8501
```

---

## 📊 Evaluation

The system was tested with essays of varying difficulty levels:

* Essays with more grammar errors → lower scores
* Well-written essays → higher scores

✅ This demonstrates the effectiveness of the system.

---

## 💡 Future Improvements

* Integrate advanced AI models *(GPT, BERT)*
* Add IELTS band estimation
* Highlight errors in text *(like Grammarly)*
* Multi-language support
* Deploy online *(Streamlit Cloud)*

---

## 👨‍💻 Author

**Phuong Loan – AI Writing Feedback System**

---

## ⭐ Project Highlights

* Combines **NLP + AI + Web App**
* Practical real-world application
* Interactive and user-friendly interface
* Comparable to a **mini Grammarly system**

---

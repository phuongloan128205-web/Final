import streamlit as st
import language_tool_python
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# ===== INIT =====
tool = language_tool_python.LanguageTool('en-US')
DATA_FILE = "history.csv"

st.set_page_config(page_title="AI Writing Feedback", page_icon="📝", layout="wide")

# ===== DARK MODE =====
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
    <style>
    .main {background-color: #0e1117; color: white;}
    .stTextArea textarea {background-color: #262730; color: white;}
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .main {background-color: #f5f7fa;}
    </style>
    """, unsafe_allow_html=True)

# ===== FUNCTIONS =====
def analyze_essay(text):
    matches = tool.check(text)
    num_errors = len(matches)

    corrected = language_tool_python.utils.correct(text, matches)

    words = text.split()
    long_words = [w for w in words if len(w) > 6]
    vocab_score = len(long_words) / len(words) if words else 0

    linking_words = ["however", "therefore", "although", "because"]
    coherence = any(word in text.lower() for word in linking_words)

    score = max(0, 10 - num_errors * 0.5)

    return score, matches, corrected, vocab_score, coherence


def generate_feedback(score, errors, vocab, coherence):
    feedback = ""

    if score >= 8:
        feedback += "Your writing is very good. "
    elif score >= 5:
        feedback += "Your writing is average but needs improvement. "
    else:
        feedback += "Your writing has many issues. "

    if errors > 10:
        feedback += "You should focus on reducing grammar mistakes. "
    elif errors > 5:
        feedback += "There are some grammar errors to fix. "
    else:
        feedback += "Grammar is mostly correct. "

    if vocab > 0.3:
        feedback += "Your vocabulary is advanced. "
    elif vocab > 0.15:
        feedback += "Your vocabulary is acceptable. "
    else:
        feedback += "Try to use more complex words. "

    if not coherence:
        feedback += "Use linking words to improve coherence."

    return feedback


def save_result(score, errors, vocab, coherence):
    data = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Score": round(score, 1),
        "Errors": errors,
        "Vocab_Level": (
            "Advanced" if vocab > 0.3 else
            "Intermediate" if vocab > 0.15 else
            "Basic"
        ),
        "Coherence": "Good" if coherence else "Needs Improvement"
    }

    df = pd.DataFrame([data])

    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)


def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame()


# ===== SIDEBAR =====
st.sidebar.title("⚙️ About App")
st.sidebar.info("""
AI Writing Feedback System

✔ Grammar Check  
✔ Vocabulary Analysis  
✔ Coherence Detection  
✔ Score Tracking  
""")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by Phuong Loan")

# ===== HEADER =====
st.title("📝 AI Writing Feedback System")
st.caption("Improve your English writing with AI")

# ===== INPUT =====
st.subheader("✏️ Enter your paragraph")

text = st.text_area("", height=180, placeholder="Type your essay here...")

# ===== UPLOAD FILE =====
uploaded_file = st.file_uploader("📂 Upload .txt file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("📄 File Content", text, height=150)

# ===== BUTTON =====
if st.button("🚀 Analyze Essay"):
    if text.strip() == "":
        st.warning("Please enter text!")
    else:
        score, errors, corrected, vocab, coherence = analyze_essay(text)
        save_result(score, len(errors), vocab, coherence)

        # ===== DASHBOARD =====
        st.subheader("📊 Results Overview")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Score", f"{score:.1f}/10")
        col2.metric("Errors", len(errors))
        col3.metric("Vocabulary", 
            "Advanced" if vocab > 0.3 else
            "Intermediate" if vocab > 0.15 else "Basic")
        col4.metric("Coherence", "Good" if coherence else "Weak")

        st.progress(score / 10)

        # ===== TABS =====
        tab1, tab2, tab3 = st.tabs(["❌ Errors", "💡 Correction", "🧠 Analysis"])

        with tab1:
            if errors:
                for e in errors:
                    st.error(e.message)
            else:
                st.success("No grammar errors 🎉")

        with tab2:
            st.success(corrected)

        with tab3:
            st.write("### 🧠 AI Feedback")

            feedback = generate_feedback(score, len(errors), vocab, coherence)
            st.info(feedback)

            st.write("### 📌 Detailed Analysis")
            st.write(f"- Errors detected: {len(errors)}")
            st.write(f"- Vocabulary level: {'High' if vocab > 0.3 else 'Medium' if vocab > 0.15 else 'Low'}")
            st.write(f"- Coherence: {'Good' if coherence else 'Needs improvement'}")

# ===== STATISTICS =====
st.subheader("📈 Writing History")

df = load_data()

if not df.empty:
    col1, col2 = st.columns(2)

    col1.metric("📄 Total Essays", len(df))
    col2.metric("⭐ Avg Score", round(df["Score"].mean(), 2))

    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots()
    ax.plot(df["Score"], marker='o')
    ax.set_title("Score Progress")
    ax.set_xlabel("Attempts")
    ax.set_ylabel("Score")

    st.pyplot(fig)

    st.download_button(
        "📥 Download CSV",
        df.to_csv(index=False),
        "history.csv",
        "text/csv"
    )
else:
    st.info("No data yet. Start analyzing!")

# ===== FOOTER =====
st.markdown("---")
st.caption("AI Writing Feedback System | Final Project 🚀")
import streamlit as st
import google.generativeai as genai
import os

# ------------------------------
# Configure API Key
# ------------------------------
# Replace with your actual key, or store it as an environment variable
genai.configure(api_key="AIzaSyCDL3a21Mx6e51iMpO_tdILTgPgyT88OA4")

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# ------------------------------
# Streamlit UI
# ------------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #00FF00 ;'>📝 AI Language Tutor</h1>
    <p style='text-align: center; font-size: 18px;'>
    Practice English writing — get corrections, explanations, rewrites, and feedback in real-time.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("Improve your English sentences with corrections and explanations.")

# User input
user_text = st.text_area("✍️ Enter your sentence or paragraph:")

if st.button("Analyze"):
    if user_text.strip():
        # Prompt template (Intermediate level)
        prompt = f"""
        You are an English language tutor for intermediate learners.
        Correct the following text, then explain the mistakes simply.
        
        Text: {user_text}
        
        Format your response like this:
        Corrected:
        <corrected text>

        Explanations:
        1) ...
        2) ...
        """
        
        # Call the model
        response = model.generate_content(prompt)
        
        # Show output
        st.subheader("✅ Results")
        st.write(response.text)
    else:
        st.warning("Please enter some text first.")
# ------------------------------
# Extra Features: Rewriting
# ------------------------------

st.markdown(
    """
    <h4 style='text-align: left; color:  #FFB6C1 ;'>✍️ Try rewriting your text</h4>
    """,
    unsafe_allow_html=True
)



# Dropdown to choose style
style = st.selectbox(
    "Choose a rewrite style:",
    ["Simplify", "Formalize", "Shorten"]
)

if st.button("Rewrite"):
    if user_text.strip():
        prompt = f"""
        Rewrite the following text in {style.lower()} style.
        Keep the original meaning the same.
        
        Text: {user_text}
        """
        response = model.generate_content(prompt)
        st.subheader(f"🔄 {style} Version")
        st.write(response.text)
    else:
        st.warning("Please enter some text first.")
# ------------------------------
# Fluency Score & Feedback
# ------------------------------
st.markdown(
    """
    <h4 style='text-align: left; color: #ADD8E6 ;'>📊 Fluency Feedback</h4>
    """,
    unsafe_allow_html=True
)


if user_text.strip():
    prompt = f"""
    Evaluate the fluency of the following English text.
    Give a score from 0 (very poor) to 100 (excellent).
    Then provide 2–3 sentences of feedback on how the user can improve.

    Text: {user_text}
    """
    response = model.generate_content(prompt)
    st.write(response.text)

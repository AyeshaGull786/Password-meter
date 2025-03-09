import re
import random
import string
import streamlit as st

# Commonly used weak passwords
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "password123", "abc123", 
    "letmein", "123123", "admin", "welcome", "monkey", "football", "iloveyou", 
    "sunshine", "1234", "princess"
}

# Function to evaluate password strength
def evaluate_password(password):
    score = 0
    feedback = []
    
    if password in COMMON_PASSWORDS:
        return 1, "❌ Weak: Your password is too common! Choose a unique one."
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Increase length to at least 8 characters.")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("🟡 Add an uppercase letter.")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("🟡 Add a lowercase letter.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("🟡 Include at least one digit.")
    
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("🟡 Use at least one special character (!@#$%^&*).")
    
    if score >= 5:
        return score, "✅ Strong Password! Well done."
    elif score >= 3:
        return score, "⚠️ Moderate: " + " ".join(feedback)
    else:
        return score, "❌ Weak: " + " ".join(feedback)

# Function to generate a strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
    
    # Custom CSS for stylish theme (White & Blue)
    st.markdown("""
        <style>
            body {
                background-color: #f4f8fb;
                color: #333;
                font-family: 'Arial', sans-serif;
            }
            .stTextInput>div>div>input {
                background-color: #ffffff;
                color: #333;
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #ccc;
            }
            .stButton>button {
                background-color: #007BFF;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                width: 100%;
                padding: 10px;
                border: none;
            }
            .stButton>button:hover {
                background-color: #0056b3;
            }
            .result-box {
                background-color: #ffffff;
                color: #333;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                margin-top: 20px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                border-left: 5px solid #007BFF;
            }
            .info-card {
                background-color: #ffffff;
                color: #333;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                border-left: 5px solid #28a745;
            }
            .tips-box {
                background-color: #e3f2fd;
                padding: 15px;
                border-radius: 10px;
                color: #333;
                margin-top: 20px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; color: #007BFF;'>🔐一═⌊✪⌋ Locksafe Password Evaluator ⌊✪⌋═一</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Check your password strength and get suggestions! 🛡️</h4>", unsafe_allow_html=True)

    with st.container():
        password = st.text_input("🔑 Enter a password:", type="password", key="password_input", placeholder="Enter your password...")
        
        if st.button("🔍 Check Password Strength"):
            if password:
                score, message = evaluate_password(password)
                st.markdown(f"<div class='result-box'><h3>Strength Score: {score}/5</h3><p>{message}</p></div>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ Please enter a password to check.")
    
    st.markdown("---")
    
    st.markdown("<h3 style='color: #28a745;'>✨ Generate a Strong Password</h3>", unsafe_allow_html=True)
    
    # Slider to choose password length
    length = st.slider("🎚️ Select Password Length", min_value=8, max_value=20, value=12)

    if st.button("⚡ Generate Password"):
        strong_password = generate_password(length)
        st.markdown(f"<div class='info-card'><strong>🔑 Generated Password:</strong> <code>{strong_password}</code></div>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #007BFF;'>📌 Tips for a Strong Password:</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class='tips-box'>
            <ul>
                <li>✅ Use at least 12 characters.</li>
                <li>🔠 Include uppercase, lowercase, numbers, and special characters.</li>
                <li>🚫 Avoid common passwords and personal details.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()

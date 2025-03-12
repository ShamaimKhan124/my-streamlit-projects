import streamlit as st
import re
import requests
import math
import random
import string


def check_password_strength(password):
    strength = 0
    remarks = []
    
    
    if len(password) >= 16:
        strength += 3
    elif len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        remarks.append("Increase password length (min 16 characters recommended)")
    
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        strength += 1
    else:
        remarks.append("Use both uppercase and lowercase letters")
    
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        remarks.append("Include at least one number")
    
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks.append("Include at least one special character (@, $, !, %, *, ?, &)")
    
    
    if len(set(password)) > 8:
        strength += 1
    else:
        remarks.append("Use more unique characters for better security")
    
    entropy = calculate_entropy(password)
    if entropy < 60:
        remarks.append("Increase password complexity (more unique characters and mix cases)")
    
    return strength, remarks, entropy


def calculate_entropy(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if re.search(r"[@$!%*?&]", password):
        charset_size += 10  
    
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)


def generate_strong_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))


st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="wide")
st.sidebar.title("⚙️ Customize Password Generator")


password_length = st.sidebar.slider("Select Password Length", min_value=8, max_value=32, value=16)
use_uppercase = st.sidebar.checkbox("Include Uppercase Letters", True)
use_numbers = st.sidebar.checkbox("Include Numbers", True)
use_special_chars = st.sidebar.checkbox("Include Special Characters", True)

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #1d2671, #c33764);
            color: white;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4caf50 !important;
            color: white !important;
            border-radius: 10px !important;
            font-size: 16px !important;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 2px solid #03dac6;
            font-size: 16px;
        }
        .stProgress > div > div > div {
            background-color: #ffeb3b;
        }
        .stSidebar {
            background-color: #2c3e50;
            padding: 20px;
            border-radius: 10px;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔒 Advanced Password Strength Meter")
st.markdown("Analyze your password strength and generate a secure one!")

password = st.text_input("Enter Password", type="password")
if password:
    strength, remarks, entropy = check_password_strength(password)
    
    
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Unbreakable"]
    st.markdown(f"**Password Strength:** {strength_levels[min(strength, 5)]}")
    st.progress(strength / 5)
    
    
    st.write(f"**Entropy Score:** {entropy} bits")
    if remarks:
        st.warning("⚠️ Suggestions to improve password strength:")
        for remark in remarks:
            st.markdown(f"- {remark}")
    

if st.button("Generate Secure Password"):
    strong_password = generate_strong_password(password_length)
    st.success(f"🔑 Suggested Secure Password: `{strong_password}`")
    st.caption("Ensure to store this password securely.")

import streamlit as st
import pandas as pd
import plotly.express as px
from pint import UnitRegistry

ureg = UnitRegistry()
ureg.default_format = "~P"

st.set_page_config(page_title="🌟 Professional Unit Converter", layout="wide")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/189/189665.png", width=100)
st.sidebar.header("🔹 🧭 Navigation Panel")
st.sidebar.subheader("📌 Select Unit Category")

category = st.sidebar.radio(
    "📏 Choose a category:",
    ["📏 Length", "⚖️ Weight", "🌡️ Temperature", "⏳ Time", "🚀 Speed", "🧪 Volume", "📐 Area", "⚡ Energy"],
    horizontal=True
)

dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

def set_theme():
    if dark_mode:
        return """
        <style>
        body { background-color: #0D0D0D; color: #00FFCC; font-family: 'Arial', sans-serif; }
        .stButton>button { background-color: #00FFCC; color: #0D0D0D; font-size: 18px; border-radius: 10px; padding: 10px 20px; transition: 0.3s; text-shadow: 0px 0px 10px #00FFCC; }
        .stButton>button:hover { background-color: #FF00FF; transform: scale(1.05); text-shadow: 0px 0px 15px #FF00FF; }
        .stSidebar { background-color: #1A1A1A; color: #00FFCC; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px #00FFCC; }
        .stSidebar div, .stSidebar label, .stSidebar span { color: #00FFCC !important; }
        .stSuccess { font-size: 20px; font-weight: bold; color: #00FFCC; padding: 10px; border-radius: 5px; background-color: #121212; box-shadow: 0px 0px 10px #00FFCC; }
        .header { font-size: 40px; font-weight: bold; color: #00FFCC; text-align: center; margin-bottom: 20px; text-shadow: 0px 0px 15px #00FFCC; }
        </style>
        """
    else:
        return """
        <style>
        body { background-color: #ffffff; color: #000000; font-family: 'Arial', sans-serif; }
        .stButton>button { background-color: #007BFF; color: white; font-size: 18px; border-radius: 10px; padding: 10px 20px; transition: 0.3s; }
        .stButton>button:hover { background-color: #0056b3; transform: scale(1.05); }
        .stSidebar { background-color: #f8f9fa; color: black; padding: 20px; border-radius: 10px; }
        .stSidebar div, .stSidebar label, .stSidebar span { color: black !important; }
        .stSuccess { font-size: 20px; font-weight: bold; color: #007BFF; padding: 10px; border-radius: 5px; background-color: #D4EDDA; }
        .header { font-size: 40px; font-weight: bold; color: #007BFF; text-align: center; margin-bottom: 20px; }
        </style>
        """

st.markdown(set_theme(), unsafe_allow_html=True)

st.markdown("<div class='header'>💡 Professional Unit Converter</div>", unsafe_allow_html=True)

history = []
def convert_units(value, from_unit, to_unit):
    try:
        if from_unit == "kilowatt-hour" and to_unit == "joule":
            result = value * 3.6e6  # 1 kWh = 3.6 × 10^6 Joules
        elif from_unit == "joule" and to_unit == "kilowatt-hour":
            result = value / 3.6e6  # Joules to kWh
        elif from_unit in ["celsius", "fahrenheit", "kelvin"] or to_unit in ["celsius", "fahrenheit", "kelvin"]:
            result = ureg.Quantity(value, ureg[from_unit]).to(ureg[to_unit])
        else:
            result = (value * ureg(from_unit)).to(to_unit)
        history.append((value, from_unit, result, to_unit))
        return round(result, 4)
    except Exception as e:
        return f"Error: {e}"

st.subheader(f"📏 Convert {category} Units")
value = st.number_input("Enter Value", value=1.0, step=0.1)

unit_options = {
    "📏 Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "⚖️ Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
    "⏳ Time": ["second", "minute", "hour", "day"],
    "🚀 Speed": ["meter/second", "kilometer/hour", "mile/hour", "foot/second"],
    "🧪 Volume": ["liter", "milliliter", "gallon", "cubic meter", "cubic inch"],
    "📐 Area": ["square meter", "square kilometer", "square mile", "square foot", "square inch"],
    "⚡ Energy": ["joule", "calorie", "kilowatt-hour", "BTU"]
}

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("🔻 From Unit", unit_options[category])
with col2:
    to_unit = st.selectbox("🔺 To Unit", unit_options[category])

if st.button("🔄 Convert Now"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"✅ {value} {from_unit} = {result} {to_unit}")

if history:
    st.markdown("### 🔍 Conversion History")
    df = pd.DataFrame(history, columns=["Input Value", "From Unit", "Converted Value", "To Unit"])
    st.dataframe(df)

st.sidebar.markdown("""
---
📌 **Developed by SHAMAIMKHAN**

🔹 Sleek & Modern UI with Light/Dark Mode  
🔹 Live Conversions & History Tracking  
🔹 Glow Effects for Buttons & Sidebar  
""")

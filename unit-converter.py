import streamlit as st
import pandas as pd

def convert_units(value, from_unit, to_unit):
    conversions = {
        # Length
        ("m", "cm"): value * 100,
        ("cm", "m"): value / 100,
        ("m", "km"): value / 1000,
        ("km", "m"): value * 1000,
        ("inch", "cm"): value * 2.54,
        ("cm", "inch"): value / 2.54,
        
        # Weight
        ("kg", "g"): value * 1000,
        ("g", "kg"): value / 1000,
        ("lb", "kg"): value * 0.453592,
        ("kg", "lb"): value / 0.453592,
        
        # Temperature
        ("C", "F"): (value * 9/5) + 32,
        ("F", "C"): (value - 32) * 5/9,
        ("C", "K"): value + 273.15,
        ("K", "C"): value - 273.15,
        ("F", "K"): (value - 32) * 5/9 + 273.15,
        ("K", "F"): (value - 273.15) * 9/5 + 32,
        
        # Speed
        ("m/s", "km/h"): value * 3.6,
        ("km/h", "m/s"): value / 3.6,
        ("mph", "km/h"): value * 1.60934,
        ("km/h", "mph"): value / 1.60934,
        
        # Time
        ("min", "sec"): value * 60,
        ("sec", "min"): value / 60,
        ("hr", "min"): value * 60,
        ("min", "hr"): value / 60
    }
    return conversions.get((from_unit, to_unit), "Conversion not supported")

# Streamlit UI
st.set_page_config(page_title="Unit Converter", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: lightblue;
    }
    .stApp {
        background: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngegg.com%2Fen%2Fpng-ppjrj&psig=AOvVaw36WvFSDMAA5ip6HJb-Pt11&ust=1741504636354000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLDLjcL4-YsDFQAAAAAdAAAAABAR");
        background-size: cover;
    }
    h1 {
        color: black;
        text-align: center;
        font-size: 40px;
        padding: 15px;
        border-radius: 10px;
    }
    p {
        color: grey;
        text-align: center;
        font-size: 18px;
    }
    div.stButton > button {
        color: white;
       
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color: black;'>Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p>Convert units of length, weight, temperature, speed, and time.</p>", unsafe_allow_html=True)

# Select Unit Type
unit_type = st.selectbox("Select a category:", ["Length", "Weight", "Temperature", "Speed", "Time"], index=0)

# Define unit options based on type
unit_options = {
    "Length": ["m", "cm", "km", "inch"],
    "Weight": ["kg", "g", "lb"],
    "Temperature": ["C", "F", "K"],
    "Speed": ["m/s", "km/h", "mph"],
    "Time": ["sec", "min", "hr"]
}

# Get user input
st.markdown("<div class='main'>", unsafe_allow_html=True)
value = st.number_input("Enter value:", min_value=0.0, step=0.1)
from_unit = st.selectbox("From:", unit_options[unit_type])
to_unit = st.selectbox("To:", unit_options[unit_type])

# Convert button
if st.button("Convert", key="convert_button", help="Click to convert" ):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"Converted Value: {result} {to_unit}")
st.markdown("</div>", unsafe_allow_html=True)
# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #999;'>Made with ❤️ by Rameen Rashid</p>", unsafe_allow_html=True)

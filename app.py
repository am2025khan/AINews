import streamlit as st
import pandas as pd

# Simulated data - in real use, replace with live data
alerts = [
    {"symbol": "BANKNIFTY", "type": "CALL", "action": "BUILDING", "strike": 47000, "change_oi": 34000},
    {"symbol": "TATASTEEL", "type": "PUT", "action": "SHEDDING", "strike": 1300, "change_oi": -22000},
    {"symbol": "RELIANCE", "type": "CALL", "action": "SHEDDING", "strike": 2800, "change_oi": -15000},
]

st.set_page_config(page_title="F&O OI Alert Bot", layout="centered")

st.title("📈 F&O OI Alert Bot Dashboard")
st.write("This dashboard shows real-time or simulated OI building/shedding alerts for Indian F&O stocks.")

# Display table
df = pd.DataFrame(alerts)
st.dataframe(df)

# Filter section
st.sidebar.header("🔍 Filter")
symbol = st.sidebar.text_input("Symbol")
if symbol:
    filtered_df = df[df["symbol"].str.contains(symbol.upper())]
    st.dataframe(filtered_df)

import streamlit as st
import requests

st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detection")
st.markdown("Enter a **news headline** below to check if it's real or fake.")

title_input = st.text_input("News Headline", "")

if st.button("Check"):
    if title_input.strip() == "":
        st.warning("Please enter a headline.")
    else:
        try:
            res = requests.post("http://127.0.0.1:5000/predict", json={"title": title_input})
            result = res.json().get("prediction", "Error in response")
            if "real" in result.lower():
                st.success("✅ " + result)
            else:
                st.error("🚫 " + result)
        except Exception as e:
            st.error("Failed to connect to backend. Make sure Flask is running.")

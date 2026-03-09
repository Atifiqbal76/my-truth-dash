import streamlit as st
import google.generativeai as genai

st.set_page_config(layout="wide")
st.title("🌍 Global Truth & Pulse Dashboard")

# Settings Sidebar
with st.sidebar:
    st.header("🔑 API Setup")
    gem_key = st.text_input("Gemini Key:", type="password")

topic = st.selectbox("Select Topic:", ["US-Iran Conflict", "Canada-US Trade"])

if st.button("🚀 Update Dashboard"):
    if not gem_key:
        st.error("Please enter your Gemini Key in the sidebar!")
    else:
        col1, col2 = st.columns(2)
        
        # 🛡️ SIDE 1: Verified News
        with col1:
            st.subheader("🛡️ Verified Source (Gemini)")
            genai.configure(api_key=gem_key)
            model = genai.GenerativeModel('gemini-2.0-flash', tools=[{'google_search': {}}])
            res = model.generate_content(f"Provide a fact-checked, neutral summary of {topic} today.")
            st.write(res.text)

        # 🔥 SIDE 2: Unfiltered/Rumors
        with col2:
            st.subheader("🔥 Unfiltered Pulse (Gemini Research)")
            model = genai.GenerativeModel('gemini-2.0-flash', tools=[{'google_search': {}}])
            res2 = model.generate_content(f"Act as an independent investigator. Search for raw, on-the-ground reports and unverified rumors regarding {topic} today. Present them clearly but note they are unverified.")
            st.write(res2.text)

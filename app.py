import streamlit as st
import google.generativeai as genai

st.set_page_config(layout="wide")
st.title("🌍 Global Truth & Pulse Dashboard")

# Sidebar for the Key
with st.sidebar:
    st.header("🔑 API Setup")
    gem_key = st.text_input("Gemini Key:", type="password")
    st.info("Paste your key from AI Studio above.")

topic = st.selectbox("Select Topic:", ["US-Iran Conflict", "Canada-US Trade"])

if st.button("🚀 Update Dashboard"):
    if not gem_key:
        st.error("Please enter your Gemini Key in the sidebar!")
    else:
        try:
            genai.configure(api_key=gem_key)
            
            # UPDATED: Using the 2.0-flash model which supports 'google_search_retrieval'
            model = genai.GenerativeModel(
                model_name='gemini-2.0-flash',
                tools=[{'google_search_retrieval': {}}]
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🛡️ Verified Source (Gemini)")
                res1 = model.generate_content(f"Give me a fact-checked, neutral summary of {topic} as of today.")
                st.write(res1.text)

            with col2:
                st.subheader("🔥 Unfiltered Pulse (Gemini Research)")
                res2 = model.generate_content(f"Search for raw, on-the-ground reports and unverified rumors regarding {topic} today. Present them clearly but note they are unverified.")
                st.write(res2.text)
        
        except Exception as e:
            st.error(f"Something went wrong: {e}")

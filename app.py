Python


import streamlit as st
import google.generativeai as genai
import openai

st.set_page_config(layout="wide")
st.title("🌍 Global Truth & Pulse Dashboard")

# Settings Sidebar
with st.sidebar:
    st.header("🔑 API Setup")
    gem_key = st.text_input("Gemini Key:", type="password")
    grok_key = st.text_input("Grok Key (Optional):", type="password")

topic = st.selectbox("Select Topic:", ["US-Iran Conflict", "Canada-US Trade"])

if st.button("🚀 Update Dashboard"):
    if not gem_key:
        st.error("Please enter your Gemini Key in the sidebar!")
    else:
        col1, col2 = st.columns(2)
        
        # 🛡️ SIDE 1: GOOGLE GEMINI (Verified)
        with col1:
            st.subheader("🛡️ Verified Source (Gemini)")
            genai.configure(api_key=gem_key)
            model = genai.GenerativeModel('gemini-1.5-flash', tools=[{'google_search': {}}])
            res = model.generate_content(f"Provide a fact-checked, neutral summary of {topic} today.")
            st.write(res.text)

        # 🔥 SIDE 2: GROK (Real-time X Sentiment)
        with col2:
            st.subheader("🔥 Live Pulse (Grok/X)")
            if grok_key:
                client = openai.OpenAI(api_key=grok_key, base_url="https://api.x.ai/v1")
                res2 = client.chat.completions.create(
                    model="grok-4.1-fast",
                    messages=[{"role": "user", "content": f"What is the latest unfiltered sentiment on X regarding {topic}?"}]
                )
                st.write(res2.choices[0].message.content)
            else:
                st.info("Grok key not provided. Showing verified news only.")

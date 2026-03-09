import streamlit as st
import google.generativeai as genai

st.set_page_config(layout="wide")
st.title("🌍 Global Truth & Pulse Dashboard")

# --- SIDEBAR SETUP ---
with st.sidebar:
    st.header("🔑 API Setup")
    
    # This 'key' argument tells Streamlit to remember the input
    gem_key = st.text_input("Gemini Key:", type="password", key="my_api_key")
    
    st.info("Your key is now remembered for this session!")
    st.markdown("---")
    st.write("Targeting: Unbiased & Unfiltered News")

# --- MAIN DASHBOARD ---
topic = st.selectbox("Select Topic:", ["US-Iran Conflict", "Canada-US Trade"])

if st.button("🚀 Update Dashboard"):
    if not gem_key:
        st.error("Please enter your Gemini Key in the sidebar!")
    else:
        try:
            genai.configure(api_key=gem_key)
            
            # Using FLASH-LITE for better reliability on Free Tier
            model = genai.GenerativeModel(
                model_name='gemini-2.0-flash-lite',
                tools=[{'google_search_retrieval': {}}]
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🛡️ Verified Source (Gemini)")
                with st.spinner("Searching official reports..."):
                    res1 = model.generate_content(f"Provide a fact-checked, neutral summary of {topic} as of today.")
                    st.write(res1.text)

            with col2:
                st.subheader("🔥 Unfiltered Pulse (Gemini Research)")
                with st.spinner("Searching for raw reports..."):
                    res2 = model.generate_content(f"Search for raw, on-the-ground reports and unverified rumors regarding {topic} today. Present them clearly but note they are unverified.")
                    st.write(res2.text)
        
        except Exception as e:
            if "429" in str(e):
                st.error("Too many requests! Please wait 60 seconds and try again.")
            else:
                st.error(f"Something went wrong: {e}")

import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Real Estate Agent", page_icon="🏠", layout="wide")

st.title("🏠 Real Estate AI Calling Agent")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Make a Call")
    
    customer_name = st.text_input("Customer Name")
    phone_number = st.text_input("Phone Number", placeholder="+1234567890")
    
    if st.button("📞 Call Now", type="primary"):
        if phone_number:
            with st.spinner("Initiating call..."):
                response = requests.post(
                    f"{API_URL}/call",
                    json={
                        "phone_number": phone_number,
                        "customer_name": customer_name
                    }
                )
                result = response.json()
                
                if "id" in result:
                    st.success(f"Call initiated! ID: {result['id']}")
                else:
                    st.error(f"Error: {result}")
        else:
            st.warning("Please enter a phone number")

with col2:
    st.subheader("Call Logs")
    
    if st.button("🔄 Refresh Logs"):
        with st.spinner("Loading..."):
            response = requests.get(f"{API_URL}/logs")
            logs = response.json()
            
            if isinstance(logs, list) and len(logs) > 0:
                for log in logs[:10]:
                    with st.expander(f"Call - {log.get('id', 'N/A')[:8]}..."):
                        st.write(f"Status: {log.get('status', 'N/A')}")
                        st.write(f"Duration: {log.get('duration', 'N/A')} sec")
                        st.write(f"Started: {log.get('startedAt', 'N/A')}")
            else:
                st.info("No calls yet")

st.markdown("---")
st.caption("Powered by Vapi AI + Gemini")
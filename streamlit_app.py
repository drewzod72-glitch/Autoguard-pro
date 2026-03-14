import streamlit as st

# --- CONFIGURATION & SECURITY ---
st.set_page_config(page_title="AutoGuard Virtual & Aviator", layout="centered")

# Session State Initialization
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'history' not in st.session_state:
    st.session_state.history = []

# --- LOGIN SYSTEM ---
if not st.session_state.authenticated:
    st.title("🛡️ AutoGuard Access")
    access_key = st.text_input("Enter Unique Access Key:", type="password")
    if st.button("Login"):
        if access_key == "master001": 
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid Key.")
    st.stop()

# --- MAIN APP ---
st.title("🚀 Virtual & Aviator Pro")
tab1, tab2 = st.tabs(["⚽ 30s Virtual", "✈️ Aviator"])

with tab1:
    st.subheader("Goal Pattern Tracker")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("OVER 1.5"):
            st.session_state.history.append("OVER")
    with col2:
        if st.button("UNDER 1.5"):
            st.session_state.history.append("UNDER")
    
    if len(st.session_state.history) >= 3:
        last_three = st.session_state.history[-3:]
        if last_three == ["UNDER", "UNDER", "UNDER"]:
            st.success("🎯 ADVICE: BET OVER 1.5")
        elif last_three == ["OVER", "OVER", "OVER"]:
            st.warning("⚠️ ADVICE: WAIT")
        else:
            st.info("📊 ADVICE: NEUTRAL")

with tab2:
    st.subheader("Aviator Watcher")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("PINK (2.0x+)"):
            st.session_state.history.append("PINK")
    with c2:
        if st.button("BLUE (<2.0x)"):
            st.session_state.history.append("BLUE")

    if len(st.session_state.history) >= 3:
        last_three_av = st.session_state.history[-3:]
        if last_three_av == ["BLUE", "BLUE", "BLUE"]:
            st.success("💎 ADVICE: HIGH PINK CHANCE")
        else:
            st.info("⚖️ ADVICE: SAFE ENTRIES")

if st.sidebar.button("Reset Session"):
    st.session_state.history = []
    st.rerun()

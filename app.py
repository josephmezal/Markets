import streamlit as st

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="Live Markets Video Dashboard By Joseph Meza",
    page_icon="📺",
    layout="wide"
)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📊 Live Streams")
st.sidebar.markdown(
    """
    **Click-to-play YouTube LIVE streams**

    Optimized for:
    - iPhone Safari
    - Streamlit Cloud
    - Live market monitoring
    """
)

# ---------------------------
# Main title
# ---------------------------
st.title("📺 Live YouTube Streams Dashboard")
st.markdown(
    """
    ⚠️ **Usuarios de iPhone:**  
    Apple bloquea reproduccion automatica.  
    **Accione el boton de play para cada video.**
    """
)

st.markdown("---")

# ---------------------------
# Spanish Stream
# ---------------------------
st.subheader("🇪🇸 Spanish – Live Stream")

if st.button("▶️ Click to Play (Spanish Stream)"):
    st.video("https://www.youtube.com/watch?v=ViTHPE5yryI")

st.markdown("---")

# ---------------------------
# English Stream
# ---------------------------
st.subheader("🇺🇸 English – Live Stream")

if st.button("▶️ Click to Play (English Stream)"):
    st.video("https://www.youtube.com/watch?v=KQp-e_XQnDE")

st.markdown("---")

# ---------------------------
# BTC Stream
# ---------------------------
st.subheader("₿ Bitcoin (BTC) – Live Stream")

if st.button("▶️ Click to Play (BTC Stream)"):
    st.video("https://www.youtube.com/watch?v=SpsoOVC56xc")

st.markdown("---")

# ---------------------------
# Solana Stream
# ---------------------------
st.subheader("🟣 Solana – Live Stream")

if st.button("▶️ Click to Play (Solana Stream)"):
    st.video("https://www.youtube.com/watch?v=CF2SVyV8A4I")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption(
    "Market Dashboard • Live YouTube Streams • iOS Safari Compatible"
)

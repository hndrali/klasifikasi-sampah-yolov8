# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="SATRIA (Smart Trash IoT for Advanced Waste Management)",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("🤖 SATRIA 🌎")
st_notif = st.empty()
st_notif.info("Masukkan sampah untuk dikelompokkan. Alat akan mendeteksi secara otomatis", icon="🚮", width="stretch")


# Sidebar
st.sidebar.header("SATRIA")
st.sidebar.subheader("MAN 2 Kudus")
st.sidebar.text("Tempat Sampah Pintar Berbasis IoT dengan Sistem Pemilah Otomatis, Pengomposan Cepat, dan Monitoring Real-Time untuk Pengelolaan Sampah Berkelanjutan dengan media Telegram apps")

confidence = 40/ 100
model_path = Path(settings.DETECTION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

# elif source_radio == settings.WEBCAM: 
helper.play_webcam(confidence, model, st_notif)

# else:
    # st.error("Please select a valid source type!")
# 


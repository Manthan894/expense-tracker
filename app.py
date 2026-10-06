import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Expense Tracker", page_icon="💰")

st.title("💰 Expense Tracker")
st.write("A simple expense tracker app for Android (college mini project).")

apk_path = Path("app-debug.apk")

if apk_path.exists():
    with open(apk_path, "rb") as f:
        st.download_button(
            label="⬇️ Download APK",
            data=f,
            file_name="expense-tracker.apk",
            mime="application/vnd.android.package-archive",
        )
else:
    st.error("APK file not found in the repository.")

st.subheader("How to install")
st.markdown("""
1. Download the APK on your Android phone.
2. Open it and allow **Install from unknown sources** when asked.
3. Tap **Install**.
""")

st.caption("This is a debug build, so your phone may show a Play Protect warning.")

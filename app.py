import streamlit as st
from a3d.utilities.u_appcore import AppCoreUtilities


st.set_page_config(page_title="A3D Streamlit Template", page_icon="🛠️")

def main():
    appcore = AppCoreUtilities()
    # Load the satrt view dynamically
    if st.session_state['appState'] == "🐣 Start":
        klass = appcore.loadModule("a3d.views.v_start", "StartView")
        klass() 


if __name__ == "__main__":
    main()
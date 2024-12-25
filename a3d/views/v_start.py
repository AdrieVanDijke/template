import streamlit as st
from a3d.utilities.u_appcore import AppCoreUtilities
from a3d.controlers.c_start import StartControler


class StartView:
    def __init__( self ):
        self.appcore = AppCoreUtilities()
        self.controler = StartControler()        
        self.buildView()


    # VIEWS =========================================
    def buildView( self ):
        self.buildSidebarView()
        self.buildMainView()


    def buildSidebarView( self ):
        st.markdown(
            """
            <style>
                section[data-testid="stSidebar"] {
                    width: 450px !important;
                    text-align: center;
                }              
            </style>
            """,
            unsafe_allow_html=True  
        )
        
        with st.sidebar:            
            option = st.selectbox(
                "Select a Module",
                ("🐣 Start"),
            )
            # Als de pagina staat niet gelijk is aan de optie, zet de pagina staat en rerun
            if st.session_state['appState'] != option:
                self.controler.reset()
                self.appcore.setAppState(option)
                st.rerun()

            if st.button("🆕 New"):
                self.controler.reset()


    def buildMainView(self):
        st.markdown(
            """
            A3D Streamlit Template
            """,
            unsafe_allow_html=True  
        )

        with st.container():
            st.title("A3D Streamlit Template")
            st.write(self.controler.run())
            st.write("This is the main view")

    # WORKERS =======================================  




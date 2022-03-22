import app1
import app2
import app3
import streamlit as st

st.set_page_config(
    page_title = ' Supermarket sales analysis',
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state = 'expanded'
)

PAGES = {
    "Pendahuluan": app1,
    "Visualisasi": app2,
    "Hipotesis": app3
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
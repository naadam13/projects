import streamlit as st
import requests

def app():
    URL = 'https://naadam-batch07-m2p1-backend.herokuapp.com/post'
    st.title("Model Prediction")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        aluminium = st.number_input("aluminium - dangerous if greater than 2.8")
        ammonia = st.number_input("ammonia - dangerous if greater than 32.5")
        arsenic = st.number_input("arsenic - dangerous if greater than 0.01")
        barium = st.number_input("barium - dangerous if greater than 2")
        cadmium = st.number_input("cadmium - dangerous if greater than 0.005")
    with col2:
        chloramine = st.number_input("chloramine - dangerous if greater than 4")
        chromium = st.number_input("chromium - dangerous if greater than 0.1")
        copper = st.number_input("copper - dangerous if greater than 1.3")
        flouride = st.number_input("flouride - dangerous if greater than 1.5")
        bacteria = st.number_input("bacteria - dangerous if greater than 0")
    with col3:
        viruses = st.number_input("viruses - dangerous if greater than 0")
        lead = st.number_input("lead - dangerous if greater than 0.015")
        nitrates = st.number_input("nitrates - dangerous if greater than 10")
        nitrites = st.number_input("nitrites - dangerous if greater than 1")
        mercury = st.number_input("mercury - dangerous if greater than 0.002")
    with col4:
        perchlorate = st.number_input("perchlorate - dangerous if greater than 56")
        radium = st.number_input("radium - dangerous if greater than 5")
        selenium = st.number_input("selenium - dangerous if greater than 0.5")
        silver = st.number_input("silver - dangerous if greater than 0.1")
        uranium = st.number_input("uranium - dangerous if greater than 0.3")

    # Parameter input
    #URL = URL + f"?aluminium={aluminium}&ammonia={ammonia}&arsenic={arsenic}&barium={barium}&cadmium={cadmium}&chloramine={chloramine}&chromium={chromium}&copper={copper}&flouride={flouride}&bacteria={bacteria}&viruses={viruses}&lead={lead}&nitrates={nitrates}&nitrites={nitrites}&mercury={mercury}&perchlorate={perchlorate}&radium={radium}&selenium={selenium}&silver={silver}&uranium={uranium}"
    data = {'aluminium':aluminium, 'ammonia':ammonia, 'arsenic':arsenic,
            'barium':barium, 'cadmium':cadmium, 'chloramine':chloramine,
            'chromium':chromium, 'copper':copper, 'flouride':flouride,
            'bacteria':bacteria, 'viruses':viruses, 'lead':lead,
            'nitrates':nitrates, 'nitrites':nitrites, 'mercury':mercury,
            'perchlorate':perchlorate, 'radium':radium, 'selenium':selenium,
            'silver':silver, 'uranium':uranium}
    
    # Komunikasi
    #r = requests.get(URL)
    r = requests.post(URL, json=data)
    pred = r.json()
    
    if st.button('Show prediction'):
        st.write(pred['data']['Prediction'])
import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('Water Quality Prediction')
    st.write('Program ini akan menganalisis data kualitas air di suatu lingkungan perkotaan.')
    st.write('Dataset dapat diunduh di https://www.kaggle.com/mssmartypants/water-quality')
    if st.checkbox('Show dataframe'):
        df = pd.read_csv("waterQuality1.csv")
        st.write(df)
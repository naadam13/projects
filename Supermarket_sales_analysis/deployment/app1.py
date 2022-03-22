import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('Supermarket sales analysis')
    st.write('Program ini akan menganalisis data penjualan suatu supermarket di Myanmar.')
    st.write('Dataset dapat diunduh di https://www.kaggle.com/aungpyaeap/supermarket-sales')
    if st.checkbox('Show dataframe'):
        df = pd.read_csv("supermarket_sales - Sheet1.csv")
        st.write(df)
        
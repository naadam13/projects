import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('Exploratory Data Analysis')
    df = pd.read_csv("waterQuality1.csv")
    df['ammonia'] = pd.to_numeric(df['ammonia'], errors = 'coerce')
    df['is_safe'] = pd.to_numeric(df['is_safe'], errors = 'coerce')
    st.subheader('Statistika deskriptif tentang dataset:')
    st.write(df.describe())
    with st.expander("Lihat penjelasan"):
        st.write('Pada deskriptif statistik di atas terlihat bahwa hanya nilai minimum "ammonia" yang bernilai negatif.')
        st.write('Berdasarkan situs https://www.researchgate.net/post/Is-it-possible-to-have-negative-NH3-concentration-from-samples-taken-from-the-field-where-NH3-volatilization-was-measured diketahui bahwa hal ini dapat disebabkan oleh kesalahan dalam pengambilan data. Data negatif tersebut tetap dapat dianggap sebagai nilai minimum.')
    st.subheader('Plot persebaran data tiap kolom:')
    option = st.selectbox('Pilih kolom:', ('aluminium', 'ammonia', 'arsenic', 'barium', 'cadmium', 'chloramine', 
                'chromium', 'copper', 'flouride', 'bacteria', 'viruses', 'lead',
                'nitrates', 'nitrites', 'mercury', 'perchlorate', 'radium',
                'selenium', 'silver', 'uranium', 'is_safe'))
    fig1, ax1 = plt.subplots(figsize=(10,5))
    sns.histplot(df[option], ax=ax1)
    plt.title('Histogram')
    st.write(fig1)
    fig2, ax2 = plt.subplots(figsize=(10,5))
    sns.boxplot(y=df[option], ax=ax2)
    plt.title('Boxplot')
    st.write(fig2)
    st.write('Skewness value for', option, ": ", df[option].skew())
    with st.expander("Lihat penjelasan"):
        st.markdown('_Skewness Value_ menunjukkan apakah data tersebut terdistribusi normal/Gaussian atau _skewed_. Data yang terdistribusi secara normal/Gaussian memiliki rentang -0.5 <= _Skewness Value_ <= 0.5 dan sisanya merupakan data yang terdistribusi secara _skewed_. Metode untuk menentukan _outlier_ pada kedua tipe data tersebut berbeda.')
    st.subheader('Plot persebaran data antar tiap kolom:')
    option1 = st.selectbox('Pilih kolom pertama:', ('aluminium', 'ammonia', 'arsenic', 'barium', 'cadmium', 'chloramine', 
                'chromium', 'copper', 'flouride', 'bacteria', 'viruses', 'lead',
                'nitrates', 'nitrites', 'mercury', 'perchlorate', 'radium',
                'selenium', 'silver', 'uranium', 'is_safe'))
    option2 = st.selectbox('Pilih kolom kedua:', ('aluminium', 'ammonia', 'arsenic', 'barium', 'cadmium', 'chloramine', 
                'chromium', 'copper', 'flouride', 'bacteria', 'viruses', 'lead',
                'nitrates', 'nitrites', 'mercury', 'perchlorate', 'radium',
                'selenium', 'silver', 'uranium', 'is_safe'))
    fig3, ax3 = plt.subplots(figsize=(10,5))
    sns.scatterplot(data=df, x=option1, y=option2, ax=ax3)
    plt.title('Scatter plot')
    st.write(fig3)
    corr = df[option1].corr(df[option2])
    st.write('Correlation value between', option1, 'and', option2, ':', corr)
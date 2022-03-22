import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('Visualisasi')
    st.write('Visualisasi yang akan ditunjukkan adalah statistik mengenai penjualan produk yang dibeli oleh member.')

    df = pd.read_csv("supermarket_sales - Sheet1.csv")
    df_stream = df.copy()
    df_stream = df_stream[(df_stream["Customer type"] == "Member")]

    if st.checkbox('Visualisasi mengenai kuantitas penjualan produk'):
        df_stream1 = df_stream[["Product line", "Quantity"]].groupby(["Product line"]).sum()
        st.write('Kuanititas penjualan produk:')
        df_stream1_1 = df_stream1.reset_index()
        st.write(df_stream1_1)
        fig1, ax1 = plt.subplots(figsize=(20,8))
        ax1.barh(df_stream1_1['Product line'], df_stream1_1['Quantity'])
        st.pyplot(fig1)
        
        df_stream2_1 = df_stream.copy()
        df_stream2_1 = df_stream2_1.drop(['Invoice ID', 'Branch', 'Customer type', 'Gender', 'Unit price', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating'], axis=1)
        df_stream2_2 = df_stream2_1.pivot_table(index='City', columns='Product line', values='Quantity', aggfunc=np.sum)
        st.write('Kuanititas penjualan produk berdasarkan kota:')
        st.write(df_stream2_2)
        
        label2_2 = list(df_stream2_2.index)
        x2_2 = np.arange(len(label2_2))
        y2_2_1 = df_stream2_2['Electronic accessories']
        y2_2_2 = df_stream2_2['Fashion accessories']
        y2_2_3 = df_stream2_2['Food and beverages']
        y2_2_4 = df_stream2_2['Health and beauty']
        y2_2_5 = df_stream2_2['Home and lifestyle']
        y2_2_6 = df_stream2_2['Sports and travel']
        with plt.style.context('seaborn'):
            fig2, ax2 = plt.subplots(figsize=(20,8))
            ax2.bar(x2_2 + 0, y2_2_1, width = 0.1, label = 'Electronic accessories')
            ax2.bar(x2_2 + 0.1, y2_2_2, width = 0.1, label = 'Fashion accessories')
            ax2.bar(x2_2 + 0.2, y2_2_3, width = 0.1, label = 'Food and beverages')
            ax2.bar(x2_2 + 0.3, y2_2_4, width = 0.1, label = 'Health and beauty')
            ax2.bar(x2_2 + 0.4, y2_2_5, width = 0.1, label = 'Home and lifestyle')
            ax2.bar(x2_2 + 0.5, y2_2_6, width = 0.1, label = 'Sports and travel')
            ax2.set_xlabel('City')
            ax2.set_ylabel('Quantity')
            ax2.set_xticks(x2_2 + 0.25)
            ax2.set_xticklabels(label2_2)
            ax2.set_title('Quantity By Product line')
            plt.legend()
            st.pyplot(fig2)

    if st.checkbox('Visualisasi mengenai rata-rata pendapatan kotor dari penjualan produk'):
        df_stream3 = df_stream[["Product line", "gross income"]].groupby(["Product line"]).mean()
        st.write('Rata-rata pendapatan kotor dari penjualan produk:')
        df_stream3_1 = df_stream3.reset_index()
        st.write(df_stream3_1)
        fig3, ax3 = plt.subplots(figsize=(20,8))
        ax3.barh(df_stream3_1['Product line'], df_stream3_1['gross income'])
        st.pyplot(fig3)
        
        df_stream4_1 = df_stream.copy()
        df_stream4_1 = df_stream4_1.drop(['Invoice ID', 'Branch', 'Customer type', 'Gender', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'Rating'], axis=1)
        df_stream4_2 = df_stream4_1.pivot_table(index='City', columns='Product line', values='gross income')
        st.write('Rata-rata pendapatan kotor dari penjualan produk berdasarkan kota:')
        st.write(df_stream4_2)
    
        label4_2 = list(df_stream4_2.index)
        x4_2 = np.arange(len(label4_2))
        y4_2_1 = df_stream4_2['Electronic accessories']
        y4_2_2 = df_stream4_2['Fashion accessories']
        y4_2_3 = df_stream4_2['Food and beverages']
        y4_2_4 = df_stream4_2['Health and beauty']
        y4_2_5 = df_stream4_2['Home and lifestyle']
        y4_2_6 = df_stream4_2['Sports and travel']
        with plt.style.context('seaborn'):
            fig4, ax4 = plt.subplots(figsize=(20,8))
            ax4.bar(x4_2 + 0, y4_2_1, width = 0.1, label = 'Electronic accessories')
            ax4.bar(x4_2 + 0.1, y4_2_2, width = 0.1, label = 'Fashion accessories')
            ax4.bar(x4_2 + 0.2, y4_2_3, width = 0.1, label = 'Food and beverages')
            ax4.bar(x4_2 + 0.3, y4_2_4, width = 0.1, label = 'Health and beauty')
            ax4.bar(x4_2 + 0.4, y4_2_5, width = 0.1, label = 'Home and lifestyle')
            ax4.bar(x4_2 + 0.5, y4_2_6, width = 0.1, label = 'Sports and travel')
            ax4.set_xlabel('City')
            ax4.set_ylabel('Gross Income Mean')
            ax4.set_xticks(x4_2 + 0.25)
            ax4.set_xticklabels(label4_2)
            ax4.set_title('Gross Income Mean By Product line')
            plt.legend()
            st.pyplot(fig4)
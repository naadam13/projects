import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def app():
    st.title('Hipotesis')
    st.write('Hipotesis yang akan ditunjukkan adalah pengujian hipotesis mengenai signifikansi perbedaan pendapatan kotor dari penjualan produk yang dibeli oleh member.')
    if st.checkbox('Hipotesis mengenai signifikansi perbedaan pendapatan kotor antara "Food and beverages" dengan "Health and beauty"'):
        df = pd.read_csv("supermarket_sales - Sheet1.csv")
        df_stream = df.copy()
        df_stream = df_stream[(df_stream["Customer type"] == "Member")]
        df_stream.rename(columns={"gross income":"gross_income"}, inplace=True)

        st.write('Berdasarkan data kuantitas penjualan produk,')

        df_stream1 = df_stream[["Product line", "Quantity"]].groupby(["Product line"]).sum()
        df_stream1_1 = df_stream1.reset_index()

        st.write(df_stream1_1)

        st.write('didapat bahwa "Food and beverages" merupakan jenis produk yang paling banyak terjual dan "Health and beauty" merupakan produk yang paling sedikit terjual, dan terdapat selisih yang cukup besar diantara keduanya.')

        st.write('Jika dilihat berdasarkan rata-rata pendapatan kotornya,')

        df_stream3 = df_stream[["Product line", "gross_income"]].groupby(["Product line"]).mean()
        df_stream3_1 = df_stream3.reset_index()
    
        st.write(df_stream3_1)

        st.write('didapat bahwa nilai rata-rata pendapatan kotor yang dihasilkan oleh "Food and beverages" tidak jauh berbeda dengan yang dihasilkan oleh "Health and beauty".')

        st.write('Pengujian hipotesis yang dilakukan menggunakan metode **"Two Samples Independent Two Tailed Hypothesis Testing"** dengan hipotesis')
        st.write('**H0: μ_food_and_beverages = μ_health_and_beauty**')
        st.write('**H1: μ_food_and_beverages != μ_health_and_beauty**')
        st.write('dimana')
        st.write('**μ_food_and_beverages** = 15.8853')
        st.write('**μ_health_and_beauty** = 16.8500.')

        st.markdown('#')

        st.write('Hasil dari hipotesis menghasilkan')
        df_hb = df_stream[df_stream['Product line'] == 'Health and beauty'][['Invoice ID','gross_income']].groupby('Invoice ID').sum()
        df_fb = df_stream[df_stream['Product line'] == "Food and beverages"][['Invoice ID','gross_income']].groupby('Invoice ID').sum()
        t_stat, p_val = stats.ttest_ind(df_hb,df_fb)
        st.write('P-value:',p_val[0])
        st.write('t-statistics:',t_stat[0])
        image = Image.open('output.png')
        st.image(image, caption='Grafik "Two Samples Independent Two Tailed Hypothesis Testing" mengenai signifikansi perbedaan pendapatan kotor antara "Food and beverages" dengan "Health and beauty".')

        st.write("""
                Kesimpulan:
                - Distribusi kedua data yang diuji merupakan distribusi normal.
                - **H0** dapat diterima, yang berarti tidak ada perbedaan signifikan antara rata-rata pendapatan kotor "Food and beverages" dengan rata-rata pendapatan kotor "Health and beauty". Hal ini karena:
                    - P-value jauh lebih besar dibandingkan critical value (0.05).
                    - Garis "Alternative Hypothesis" berada di dalam jangkauan garis "Confidence threshold".
                """)
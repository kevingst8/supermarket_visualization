# -*- coding: utf-8 -*-
"""h8dsft_Milestone1_kevin_gusti_arswendy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c4d8HbQPRfavtEs6hFA7vmr_hIEU0GMR
"""

import streamlit as st
import pandas as pd
from google.colab import drive
from google.colab import files

data = pd.read_csv('supermarket_sales.csv')
data

def main():
  st.title('Visualisasi Data Supermarket Sales')
  st.subheader('Data Supermarket Sales')
  st.write(data)
  st.subheader('Grafik Jumlah Penjualan per Kategori Produk')
  chart_data = data['Product line'].value_counts()
  st.bar_chart(chart_data)
if __name__ == '__main__':
  main()
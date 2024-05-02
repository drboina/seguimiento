import pandas as pd
import streamlit as st
import openpyxl

st.image("images/sonora.png")

st.sidebar.image("images/coord.png")

option = st.sidebar.selectbox("Menu",('Avance Presupuestal','Presupuesto','Ordenes de pago','Minutario','Adquisiciones'))

st.header(option)

if option == 'Avance Presupuestal':
    st.title("Sistema del Avance Presupuestal del Ejecutivo del Estado")
    st.markdown ('___________________________________________________')

    st.subheader("Presupuesto de Egresos Aprobado")

    df=pd.read_excel("data/aprobado.xlsx")
    p=df["Centro gestor"].groupby(by=["Per.Presup"]).sum()    
    st.dataframe(p)
    
  

    





if option == 'Presupuesto':
    st.subheader("Presupuesto de Egresos 2024")
    
    
     
if option == 'Ordenes de pago':
    st.subheader("Status de Ordenes de pago")

if option == 'Minutario':
    st.subheader("Control de Oficios de la Coordinación Ejecutiva de Administración y Finanzas")

if option == 'Adquisiciones':
    st.subheader("Reporte de Adquisiciones 2024")


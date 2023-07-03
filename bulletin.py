import streamlit as st
import pandas as pd
from millify import millify

st.set_page_config(page_title="Performance",layout="wide")

st.title("Report Performance Card")
uploaded_file = st.file_uploader("File",type=["xlsx"])
a = 1
if uploaded_file is not None:
    file_name = uploaded_file.name 
    
        
    if "21TO" in file_name :
        a = 0
    excel_data = pd.read_excel(uploaded_file,sheet_name=None)
    with st.expander("Informations"):
        st.write(uploaded_file.name)
        for sheet_name in excel_data.keys():
            
            st.write(sheet_name,"rows:",excel_data[sheet_name].shape[0],"columns:",excel_data[sheet_name].shape[1])
    
    with st.expander("dataframe"):
        sheet_names = list(excel_data.keys())
        sheet_name = st.selectbox("select a sheet",sheet_names)
        
        st.dataframe(excel_data[sheet_name])
    
    
    if a == 1:
        st.metric("Assiette",millify(excel_data["IND2"]["ASSIETTE"].str.replace(",","_").astype("float").sum()))
        st.metric("Tax",millify(excel_data["IND2"]["TAX"].str.replace(",","_").astype("float").sum()))
    else:
        st.metric("Assiette",millify(excel_data["IND4"]["ASSIETTE"].str.replace(",","_").astype("float").sum()))
        st.metric("Tax",millify(excel_data["IND4"]["TAX"].str.replace(",","_").astype("float").sum()))
        
    cuo = st.radio("Custom office",["21TO","CDL"],horizontal=False,index=a)

if st.button("Download"):
    st.write("Press")

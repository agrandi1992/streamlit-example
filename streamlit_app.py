from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import pandas as pd

import io

buffer = io.BytesIO()
c=pd.read_excel("C.xlsx")
ba=pd.read_excel("b.xlsx")
b=c.columns
l=ba.columns

uploaded_file = st.file_uploader("Importer le fichier de la revue d'offre", type="xlsx")
if uploaded_file:
    options = st.multiselect(
    'Choisir les marchés ',
   
    ["MENUISERIES"	,"QUINCAILLERIE",	"COUVERTURE","PANNEAUX"	,"REVÊTEMENTS"	,"AMENAGEMENT EXTERIEUR",	"AMENAGEMENT INTERIEUR",	"MATERIEL ET OUTILLAGE"	,"BOIS DE CONSTRUCTION"	,"PLAFOND, PLATRERIE, ISOLATION",	"SANITAIRE",	"CHAUFFAGE",	"VRD-TP"	,"ELECTRICITE"	,"PLOMBERIE"	,"PEINTURE / DROGUERIE"	,"PRODUITS BETON INDUSTRIALISES",	"CHARPENTES INDUSTRIALISÉES",	"GROS-ŒUVRE"])
    st.write('Marchés:', options) 

    
    df_data = pd.read_excel(uploaded_file,"DATA")
    df_data =df_data.fillna(0)
    df_data=df_data[["Agence","Agence LIB","Fournisseur Appro Principal","Article","Article LIB"]]
    df_data["Article"]=df_data["Article"].apply(str)
    df_data["cle"]=df_data["Agence LIB"]+"-"+df_data["Article"]
    df_data=df_data[["cle","Agence","Agence LIB","Fournisseur Appro Principal","Article","Article LIB"]]
    
    df_gig = pd.read_excel(uploaded_file,"Gigonité")
    df_gig=df_gig.fillna(0)
    
    df_gig=df_gig[l]
    
    df_dmoins = pd.read_excel(uploaded_file,"D-1")
    df_dmoins =df_dmoins .fillna(0)
    df_dmoins=df_dmoins[l]


    df_dpac = pd.read_excel(uploaded_file,"DPAC")
    df_dpac =df_dpac .fillna(0)
    df_dpac=df_dpac[l]
   
    df_dplus = pd.read_excel(uploaded_file,"D+1")
    df_dplus =df_dplus .fillna(0)
    df_dplus=df_dplus[b]
    df_dplus.columns=l


    df_ab = pd.read_excel(uploaded_file,"AB")
    df_ab =df_ab.fillna(0)
    df_ab=df_ab[l]
    df_prop = pd.read_excel(uploaded_file,"PROP")
    df_prop =df_prop.fillna(0)
    df_prop=df_prop[l]

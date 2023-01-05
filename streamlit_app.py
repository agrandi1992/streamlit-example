import streamlit as st
import pandas as pd

import io

buffer = io.BytesIO()
#c=pd.read_excel("C.xlsx")
#ba=pd.read_excel("b.xlsx")
#b=c.columns
#l=ba.columns

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
    
   

    try:
        df_c = pd.read_excel(uploaded_file,"C")
        df_c =df_c.fillna(0)
        df_c=df_c[l]
    except:
        df_c=ba

    df=pd.concat([df_c,df_prop,df_ab,df_dplus,df_dpac,df_dmoins,df_gig])
    df_revue=df[df["Marché"].isin(options)]
     
    df_revue.index=range(len(df_revue))
    df_revue["Decision finale code dispo"]=df_revue["Decision (Par defaut) : Code dispo"]
    df_revue["Decision finale Lien appro"]=df_revue["Decision (Par defaut) : Liens d'appro"]
    for i in range(len(df_revue)): 
        if df_revue["Decisions CM :Codes dispo"][i] !=0:
            df_revue["Decision finale code dispo"][i]=df_revue["Decisions CM :Codes dispo"][i]
           
        elif df_revue["Decisions RAR :Codes dispo"][i] !=0 :
            df_revue["Decision finale code dispo"][i]=df_revue["Decisions RAR :Codes dispo"][i]
            

        elif df_revue["Preconisation CA : Code dispo"][i] !=0 :
            df_revue["Decision finale code dispo"][i]=df_revue["Preconisation CA : Code dispo"][i]
           


    for i in range(len(df_revue)): 
        if df_revue["Decisions CM :Liens appro"][i] !=0:
           
            df_revue["Decision finale Lien appro"][i]=df_revue["Decisions CM :Liens appro"][i]

        elif df_revue["Decisions RAR :Liens appro"][i] !=0 :
            
            df_revue["Decision finale Lien appro"][i]=df_revue["Decisions RAR :Liens appro"][i]

        elif df_revue["Preconisation CA : Liens d'appro"][i] !=0 :
           
            df_revue["Decision finale Lien appro"][i]=df_revue["Preconisation CA : Liens d'appro"][i]

    


    
    
    df_geo=df_revue[["Agence LIB","Article","Decision finale code dispo","Decision finale Lien appro"]]
    df_geo["Decision finale Lien appro"]=df_geo["Decision finale Lien appro"].apply(str)
    df_geo["Article"]=df_geo["Article"].apply(str)
    df_geo["cle"]=df_geo["Agence LIB"]+"-"+df_geo["Article"]
    df_data=df_data[["cle","Agence","Fournisseur Appro Principal","Article LIB"]]
    df_geo=df_geo.merge(df_data,how ='left', on ="cle")
    df_geo=df_geo[["Agence LIB","Agence","Article LIB","Article","Fournisseur Appro Principal","Decision finale code dispo","Decision finale Lien appro"]]
    st.dataframe(df_geo)
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    # Write each dataframe to a different worksheet.
         df_geo.to_excel(writer, sheet_name='Sheet1')
    

    # Close the Pandas Excel writer and output the Excel file to the buffer
         writer.save()

         st.download_button(
           label="Download Excel worksheets",
           data=buffer,
           file_name="pandas_multiple.xlsx",
           mime="application/vnd.ms-excel"
           )

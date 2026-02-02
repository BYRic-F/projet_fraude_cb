
from numpy import test
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import requests
import os
import time

#---------------Configuration de la page 
st.set_page_config(layout="wide")
    
#---------------Fonction carte métrique
def metric_card(label, value, color="#f0f2f6"):
    st.markdown(
        f"""
        <div style="
            background-color: {color};
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #ddd;
            margin-bottom: 10px;">
            <p style="margin: 0; font-size: 14px; color: #555; font-weight: bold;">{label}</p>
            <h2 style="margin: 0; color: black;">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


#------------CSS personnalisé
st.markdown("""
    <style>
    /* Cibler le texte à l'intérieur des onglets */
    .stTabs [data-baseweb="tab"] p {
        font-size: 24px;      /* Modifiez ce chiffre pour la taille */
        font-weight: bold;    /* Optionnel : mettre en gras */
    }
    </style>
    """, unsafe_allow_html=True)

#-----------Page présentation
def page_presentation ():
    
    st.markdown("""
    <style>
    /* Cibler le texte à l'intérieur des onglets */
    .stTabs [data-baseweb="tab"] p {
        font-size: 20px;      /* Modifiez ce chiffre pour la taille */
        font-weight: bold;    /* Optionnel : mettre en gras */
    }
    /* 2. Couleur de l'onglet quand on passe la souris dessus (Hover) */
    .stTabs [data-baseweb="tab"]:hover {
        color: #FF4B4B; /* Le rouge Streamlit ou votre couleur */
    }

    /* 3. Couleur de l'onglet sélectionné (Actif) */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: rgba(255, 75, 75, 0.1); /* Un fond léger rouge */
        border-radius: 10px 10px 0px 0px;
    }
    
    /* 4. La petite barre de soulignement sous l'onglet actif */
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)
    
 

    title = "Présentation du projet"
    st.title(title, text_alignment="center")

    #---------------création des onglets
    onglet_projet, onglet_stack, onglet_eda, onglet_flux_de_donnees, onglet_equipe = st.tabs(["Le Projet", "La Stack", "L'Analyse (EDA)", "Flux de données", "L'Équipe",])
    
    with onglet_projet:
        
        (st.write(""))        
        st.markdown("#### 🎯 <u>Ojectif</u> ", unsafe_allow_html=True)
        st.markdown("##### Concevoir une application de détection de fraudes en temps réel à l'aide du modèle XGBoost à partir de données réelles fournies par une entreprise multinationale sur une période d’un mois. <br><br>", unsafe_allow_html=True)
        
        st.markdown("#### 📊 <u>Dataset et Méthodologie</u>: PaySim (Kaggle)", unsafe_allow_html=True)
        
        col1_dataset, col2_dataset, col3_dataset= st.columns(3)
        with col1_dataset:
            metric_card("Dataframe de base", "6 353 307 rows", color="#d1ecf1")           
        with col2_dataset:
            metric_card("Fraudes identifiées", "8 213", color="#d4edda")
        with col3_dataset:
            metric_card("Taux de fraude", "0.13 %", color="#e0c5d6")
        
        (st.write(""))
        st.markdown("##### 🛠️ Séparation des données historiques pour l'entraînement et le flux temps réel (production)", unsafe_allow_html=True)
                                
        col1, col2, col3 = st.columns(3)
        with col1: 
            metric_card("Dataframe d'entraînement", "5 726 358 rows", color="#d1ecf1")   
            metric_card("Dataframe de production", "636 262 rows", color="#d1ecf1")         
        with col2:
            metric_card("Fraudes identifiées", "4 449", color="#d4edda")
            metric_card("Fraudes identifiées", "3 764", color="#d4edda")
        with col3:
            metric_card("Taux de fraude", "0.07 %", color="#e0c5d6")
            metric_card("Taux de fraude", "0.59 %", color="#e0c5d6")
    
    with onglet_stack:
        
        (st.write(""))   
        st.markdown("#### <u>Stack Technique</u>", unsafe_allow_html=True)
        (st.write("")) 
        (st.write("")) 
    
        col1, col2, col3 = st.columns(3)        
        with col1:
            st.image("fastapi.png", width=140)
            st.markdown("##### *Chef d'orchestre*: Reçoit les flux et interroge le modèle pour prédire la fraude. Une fois la prédiction obtenue, l'API renvoie instantanément le verdict (Fraude ou Sain) au système avant d'envoyer les données vers notre buffer Redis")
            st.image("grafana.png", width=180)
            st.markdown("##### *Monitoring*: Plateforme de monitoring permettant de visualiser en temps réel la santé technique de l'infrastructure. Elle affiche les performances de l'API, l'utilisation des ressources système et l'état des flux de données.")
            (st.write("")) 
            (st.write("")) 
            (st.write("")) 
            (st.write(""))
            st.image("XGBoost.png", width=180)
            st.markdown("##### *Cerveau*:    C'est le Dashboard qui permet de visualiser les résultats en temps réel. Elle transforme nos données complexes en graphiques interactifs, en cartes et en indicateurs clés pour rendre la détection de fraude compréhensible par n'importe quel utilisateur.")
            st.write(" ") # Petit espace verticalA
        with col2:
            st.image("redis.png", width=140)
            st.markdown("##### *Buffer*: Stocke temporairement les données pour fluidifier le passage entre l'API et le Worker. Il fait office de file d'attente pour absorber les pics de charge. Cela garantit qu'aucune transaction n'est perdue, même en cas de fort trafic<br><br>", unsafe_allow_html=True)
            st.image("prometheus.png", width=130)
            st.markdown("##### *Métriques*: C'est la base de données qui collecte et stocke les mesures de performance (temps de réponse, CPU, RAM) envoyées par les différents services. Elle sert de source de données à Grafana pour transformer ces chiffres bruts en graphiques lisibles.")

        with col3:
            st.image("bigquery.png", width=140)
            st.markdown("##### *Cloud*: Archive l'historique des transactions et des prédictions dans le Cloud. Cet outil permet de réaliser des analyses statistiques à grande échelle.<br>", unsafe_allow_html=True)
            st.image("streamlit.png", width=180)
            st.markdown("##### *Vitrine*: Plateforme de monitoring permettant de visualiser en temps réel la santé technique de l'infrastructure. Elle affiche les performances de l'API, l'utilisation des ressources système et l'état des flux de données.")
    
    with onglet_eda:
        st.markdown("#### 📈 <u>Exploratory Data Analysis (EDA)</u><br>", unsafe_allow_html=True)
        st.markdown("##### Voici un résumé des principales découvertes issues de notre analyse exploratoire des données (EDA) sur le dataframe de production :", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image("bar_chart_types.png", width=1000)
            st.markdown("##### 1. Répartition des Fraudes par Type de Transaction", unsafe_allow_html=True)
            st.markdown("Les fraudes sont inégalement réparties selon le type de transaction. Les types 'TRANSFER' et 'CASH_OUT' représentent la majorité des fraudes détectées, suggérant que les fraudeurs privilégient ces méthodes pour leurs activités illicites.<br><br><br><br>", unsafe_allow_html=True)
            st.image("histplot_heures.png", width=1000)
            st.markdown("##### 3. Distribution des Fraudes par Heure de la Journée", unsafe_allow_html=True)
            st.markdown("L'analyse horaire révèle que les fraudes n'ont pas de période spécifique dans la journée. Peut-être en raison de la nature automatisée des attaques, les fraudeurs opèrent à toute heure, rendant la détection basée sur le temps plus complexe.", unsafe_allow_html=True)
        with col2:      
            st.image("pie_chart_fraude.png", width=800)
            st.markdown("##### 2. Proportion de Transactions Frauduleuses", unsafe_allow_html=True)
            st.markdown("Le graphique circulaire montre que les transactions frauduleuses sur les données de productionsconstituent une très faible proportion du total des transactions (0.59%).<br><br><br><br><br>", unsafe_allow_html=True)
            st.image("histogramme_final.png", width=1000)
            st.markdown("##### 4. Montant des fraudes", unsafe_allow_html=True)
            st.markdown("L'histogramme des montants indique que la majorité des fraudes impliquent des montants relativement elevés.", unsafe_allow_html=True)


# 4. L'APPEL DE LA FONCTION (Le déclencheur)
page_presentation()
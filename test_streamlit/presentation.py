
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
    onglet_projet, onglet_stack, onglet_eda, onglet_flux_de_donnees, onglet_equipe = st.tabs(["Le projet", "La Stack", "L'analyse (EDA)", "Flux de données", "L'Équipe",])
    
    with onglet_projet:
        
        (st.write(""))  
        col1title, col2title, col3title = st.columns([4.5,6,1])
        with col2title:
            st.markdown("### <u> Vision Business & storytelling</u>", unsafe_allow_html=True)
        (st.write(""))
        
        with st.expander("**Le constat : Une hémorragie financière**"): 
            st.markdown("""
            Imaginez une banque digitale en pleine expansion. Chaque jour, des milliers de clients effectuent des transactions cruciales depuis leur mobile. Cette ouverture numérique est devenue la cible privilégiée des réseaux criminels spécialisés dans le détournement de fonds. Pour notre institution, cette faille de sécurité se chiffrait par des pertes réelles de plusieurs centaines de millions d'euros par an.
            """)
        
        with st.expander("**La problématique : L'équilibre entre sécurité et fluidité**"):
            st.markdown("""
Le défi posé à notre équipe : stopper la fraude sans dégrader l'expérience utilisateur.

* **Rapidité** : La décision (bloquer ou autoriser) doit être rendue en quelques millisecondes pour ne pas ralentir le client.
* **Satisfaction Client** : Un "Faux Positif" (client honnête bloqué par erreur) est commercialement problématique et a un coût financier non négligeable.
    """)
            
        with st.expander("**La solution : Une architecture innovante de détection en temps réel**"):
            st.markdown("""
Plutôt qu'un modèle statique, nous avons conçu une infrastructure évolutive.

Grâce à notre pipeline MLOps, le système apprend en continu.
Dès que de nouvelles typologies de fraude apparaissent, le modèle se réentraîne automatiquement pour s'adapter aux nouvelles menaces, garantissant une protection toujours à jour.""")
            
        with st.expander("**Les résultats : Une efficacité prouvée**"):
            st.markdown("""
* **Le Bouclier (Recall de 87 %)** : Nous interceptons désormais la grande majorité des tentatives de fraude.

* **La fluidité client (Spécificité de 99,4 %)** : Nous garantissons une expérience sans problème. 99,4 % des transactions légitimes sont validées instantanément, minimisant ainsi le mécontentement client.

* **L'efficacité des alertes (Précision de 63 %)** : Sur l'ensemble des transactions bloquées pour suspicion, près de 2 sur 3 sont réellement des fraudes. Ce score élevé permet aux équipes de sécurité de se concentrer sur des menaces hautement probables plutôt que de traiter un volume ingérable de fausses alertes.""")
            
        with st.expander('**Note sur la simulation de la "Vérité Terrain"**'):   
            st.markdown("""Dans ce projet, les transactions envoyées vers BigQuery incluent la valeur réelle de fraude.

Pourquoi ce choix ? Dans un environnement bancaire réel, il existe un décalage temporel : le modèle prédit une fraude à l'instant T, et la confirmation réelle (le "retour client" ou le signalement) arrive plus tard.

Pour les besoins de la démonstration en temps réel et pour permettre au cycle d'auto-apprentissage (MLOps) de fonctionner de manière fluide, nous avons "compressé le temps". Nous simulons ce retour d'information instantanément afin de démontrer la capacité du pipeline à :

* Détecter l'apparition de nouveaux patterns.

* Déclencher un réentraînement automatique basé sur des données vérifiées.

* Comparer immédiatement la prédiction du modèle avec la réalité pour calculer les métriques de performance.""")


            
        st.write("---")
        
        col1title, col2title, col3title = st.columns([5,6,1])
        with col2title:
            st.markdown("### <u>Dataset et méthodologie</u>", unsafe_allow_html=True)           
        (st.write(""))
        
        st.markdown("##### <u> Aperçu du Dataset complet utilisé pour la détection de fraude :</u>", unsafe_allow_html=True)
        (st.write(""))
        col1_dataset, col2_dataset, col3_dataset= st.columns(3)
        with col1_dataset:
            metric_card("Dataframe de base", "6 353 307 lignes", color="#d1ecf1")           
        with col2_dataset:
            metric_card("Fraudes identifiées", "8 213", color="#d4edda")
        with col3_dataset:
            metric_card("Taux de fraude", "0.13 %", color="#e0c5d6")
        
        (st.write(""))
        st.markdown("##### <u>Séparation des données historiques pour l'entraînement et le flux temps réel (production)</u> :", unsafe_allow_html=True)
        (st.write(""))
        with st.expander("**Détails de la séparation des datasets**"):
            st.markdown("""
Pour simuler un environnement de production réel, nous avons créé un script pour segmenter les données :

* **90% (Historique)** : Utilisés pour l'entraînement initial et stockés comme base de référence.

* **10% (Flux Stream)** : Isolés pour simuler l'envoi de transactions ligne par ligne.

Cette méthode garantit que le modèle est testé sur des données qu'il n'a jamais rencontrées lors de sa phase d'apprentissage initiale.""")
        (st.write(""))
                                
        col1, col2, col3 = st.columns(3)
        with col1: 
            metric_card("Dataframe d'entraînement", "5 726 358 lignes", color="#d1ecf1")   
            metric_card("Dataframe de production", "636 262 lignes", color="#d1ecf1")         
        with col2:
            metric_card("Fraudes identifiées", "4 449", color="#d4edda")
            metric_card("Fraudes identifiées", "3 764", color="#d4edda")
        with col3:
            metric_card("Taux de fraude", "0.07 %", color="#e0c5d6")
            metric_card("Taux de fraude", "0.59 %", color="#e0c5d6")
            
        st.write("---")    
#-------------------ONGLET STACK TECHNIQUE-------------------------
    
    with onglet_stack:
        
        (st.write(""))   
        col1title, col2title, col3title = st.columns([5,6,1])
        with col2title:
            st.markdown("### <u>Stack Technique</u>", unsafe_allow_html=True)
        (st.write("")) 
        (st.write("")) 
    
        col1, col2, col3 = st.columns(3)        
        with col1:
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1.2, 2, 1])
                with centre:
                    st.image("fastapi.png", width=180)
                st.markdown("**Communication** : Reçoit les flux et interroge le modèle pour prédire la fraude. Une fois la prédiction obtenue, l'API renvoie instantanément le verdict (Fraude ou Sain) au système avant d'envoyer les données vers notre buffer Redis")
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1.2, 2, 1])
                with centre:
                    st.image("grafana.png", width=180)
                st.markdown("**Monitoring** : Plateforme de monitoring permettant de visualiser en temps réel la santé technique de l'infrastructure. Elle affiche les performances de l'API, l'utilisation des ressources système et l'état des flux de données.")
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1, 2, 1])
                with centre:
                    st.image("XGBoost.png", width=250)
                    
                st.markdown("""**Modèle de Machine Learning** : basé sur des arbres de décision boostés (Gradient Boosting). 
    C'est lui qui analyse chaque transaction en une fraction de seconde pour calculer une probabilité de fraude. 
    Il a été entraîné pour repérer des patterns complexes (comportements suspects) que des règles classiques ne verraient pas.
    """)

        with col2: 
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1.5, 2, 1])
                with centre:
                    st.image("redis.png", width=140)
                st.markdown("**Redis** : Stocke temporairement les données pour fluidifier le passage entre l'API et le Worker. Il fait office de file d'attente pour absorber les pics de charge. Cela garantit qu'aucune transaction n'est perdue, même en cas de fort trafic")
                
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1.5, 2, 1])
                with centre:
                    st.image("prometheus.png", width=160)
                st.markdown("""**Le Collecteur de Métriques** : Il interroge (pull) régulièrement chaque service pour récupérer leurs constantes vitales (CPU, RAM, temps de latence). Il stocke ces données temporelles 
    et sert de source de données exclusive à Grafana pour l'alerting et le monitoring.
    """)
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([0.5, 2, 0.5])
                with centre:
                    st.image("docker.png", width=800)
                st.markdown("**Docker** : Conteneurisation des services pour garantir une exécution homogène de l'application dans tous les environnements (développement, staging, production).")

            

        with col3:
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1, 2, 1])
                with centre:
                    st.image("bigquery.png", width=140)
                st.markdown("""**Cloud** : Archive l'intégralité des transactions et des prédictions. 
    C'est une étape cruciale pour le réentrainement du modèle : ces données historiques permettent 
    de réentraîner XGBoost régulièrement pour qu'il s'adapte aux nouvelles méthodes de fraude.
    """)
            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1, 2, 1])
                with centre:
                    st.image("streamlit.png", width=180)
                st.markdown("**Vitrine** : Plateforme de monitoring permettant de visualiser en temps réel la santé technique de l'infrastructure. Elle affiche les performances de l'API, l'utilisation des ressources système et l'état des flux de données.")

            with st.container(border=True):
                marge_gauche, centre, marge_droite = st.columns([1, 2, 1])
                with centre:
                    st.image("prefect.png", width=140)
                st.markdown("""**Orchestration** : Automatise le réentraînement du modèle.""")
    
    st.write("---")
    
    
# --------------------------- ONGLET EDA -----------------------------    
    
    with onglet_eda:
        (st.write(""))   
        col1title, col2title, col3title = st.columns([5,6,1])
        with col2title:
            st.markdown("### <u>Analyse exploratoire des données</u>", unsafe_allow_html=True)
        (st.write(""))
        st.markdown("Voici un résumé des principales découvertes issues de notre analyse exploratoire des données (EDA) sur le dataframe d'entrainement du modèle.")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.write("")
                st.write("")
                st.image("bar_chart_types.png", width=1000)
                st.write("")
                st.write("")
                st.write("")
                st.write(" ")
                st.write("")
                st.markdown("##### 1. Répartition des fraudes par type de transaction")
                st.markdown("Les fraudes sont inégalement réparties selon le type de transaction. Les types 'TRANSFER' et 'CASH_OUT' représentent la majorité des fraudes détectées, suggérant que les fraudeurs privilégient ces méthodes pour leurs activités illicites.")
                st.write("")
        with col2:      
            with st.container(border=True):
                st.image("pie_chart_fraude.png", width=700)
                st.markdown("##### 2. Proportion de transactions frauduleuses")
                st.markdown("Le graphique circulaire montre que les transactions frauduleuses sur les données de productions constituent une très faible proportion du total des transactions (0.1%).")
                st.write("")
            

        col1a, col2a = st.columns(2)
        with col1a:
            with st.container(border=True):
                st.image("histplot_heures.png", width=1000)
                st.write(" ")
                st.write(" ")
                st.markdown("##### 3. Distribution des fraudes par heure de la journée")
                st.markdown("L'analyse horaire révèle que les fraudes n'ont pas de période spécifique dans la journée. Peut-être en raison de la nature automatisée des attaques, les fraudeurs opèrent à toute heure, rendant la détection basée sur le temps plus complexe.")
                st.write(" ")
                st.write(" ")
        with col2a:
            with st.container(border=True):
                st.write(" ")
                st.write(" ")
                st.image("histogramme_final.png", width=705)
                st.markdown("##### 4. Montants des fraudes par type de transaction")
                st.markdown("""
L'analyse de la distribution montre que la majorité des fraudes porte sur des montants significatifs, 
avec un pic marqué entre **100 000 € et 1 000 000 €**. La présence d'une barre isolée à l'extrémité droite 
suggère l'existence d'un **plafond transactionnel** fréquemment atteint par les fraudeurs.
""")

# 4. L'APPEL DE LA FONCTION (Le déclencheur)
page_presentation()
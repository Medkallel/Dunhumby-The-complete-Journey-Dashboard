import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import socket


# Charger les données
@st.cache_data  # Cache les données pour une meilleure performance
def load_data():
    data1 = pd.read_csv("./Data/hh_demographic.csv")  
    return data1

data1 = load_data()

def load_data1():
    data2 = pd.read_csv("./Data/transaction_data.csv").merge(pd.read_csv("./Data/hh_demographic.csv"), on='household_key') 
    return data2
data2 = load_data1()

def load_data2():
    data3 = pd.read_csv("./Data/transaction_data.csv").merge(pd.read_csv("./Data/product.csv"), on='PRODUCT_ID')  
    return data3
data3 = load_data2()

# Page 1
def page1():
    st.title("Statistiques descriptives")
    st.subheader('Nombre de lignes et de colonnes:')
    st.write(data1.shape)

    st.subheader('Affichages des premières lignes du jeu de données:')
    st.write(data1.head())
    st.subheader('Statistiques descriptives pour la table sur les données démographiques:')
    st.write(data1.describe())

    st.title("Statistiques descriptives")
    st.subheader('Nombre de lignes et de colonnes:')
    st.write(data2.shape)

    st.subheader('Affichages des premières lignes du jeu de données:')
    st.write(data2.head())
    st.subheader('Statistiques descriptives pour la table sur les données démographiques et transactions:')
    st.write(data2.describe())

# Page 2
def page2():

# Créer le graphique camembert pour la colonne AGE_DESC
    st.markdown("<h2 style='text-align: center; color: #555B61;'>Age des consommateurs</h2>", unsafe_allow_html=True)

    # Compter les occurrences de chaque catégorie d'âge
    age_counts = data1['AGE_DESC'].value_counts()

    # Calculer les pourcentages
    age_percentages = age_counts / len(data1) * 100

    # Créer des étiquettes incluant les titres et les valeurs numériques entre parenthèses
    labels = [f'{age} ({count})' for age, count in zip(age_counts.index, age_counts.values)]

    # Utiliser une palette de couleurs pastel avec Seaborn
    colors = sns.color_palette("muted")

    # Créer le graphique camembert avec des couleurs personnalisées
    fig, ax = plt.subplots()
    ax.pie(age_percentages, labels=labels, autopct='%1.1f%%', colors=colors, 
       textprops={'fontsize': 12, 'fontweight': 500})  # Personnaliser les étiquettes
    # Afficher le graphique avec Streamlit
    st.pyplot(fig)




    # Créer le graphique camembert pour la colonne MARITAL_STATUS_CODE
    st.markdown("<h2 style='text-align: center; color: #555B61;'>Statut marital des consommateurs</h2>", unsafe_allow_html=True)

    # Remplacer les valeurs dans la colonne MARITAL_STATUS_CODE
    data1['MARITAL_STATUS_CODE'] = data1['MARITAL_STATUS_CODE'].replace({'A': 'Couple', 'B': 'Seul(e)'})

    # Compter les occurrences pour les catégories maritales
    statuts_code_counts = data1['MARITAL_STATUS_CODE'].value_counts()

    # Calculer les pourcentages
    status_percentages = statuts_code_counts / len(data1) * 100

    # Créer des étiquettes incluant les titres et les valeurs numériques entre parenthèses
    labels = [f'{statut} ({count})' for statut, count in zip(statuts_code_counts.index, statuts_code_counts.values)]
    # Utiliser une palette de couleurs pastel avec Seaborn
    colors = sns.color_palette("pastel")

    # Créer le graphique camembert avec des couleurs personnalisées
    fig, ax = plt.subplots()
    ax.pie(status_percentages, labels=labels, autopct='%1.1f%%', colors=colors, 
       textprops={'fontsize': 12, 'fontweight': 500})  # Personnaliser les étiquettes
    # Afficher le graphique avec Streamlit
    st.pyplot(fig)






    # Fonction pour remplacer les valeurs d'INCOME_DESC
    def map_income(value):
        if value in ['Under 15K', '15-24K']:
            return '<25K'
        elif value in ['25-34K', '35-49K']:
            return '25-49K'
        elif value in ['50-74K', '75-99K']:
            return '50-99K'
        elif value in ['100-124K', '125-149K']:
            return '100-149K'
        elif value in ['150-174K', '175-199K', '200-249K', '250K+']:
            return '150+'
        else:
            return 'Autre'

    # Appliquer la fonction de mappage
    data1['INCOME_DESC'] = data1['INCOME_DESC'].apply(map_income)

    # Créer le graphique camembert pour la colonne INCOME_DESC
    st.markdown("<h2 style='text-align: center; color: #555B61;'>Répartition des revenus</h2>", unsafe_allow_html=True)

    # Compter les occurrences de chaque catégorie de revenus
    income_counts = data1['INCOME_DESC'].value_counts()

    # Calculer les pourcentages
    income_percentages = income_counts / len(data1) * 100

    # Créer des étiquettes incluant les titres et les valeurs numériques entre parenthèses
    labels = [f'{income} ({count})' for income, count in zip(income_counts.index, income_counts.values)]

    # Utiliser une palette de couleurs pastel avec Seaborn
    colors = sns.color_palette("pastel")

     # Créer le graphique camembert avec des couleurs personnalisées
    fig, ax = plt.subplots()
    ax.pie(income_percentages, labels=labels, autopct='%1.1f%%', colors=colors, 
       textprops={'fontsize': 12, 'fontweight': 500})  # Personnaliser les étiquettes
    # Afficher le graphique avec Streamlit
    st.pyplot(fig)

# Créer le graphique camembert pour la colonne HH_COMP_DESC
    st.markdown("<h2 style='text-align: center; color: #555B61;'>Composition de la famille</h2>", unsafe_allow_html=True)

    # Compter les occurrences 
    comp_desc_counts = data1['HH_COMP_DESC'].value_counts()

    # Calculer les pourcentages
    comp_desc_percentages = comp_desc_counts / len(data1) * 100
    
    # Créer des étiquettes incluant les titres et les valeurs numériques entre parenthèses
    labels = [f'{comp_desc} ({count})' for comp_desc, count in zip(comp_desc_counts.index, comp_desc_counts.values)]
    # Utiliser une palette de couleurs pastel avec Seaborn
    colors = sns.color_palette("pastel")

     # Créer le graphique camembert avec des couleurs personnalisées
    fig, ax = plt.subplots()
    ax.pie(comp_desc_percentages, labels=labels, autopct='%1.1f%%', colors=colors, 
       textprops={'fontsize': 12, 'fontweight': 500})  # Personnaliser les étiquettes
    # Afficher le graphique avec Streamlit
    st.pyplot(fig)


    # Créer le graphique camembert pour la colonne HOMEOWNER_DESC	
    st.markdown("<h2 style='text-align: center; color: #555B61;'>Statut habitation</h2>", unsafe_allow_html=True)

    # Compter les occurrences 
    homeowner_counts = data1['HOMEOWNER_DESC'].value_counts()

    # Calculer les pourcentages
    homeowner_percentages = homeowner_counts / len(data1) * 100

     # Créer des étiquettes incluant les titres et les valeurs numériques entre parenthèses
    labels = [f'{homeowner} ({count})' for homeowner, count in zip(homeowner_counts.index, homeowner_counts.values)]

    # Utiliser une palette de couleurs pastel avec Seaborn
    colors = sns.color_palette("colorblind")

     # Créer le graphique camembert avec des couleurs personnalisées
    fig, ax = plt.subplots()
    ax.pie(homeowner_percentages, labels=labels, autopct='%1.1f%%', colors=colors, 
       textprops={'fontsize': 12, 'fontweight': 500})  # Personnaliser les étiquettes
    # Afficher le graphique avec Streamlit
    st.pyplot(fig)

    # Créer le graphique camembert pour la colonne KID_CATEGORY_DESC
    st.markdown("<h2 style='text-align: center; color: #555B61;'>Nombre d'enfants par foyer</h2>", unsafe_allow_html=True)

    # Compter les occurrences 
    kid_counts = data1['KID_CATEGORY_DESC'].value_counts()

    # Calculer les pourcentages
    kid_percentages = kid_counts / len(data1) * 100

     # Créer des étiquettes incluant les titres et les valeurs numériques entre parenthèses
    labels = [f'{kid} ({count})' for kid, count in zip(kid_counts.index, kid_counts.values)]

    # Utiliser une palette de couleurs pastel avec Seaborn
    colors = sns.color_palette("colorblind")

     # Créer le graphique camembert avec des couleurs personnalisées
    fig, ax = plt.subplots()
    ax.pie(kid_percentages, labels=labels, autopct='%1.1f%%', colors=colors, 
       textprops={'fontsize': 12, 'fontweight': 500})  # Personnaliser les étiquettes
    # Afficher le graphique avec Streamlit
    st.pyplot(fig)

#Page 3
def page3():
# Calculer les ventes totales
    total_sales = data2['SALES_VALUE'].sum()

# Agréger les ventes par catégorie d'âge et calculer les pourcentages
    sales_by_income = data2.groupby('INCOME_DESC')['SALES_VALUE'].sum().reset_index()
    sales_by_income['SALES_PERCENTAGE'] = (sales_by_income['SALES_VALUE'] / total_sales) * 100
     # Trier les données par ordre décroissant
    sales_by_income = sales_by_income.sort_values(by='SALES_VALUE', ascending=False)
     # Créer le graphique
    fig, ax = plt.subplots()
    colors = sns.color_palette('pastel', len(sales_by_income))
    bars = ax.bar(sales_by_income['INCOME_DESC'], sales_by_income['SALES_VALUE'], color=colors)
    ax.set_xlabel('Income Description')
    ax.set_ylabel('Sales Value')
    ax.set_title('Sales Value by Income Description')

    # Ajouter les pourcentages sur les étiquettes de données
    total_sales = data2['SALES_VALUE'].sum()
    for bar, income in zip(bars, sales_by_income['INCOME_DESC']):
        percentage = (sales_by_income.loc[sales_by_income['INCOME_DESC'] == income, 'SALES_VALUE'].values[0] / total_sales) * 100
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{percentage:.1f}%', ha='center', va='center', color='white', fontsize=8)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Afficher le graphique dans Streamlit avec des filtres interactifs
    st.pyplot(fig)


    # Calculer les ventes totales
    total_sales = data2['SALES_VALUE'].sum()

    # Agréger les ventes par catégorie d'âge et calculer les pourcentages
    sales_by_age = data2.groupby('AGE_DESC')['SALES_VALUE'].sum().reset_index()
    sales_by_age['SALES_PERCENTAGE'] = (sales_by_age['SALES_VALUE'] / total_sales) * 100

    # Créer le graphique
    fig, ax = plt.subplots()
    colors = sns.color_palette('pastel', len(sales_by_age))
    ax.bar(sales_by_age['AGE_DESC'], sales_by_age['SALES_VALUE'], color=colors)
    ax.set_xlabel('Age')
    ax.set_ylabel('Sales Value')
    ax.set_title('Sales Value by Age')

    # Ajouter les pourcentages sur les étiquettes de données
    for i, v in enumerate(sales_by_age['SALES_PERCENTAGE']):
        ax.text(i, sales_by_age['SALES_VALUE'][i] + 0.5, f'{v:.1f}%', ha='center')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Afficher le graphique dans Streamlit avec des filtres interactifs
    st.pyplot(fig)

    

    # Calculer les ventes totales
    total_sales = data2['SALES_VALUE'].sum()

    # Agréger les ventes par catégorie d'âge et calculer les pourcentages
    sales_by_status = data2.groupby('MARITAL_STATUS_CODE')['SALES_VALUE'].sum().reset_index()
    sales_by_status['SALES_PERCENTAGE'] = (sales_by_status['SALES_VALUE'] / total_sales) * 100

    # Créer le graphique
    fig, ax = plt.subplots()
    colors = sns.color_palette('pastel', len(sales_by_status))
    ax.bar(sales_by_status['MARITAL_STATUS_CODE'], sales_by_status['SALES_VALUE'], color=colors)
    ax.set_xlabel('Marital Status')
    ax.set_ylabel('Sales Value')
    ax.set_title('Sales Value by Marital Status')

    # Ajouter les pourcentages sur les étiquettes de données
    for i, v in enumerate(sales_by_status['SALES_PERCENTAGE']):
        ax.text(i, sales_by_status['SALES_VALUE'][i] + 0.5, f'{v:.1f}%', ha='center')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Afficher le graphique dans Streamlit avec des filtres interactifs
    st.pyplot(fig)




    # Calculer les ventes totales
    total_sales = data2['SALES_VALUE'].sum()

    # Agréger les ventes par catégorie d'âge et calculer les pourcentages
    sales_by_hh = data2.groupby('HH_COMP_DESC')['SALES_VALUE'].sum().reset_index()
    sales_by_hh['SALES_PERCENTAGE'] = (sales_by_hh['SALES_VALUE'] / total_sales) * 100

# Trier les données par ordre décroissant
    sales_by_hh = sales_by_hh.sort_values(by='SALES_VALUE', ascending=False)

    # Créer le graphique
    fig, ax = plt.subplots()
    colors = sns.color_palette('pastel', len(sales_by_hh))
    bars = ax.bar(sales_by_hh['HH_COMP_DESC'], sales_by_hh['SALES_VALUE'], color=colors)
    ax.set_xlabel('Family composition')
    ax.set_ylabel('Sales Value')
    ax.set_title('Sales Value by Family composition')

    # Ajouter les pourcentages sur les étiquettes de données à l'intérieur des barres
    for bar, percentage in zip(bars, sales_by_hh['SALES_PERCENTAGE']):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{percentage:.1f}%', ha='center', va='center', color='white', fontsize=10)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Afficher le graphique dans Streamlit avec des filtres interactifs
    st.pyplot(fig)


     # Calculer les ventes totales
    total_sales = data2['SALES_VALUE'].sum()

    # Agréger les ventes par catégorie de revenu et calculer les pourcentages
    sales_by_howner = data2.groupby('HOMEOWNER_DESC')['SALES_VALUE'].sum().reset_index()
    sales_by_howner['SALES_PERCENTAGE'] = (sales_by_howner['SALES_VALUE'] / total_sales) * 100



    # Créer le graphique
    fig, ax = plt.subplots()
    colors = sns.color_palette('pastel', len(sales_by_howner))
    ax.bar(sales_by_howner['HOMEOWNER_DESC'], sales_by_howner['SALES_VALUE'], color=colors)
    ax.set_xlabel('Status')
    ax.set_ylabel('Sales Value')
    ax.set_title('Sales Value by Accomodation Status')

    # Ajouter les pourcentages sur les étiquettes de données
    for i, v in enumerate(sales_by_howner['SALES_PERCENTAGE']):
        ax.text(i, sales_by_howner['SALES_VALUE'][i] + 0.5, f'{v:.1f}%', ha='center')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Afficher le graphique dans Streamlit avec des filtres interactifs
    st.pyplot(fig)

    # Calculer les ventes totales
    total_sales = data2['SALES_VALUE'].sum()

    # Agréger les ventes par catégorie de revenu et calculer les pourcentages
    sales_by_kid = data2.groupby('KID_CATEGORY_DESC')['SALES_VALUE'].sum().reset_index()
    sales_by_kid['SALES_PERCENTAGE'] = (sales_by_kid['SALES_VALUE'] / total_sales) * 100



    # Créer le graphique
    fig, ax = plt.subplots()
    colors = sns.color_palette('pastel', len(sales_by_kid))
    ax.bar(sales_by_kid['KID_CATEGORY_DESC'], sales_by_kid['SALES_VALUE'], color=colors)
    ax.set_xlabel('Number of children')
    ax.set_ylabel('Sales Value')
    ax.set_title('Sales Value by Number of Kids')

    # Ajouter les pourcentages sur les étiquettes de données
    for i, v in enumerate(sales_by_kid['SALES_PERCENTAGE']):
        ax.text(i, sales_by_kid['SALES_VALUE'][i] + 0.5, f'{v:.1f}%', ha='center')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Afficher le graphique dans Streamlit avec des filtres interactifs
    st.pyplot(fig)

def page4():
    # Agrégation des ventes par commodité
    sales_by_commodity = data3.groupby('COMMODITY_DESC')['SALES_VALUE'].sum().reset_index()

    # Sélection des 10 premiers COMMODITY_DESC les plus vendus
    top_10_commodities = sales_by_commodity.nlargest(10, 'SALES_VALUE')

    # Interface Streamlit
    st.title('Répartition des ventes par les 10 premiers COMMODITY_DESC les plus vendus')

    # Création du graphique à secteurs (pie chart)
    fig, ax = plt.subplots()
    ax.pie(top_10_commodities['SALES_VALUE'], labels=top_10_commodities['COMMODITY_DESC'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)

    # Affichage des données agrégées
    st.subheader('Données agrégées par les 10 premiers COMMODITY_DESC les plus vendus')
    st.write(top_10_commodities)

        # Création du graphique
    fig, ax = plt.subplots()
    ax.scatter(data3['TRANS_TIME'], data3['SALES_VALUE'], color='blue', alpha=0.7)
    ax.set_xlabel('Heure de la transaction (TRANS_TIME)')
    ax.set_ylabel('Valeur des ventes (SALES_VALUE)')
    ax.set_title('Corrélation entre Heure de la transaction et Valeur des ventes')

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)

   # Calcul de la somme des ventes par mois et par année
    data3_sum = data3.groupby(['ANNÉE', 'MOIS'])['SALES_VALUE'].sum().reset_index()

    # Création du graphique
    fig, ax = plt.subplots()

    # Filtrage des données par année et création des courbes
    for year in data3_sum['ANNÉE'].unique():
        data_year = data3_sum[data3_sum['ANNÉE'] == year]
        ax.plot(data_year['MOIS'], data_year['SALES_VALUE'], marker='o', label=str(year))

    # Personnalisation du graphique
    ax.set_xlabel('Mois')
    ax.set_ylabel('Somme des ventes')
    ax.set_title('Somme des ventes par mois et par année')
    ax.legend()

    # Rotation des étiquettes des mois pour une meilleure lisibilité
    plt.xticks(rotation=45)

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)

    # Rotation des étiquettes des mois pour une meilleure lisibilité
    plt.xticks(rotation=45)

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)


# Sidebar navigation
page = st.sidebar.radio("Sommaire", ["Statistiques descriptives", "Profil des consommateurs", "Analyse des ventes", "Etude produit", "Customer Acquisition"])

    # Display selected page
if page == "Statistiques descriptives":
        page1()
elif page == "Profil des consommateurs":
        page2()
elif page == "Analyse des ventes":
        page3() 
elif page == "Etude produit":
        page4()
elif page == "Customer Acquisition":
        page5()


        
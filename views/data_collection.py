import streamlit as st
import datetime
from database import DataEntry

def display_data_collection_page():
    st.title("HealthPro")
    st.header("Saisie de vos données quotidiennes")
    if 'user_id' not in st.session_state:
        st.error("Veuillez vous connecter pour saisir vos données.")
    else:
        user_id = st.session_state['user_id']
        unformatted_date = st.date_input("Date", datetime.date.today())
        date = datetime.datetime.combine(unformatted_date, datetime.datetime.min.time())

        # Données générales
        st.subheader("Informations générales")
        age = st.number_input("Âge", min_value=0, step=1)
        sexe = st.text_input("Sexe à la naissance", value = "Homme / Femme")
        height = st.number_input("Taille (cm)", min_value=50, max_value=250, step=1)
        weight = st.number_input("Poids (kg)", min_value=20.0, max_value=200.0, step=0.1)
        bmi = weight / ((height / 100) ** 2) if height > 0 else 0

        # Données quotidiennes
        st.subheader("Données quotidiennes")
        water = st.number_input("Eau consommée (L)", min_value=0.0, step=0.1)
        calories = st.number_input("Calories consommées", min_value=0, step=10)
        sleep = st.number_input("Heures de sommeil", min_value=0.0, step=0.5)
        activity_time = st.number_input("Temps d'activité physique (min)", min_value=0, step=1)

        # Données pour ainés (optionnelles) >>> (Entrez "---" si ça ne s'applique pas à vous)
        st.subheader("Pour les seniors (optionnel)")
        tug = st.number_input("Test de 'Timed up and go' (sec) \n- Temps que ça vous prend pour vous lever d'une position assise", min_value=0, step=1, value=0)
        amsler = st.text_input("Résultat test visuel (Amsler)\n- Instructions: Regardez le point au milieu de la grille pendant 30 secondes.\nSi les carreaux de la grille commencent à courber, notez le. Sinon, Notez 'Normal'.", value="Normal")
        hearing = st.number_input("Résultat test auditif (cm)\n- Instructions : Dites à quelqu'un de frotter leurs doigts à 7-10cm de votre oreille en s'éloignant progressivement.\nNotez la distance à laquelle vous arretez d'entendre le son du frottement des doigts.\nRépetez pour l'autre oreille.", min_value=0.0, step=0.1, value=0.0)
        if st.button("Enregistrer les données"):
            new_entry = DataEntry(
                user_id=user_id,
                date=date,
                age=age,
                sexe = sexe,
                height=height,
                weight=weight,
                bmi=bmi,
                water=water,
                calories=calories,
                sleep=sleep,
                activity_time=activity_time,
                timed_up_and_go_test=tug,
                amsler=amsler,
                hearing=hearing
            )
            new_entry.save()
            st.success("Données enregistrées avec succès!")
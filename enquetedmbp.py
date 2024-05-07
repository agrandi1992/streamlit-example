import streamlit as st
import pandas as pd

def main():
    st.title("**Questionnaire**")
    st.write("Veuillez répondre aux questions suivantes :")
    
    # Collecte des informations sur le répondant
    st.markdown("### Informations sur le répondant")
    first_name = st.text_input("Prénom")
    last_name = st.text_input("Nom de famille")
    company = st.text_input("Société")

    # Créer un DataFrame pour stocker les réponses
    responses_df = pd.DataFrame(columns=["Question", "Réponse"])

    # Ajout des nouvelles questions au début du questionnaire
    profession = st.radio("1/ Comment définissez-vous votre activité professionnelle ?", ("", "1 – Agenceur", "2 – Menuisier", "3 – Charpentier", "4 – Constructeur Ossature Bois", "5 – Entreprise générale du bâtiment", "6 – Autres – Préciser dans ce cas"), key="profession")
    if profession == "":
        st.warning("Veuillez répondre à la question.")
    else:
        responses_df = responses_df.append({"Question": "Activité professionnelle", "Réponse": profession}, ignore_index=True)
        if profession == "6 – Autres – Préciser dans ce cas":
            other_profession = st.text_input("Veuillez préciser votre activité professionnelle")
            responses_df = responses_df.append({"Question": "Autre activité professionnelle", "Réponse": other_profession}, ignore_index=True)

    st.markdown("### Dans le cadre de votre activité, vous achetez à votre distributeur (Dispano/Panofrance ou autres distributeurs) ")
    # Poser les questions initiales et enregistrer les réponses
    questions = [
        "Des Panneaux décoratifs (mélaminés, stratifiés, MDF…)",
        "Des Panneaux de structure (OSB, contreplaqués, 3 plis résineux…)",
        "Du Bois de construction (poutre grande longueur, …)",
        "De la Menuiserie intérieures / extérieures / Dressing",
        "Du Parquets et des Lambris",
        "De la Terrasse et de l’aménagement extérieur",
        "de l’outillage et de la quincaillerie",
        "Des Plaques de plâtre et de l’isolation",
        "Des bardages et panneaux de façade"
    ]
    for index, question in enumerate(questions, start=1):
        response = st.radio(f"**{question} ?**", ("", "Oui", "Non"), key=f"main_question_{index}")
        if response == "":
            st.warning("Veuillez répondre à la question.")
        responses_df = responses_df.append({"Question": question, "Réponse": response}, ignore_index=True)

    # Vérifier si toutes les réponses aux questions principales sont Oui ou Non
    all_responses = responses_df["Réponse"].isin(["Oui", "Non"]).all()

    # Si toutes les réponses aux questions principales sont Oui ou Non, poser les questions spécifiques selon la réponse à chaque question principale
    if all_responses:
        for i in range(len(questions)):
            question_response = responses_df.iloc[i]["Réponse"]
            if question_response == "Oui":
                if i == 0:  # Première question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la première question - Des Panneaux décoratifs (mélaminés, stratifiés, MDF…)")
                    additional_question_1 = st.radio("a/ Concernant les panneaux décoratifs, vous récupérez le plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_1")
                    if additional_question_1 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération des panneaux décoratifs", "Réponse": additional_question_1}, ignore_index=True)
                        if additional_question_1 == "1 – via une livraison sur site":
                            delivery_time_question_1 = st.radio("b/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures", "3 – J+5 : sous une semaine"), key="delivery_time_question_1")
                            if delivery_time_question_1 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_1}, ignore_index=True)
                                if delivery_time_question_1 in ["1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures"]:
                                    order_time_question_1 = st.radio("c/ Jusqu’à quelle heure souhaitez-vous pouvoir passer cette commande?", ("", "1 – Une clôture de passage de commande à 12h00 me convient pour la livraison en 24/48h", "2 – Une clôture de passage de commande à 16h00 me convient pour la livraison en 24/48h"), key="order_time_question_1")
                                    if order_time_question_1 == "":
                                        st.warning("Veuillez répondre à la question.")
                                    else:
                                        responses_df = responses_df.append({"Question": "Heure de commande", "Réponse": order_time_question_1}, ignore_index=True)
                        elif additional_question_1 == "2 – par un enlèvement en agence":
                            pickup_time_question_1 = st.radio("d/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "1 – J0 : Les produits sont communs et doivent être en stock en agence", "2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_1")
                            if pickup_time_question_1 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_1}, ignore_index=True)
                                if pickup_time_question_1 in ["2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"]:
                                    order_time_question_2 = st.radio("e/ Jusqu’à quelle heure souhaitez-vous pouvoir passer cette commande?", ("", "1 – Une clôture de passage de commande à 12h00 me convient pour une mise à disposition", "2 – Une clôture de passage de commande à 16h00 me convient pour une mise à disposition"), key="order_time_question_2")
                                    if order_time_question_2 == "":
                                        st.warning("Veuillez répondre à la question.")
                                    else:
                                        responses_df = responses_df.append({"Question": "Heure de commande", "Réponse": order_time_question_2}, ignore_index=True)
                        st.markdown("### Retour sur une question d’ordre général sur le marché du panneau d’agencement ")
                        additional_question_b = st.radio("Faites-vous appel à de la sous-traitance dans votre activité de transformation des panneaux ?", ("", "1 – Oui souvent", "2 – Non rarement"), key="additional_question_b")
                        if additional_question_b == "":
                           st.warning("Veuillez répondre à la question.")
                        else:
                           responses_df = responses_df.append({"Question": "Méthode de récupération des panneaux de structure", "Réponse": additional_question_b}, ignore_index=True)                
                    
                elif i == 1:  # Deuxième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la deuxième question - Des Panneaux de structure (OSB, contreplaqués, 3 plis résineux…)")
                    additional_question_2 = st.radio("a/ Concernant les panneaux de structure, vous récupérez le plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_2")
                    if additional_question_2 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération des panneaux de structure", "Réponse": additional_question_2}, ignore_index=True)
                        if additional_question_2 == "1 – via une livraison sur site":
                            delivery_time_question_2 = st.radio("b/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures", "3 – J+5 : sous une semaine"), key="delivery_time_question_2")
                            if delivery_time_question_2 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_2}, ignore_index=True)
                                
                        elif additional_question_2 == "2 – par un enlèvement en agence":
                            pickup_time_question_2 = st.radio("d/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "1 – J0 : Les produits sont communs et doivent être en stock en agence", "2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_2")
                            if pickup_time_question_2 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_2}, ignore_index=True)
                                
                elif i == 2:  # Troisième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la troisième question - Du Bois de construction (poutre grande longueur, …)")
                    additional_question_3 = st.radio("a/ Concernant le Bois de construction, vous récupérez le plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_3")
                    if additional_question_3 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération du bois de construction", "Réponse": additional_question_3}, ignore_index=True)
                        if additional_question_3 == "1 – via une livraison sur site":
                            delivery_time_question_3 = st.radio("b/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures", "3 – J+5 : sous une semaine"), key="delivery_time_question_3")
                            if delivery_time_question_3 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_3}, ignore_index=True)
                                
                                    
                        elif additional_question_3 == "2 – par un enlèvement en agence":
                            pickup_time_question_3 = st.radio("d/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "1 – J0 : Les produits sont communs et doivent être en stock en agence", "2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_3")
                            if pickup_time_question_3 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_3}, ignore_index=True)
                elif i == 3:  # Quatrième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la quatrième question - De la Menuiserie intérieure / extérieure / Dressing")
                    additional_question_4 = st.radio("n/ Concernant la menuiserie intérieure / extérieure, vous récupérez le plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_4")
                    if additional_question_4 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération de la menuiserie intérieure / extérieure", "Réponse": additional_question_4}, ignore_index=True)
                        if additional_question_4 == "1 – via une livraison sur site":
                            delivery_time_question_4 = st.radio("z/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "J+1 : le lendemain", "J+2 : sous 48 heures", "J+5 : sous une semaine"), key="delivery_time_question_4")
                            if delivery_time_question_4 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_4}, ignore_index=True)
                        elif additional_question_4 == "2 – par un enlèvement en agence":
                            pickup_time_question_4 = st.radio("v/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "J0 : Les produits sont communs et doivent être en stock en agence", "J+1 : mise à disposition en agence le lendemain", "J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_4")
                            if pickup_time_question_4 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_4}, ignore_index=True)
                elif i == 4:  # Cinquième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la cinquième question - Des Parquets et Lambris")
                    additional_question_5 = st.radio("ff/ Concernant les Parquets et Lambris, vous récupérez le plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_5")
                    if additional_question_5 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération des Parquets et Lambris", "Réponse": additional_question_5}, ignore_index=True)
                        if additional_question_5 == "1 – via une livraison sur site":
                            delivery_time_question_5 = st.radio("gg/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "J+1 : le lendemain", "J+2 : sous 48 heures", "J+5 : sous une semaine"), key="delivery_time_question_5")
                            if delivery_time_question_5 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_5}, ignore_index=True)
                        elif additional_question_5 == "2 – par un enlèvement en agence":
                            pickup_time_question_5 = st.radio("hh/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "J0 : Les produits sont communs et doivent être en stock en agence", "J+1 : mise à disposition en agence le lendemain", "J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_5")
                            if pickup_time_question_5 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_5}, ignore_index=True)
                elif i == 5:  # Sixième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la sixième question - De la Terrasse et de l’aménagement extérieur")
                    additional_question_6 = st.radio("i/ Concernant les produits de terrasse / aménagements extérieurs, vous récupérez les plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_6")
                    if additional_question_6 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération des produits de terrasse / aménagements extérieurs", "Réponse": additional_question_6}, ignore_index=True)
                        if additional_question_6 == "1 – via une livraison sur site":
                            delivery_time_question_6 = st.radio("j/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures", "3 – J+5 : sous une semaine"), key="delivery_time_question_6")
                            if delivery_time_question_6 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_6}, ignore_index=True)
                        elif additional_question_6 == "2 – par un enlèvement en agence":
                            pickup_time_question_6 = st.radio("k/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "1 – J0 : Les produits sont communs et doivent être en stock en agence", "2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_6")
                            if pickup_time_question_6 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_6}, ignore_index=True)
                elif i == 6:  # Septième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la septième question - De l'outillage et de la quincaillerie")
                    additional_question_7 = st.radio("l/ Concernant l'outillage et la quincaillerie, vous récupérez les plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_7")
                    if additional_question_7 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération de l'outillage et de la quincaillerie", "Réponse": additional_question_7}, ignore_index=True)
                        if additional_question_7 == "1 – via une livraison sur site":
                            delivery_time_question_7 = st.radio("m/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures", "3 – J+5 : sous une semaine"), key="delivery_time_question_7")
                            if delivery_time_question_7 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_7}, ignore_index=True)
                        elif additional_question_7 == "2 – par un enlèvement en agence":
                            pickup_time_question_7 = st.radio("n/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "1 – J0 : Les produits sont communs et doivent être en stock en agence", "2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_7")
                            if pickup_time_question_7 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_7}, ignore_index=True)
                elif i == 7:  # Huitième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la huitième question - Des Plaques de plâtre et de l'isolation")
                    additional_question_8 = st.radio("o/ Concernant les Plaques de plâtre et de l'isolation, vous récupérez les plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_8")
                    if additional_question_8 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération des Plaques de plâtre et de l'isolation", "Réponse": additional_question_8}, ignore_index=True)
                        if additional_question_8 == "1 – via une livraison sur site":
                            delivery_time_question_8 = st.radio("p/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures", "3 – J+5 : sous une semaine"), key="delivery_time_question_8")
                            if delivery_time_question_8 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_8}, ignore_index=True)
                        elif additional_question_8 == "2 – par un enlèvement en agence":
                            pickup_time_question_8 = st.radio("q/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "1 – J0 : Les produits sont communs et doivent être en stock en agence", "2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_8")
                            if pickup_time_question_8 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_8}, ignore_index=True)
                elif i == 8:  # Neuvième question principale
                    st.markdown("### Questions spécifiques pour la réponse 'Oui' à la neuvième question - Des bardages et panneaux de façade")
                    additional_question_9 = st.radio("r/ Concernant les bardages et panneaux de façade, vous récupérez les plus souvent ces derniers ?", ("", "1 – via une livraison sur site", "2 – par un enlèvement en agence"), key="additional_question_9")
                    if additional_question_9 == "":
                        st.warning("Veuillez répondre à la question.")
                    else:
                        responses_df = responses_df.append({"Question": "Méthode de récupération des bardages et panneaux de façade", "Réponse": additional_question_9}, ignore_index=True)
                        if additional_question_9 == "1 – via une livraison sur site":
                            delivery_time_question_9 = st.radio("s/ Quel délai souhaitez-vous entre la commande et la livraison ?", ("", "1 – J+1 : le lendemain", "2 – J+2 : sous 48 heures", "3 – J+5 : sous une semaine"), key="delivery_time_question_9")
                            if delivery_time_question_9 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de livraison", "Réponse": delivery_time_question_9}, ignore_index=True)
                        elif additional_question_9 == "2 – par un enlèvement en agence":
                            pickup_time_question_9 = st.radio("t/ Quel délai souhaitez-vous entre la commande et la mise à disposition pour enlèvement?", ("", "1 – J0 : Les produits sont communs et doivent être en stock en agence", "2 – J+1 : mise à disposition en agence le lendemain", "3 – J+2 : mise à disposition en agence sous 48h00"), key="pickup_time_question_9")
                            if pickup_time_question_9 == "":
                                st.warning("Veuillez répondre à la question.")
                            else:
                                responses_df = responses_df.append({"Question": "Délai de mise à disposition pour enlèvement", "Réponse": pickup_time_question_9}, ignore_index=True)


      
  # Poser des questions supplémentaires
    st.markdown("### Questions supplémentaires hors questions spécifiques")
    additional_question_12 = st.radio("12/ Lorsque vous commandez plusieurs produits (panneaux décoratifs et portes par exemple), comment souhaitez-vous être livré ?", ("", "1 – Tous les produits que je consomme doivent être livrés en même temps", "2 – Des livraisons dissociées par famille (par exemple les panneaux d’une part et les portes d’autres part) ne me posent pas de problèmes si elles sont annoncées"), key="additional_question_12")
    if additional_question_12 == "":
        st.warning("Veuillez répondre à la question.")
    else:
        responses_df = responses_df.append({"Question": "Mode de livraison pour plusieurs produits", "Réponse": additional_question_12}, ignore_index=True)

    # Afficher les réponses
    if st.button("Afficher les réponses"):
        st.write(responses_df)
if __name__ == "__main__":
    main()

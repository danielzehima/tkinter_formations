import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

fenetre = ctk.CTk()
fenetre.title("Formulaire d'ajout de bien 🏠")
fenetre.geometry("500x400")

# --- Titre ---
titre = ctk.CTkLabel(fenetre, text="Ajouter un Bien Immobilier", font=("Segoe UI", 20, "bold"))
titre.pack(pady=20)

# --- Champs du formulaire ---
label_nom = ctk.CTkLabel(fenetre, text="Nom du bien :")
label_nom.pack()
entree_nom = ctk.CTkEntry(fenetre, placeholder_text="Ex : Villa Bonapriso")
entree_nom.pack(pady=5)

label_adresse = ctk.CTkLabel(fenetre, text="Adresse :")
label_adresse.pack()
entree_adresse = ctk.CTkEntry(fenetre, placeholder_text="Ex : Cocody, Abidjan")
entree_adresse.pack(pady=5)

label_prix = ctk.CTkLabel(fenetre, text="Prix mensuel (FCFA) :")
label_prix.pack()
entree_prix = ctk.CTkEntry(fenetre, placeholder_text="Ex : 250000")
entree_prix.pack(pady=5)

# --- Menu déroulant ---
label_type = ctk.CTkLabel(fenetre, text="Type de bien :")
label_type.pack()
type_bien = ctk.CTkOptionMenu(fenetre, values=["Appartement", "Maison", "Studio", "Bureau"])
type_bien.pack(pady=5)

# --- Fonction de validation ---
def enregistrer():
    nom = entree_nom.get()
    adresse = entree_adresse.get()
    prix = entree_prix.get()
    type_sel = type_bien.get()

    if nom and adresse and prix:
        ctk.CTkLabel(fenetre, text=f"✅ Bien '{nom}' enregistré avec succès !", text_color="green").pack(pady=10)
        print(f"Bien ajouté : {nom}, {adresse}, {prix} FCFA, {type_sel}")
    else:
        ctk.CTkLabel(fenetre, text="⚠️ Veuillez remplir tous les champs.", text_color="red").pack(pady=10)

# --- Bouton ---
btn_valider = ctk.CTkButton(fenetre, text="Enregistrer", command=enregistrer)
btn_valider.pack(pady=20)

fenetre.mainloop()

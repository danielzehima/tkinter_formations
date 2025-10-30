import customtkinter as ctk
import sqlite3

# --- Configuration fenêtre ---
ctk.set_appearance_mode("light")  # light, dark ou system
ctk.set_default_color_theme("green")

fenetre = ctk.CTk()
fenetre.geometry("700x450")
fenetre.title("Enregistrement des données dans une base de données")

# --- Connexion / création de la base ---
conn = sqlite3.connect("Immobilier.db")
curseur = conn.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS biens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    adresse TEXT,
    prix INTEGER,
    type TEXT
)
""")
conn.commit()

# --- Fonction d’enregistrement ---
def enregistrer():
    nom = txt_nom.get()
    adresse = txt_adr.get()
    prix = txt_prix.get()
    type_bien = txt_type.get()

    if not nom or not prix or not adresse:
        message_info.configure(text="⚠️ Veuillez remplir tous les champs", text_color='red')
        return
    try:
        curseur.execute(
            "INSERT INTO biens (nom, adresse, prix, type) VALUES (?, ?, ?, ?)",
            (nom, adresse, prix, type_bien)
        )
        conn.commit()

        message_info.configure(text=f"✅ Bien '{nom}' ajouté avec succès !", text_color="green")

        # Réinitialisation
        txt_nom.delete(0, "end")
        txt_prix.delete(0, "end")
        txt_adr.delete(0, "end")

    except Exception as e:
        message_info.configure(text=f"❌ Erreur : {e}", text_color="red")

# --- Interface ---
ctk.CTkLabel(
    fenetre,
    text="Formulaire de saisie des biens immobiliers",
    font=("Times New Roman", 20, "bold")
).pack(pady=15)

txt_nom = ctk.CTkEntry(fenetre, placeholder_text="Entrez le nom")
txt_nom.pack(pady=10)

txt_adr = ctk.CTkEntry(fenetre, placeholder_text="Saisir l'adresse")
txt_adr.pack(pady=10)

txt_prix = ctk.CTkEntry(fenetre, placeholder_text="Entrez le prix")
txt_prix.pack(pady=10)

txt_type = ctk.CTkOptionMenu(fenetre, values=["Maison", "Appartement", "Bureau", "Magasin", "Terrain"])
txt_type.pack(pady=10)

message_info = ctk.CTkLabel(fenetre, text="")
message_info.pack(pady=10)

btn_enregistrer = ctk.CTkButton(fenetre, text="Enregistrer", font=("Arial", 12, "bold"), cursor="hand2", command=enregistrer)
btn_enregistrer.pack(pady=15)

fenetre.mainloop()

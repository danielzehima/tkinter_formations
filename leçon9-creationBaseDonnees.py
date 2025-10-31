import customtkinter as ctk
from tkinter import ttk
import sqlite3


# --- Apparence ---
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# --- Fenêtre principale ---
fenetre = ctk.CTk()
fenetre.geometry("850x550")
fenetre.title("Gestion des biens immobiliers 🏠")

# --- Base de données ---
conn = sqlite3.connect("Immobilier.db")
curseur = conn.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS biens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    adresse TEXT,
    prix INTEGER,
    type TEXT
)
""")
conn.commit()

# --- Fonction pour insérer un bien ---
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

        txt_nom.delete(0, "end")
        txt_prix.delete(0, "end")
        txt_adr.delete(0, "end")

        # Mettre à jour le tableau automatiquement
        afficher_biens()

    except Exception as e:
        message_info.configure(text=f"❌ Erreur : {e}", text_color="red")


# --- Fonction pour afficher les biens ---
def afficher_biens():
    for item in tableau.get_children():
        tableau.delete(item)

    curseur.execute("SELECT * FROM biens")
    biens = curseur.fetchall()
    for b in biens:
        tableau.insert("", "end", values=b)


# --- Interface graphique ---
# Titre
ctk.CTkLabel(
    fenetre,
    text="Formulaire de saisie des biens immobiliers",
    font=("Times New Roman", 20, "bold")
).pack(pady=10)

# Frame de saisie
frame_saisie = ctk.CTkFrame(fenetre)
frame_saisie.pack(pady=10, fill="x", padx=20)

txt_nom = ctk.CTkEntry(frame_saisie, placeholder_text="Nom du bien")
txt_nom.grid(row=0, column=0, padx=10, pady=5)

txt_adr = ctk.CTkEntry(frame_saisie, placeholder_text="Adresse")
txt_adr.grid(row=0, column=1, padx=10, pady=5)

txt_prix = ctk.CTkEntry(frame_saisie, placeholder_text="Prix (FCFA)")
txt_prix.grid(row=0, column=2, padx=10, pady=5)

txt_type = ctk.CTkOptionMenu(frame_saisie, values=["Maison", "Appartement", "Bureau", "Magasin", "Terrain"])
txt_type.grid(row=0, column=3, padx=10, pady=5)

# Bouton d’enregistrement
btn_enregistrer = ctk.CTkButton(frame_saisie, text="Enregistrer", command=enregistrer)
btn_enregistrer.grid(row=0, column=4, padx=10, pady=5)

message_info = ctk.CTkLabel(fenetre, text="")
message_info.pack(pady=5)

# --- Tableau d’affichage ---
ctk.CTkLabel(
    fenetre,
    text="Liste des biens enregistrés",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Frame contenant le tableau
frame_tableau = ctk.CTkFrame(fenetre)
frame_tableau.pack(padx=20, pady=10, fill="both", expand=True)

# Colonnes du tableau
style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 12), rowheight=30)
style.configure("Treeview.Heading", font=("Segoe UI", 13, "bold"))

colonnes = ("ID", "Nom", "Adresse", "Prix", "Type")

tableau = ttk.Treeview(frame_tableau, columns=colonnes, show="headings", height=10)
for col in colonnes:
    tableau.heading(col, text=col)
    tableau.column(col, width=150)

# Barre de défilement
scrollbar = ttk.Scrollbar(frame_tableau, orient="vertical", command=tableau.yview)
tableau.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tableau.pack(fill="both", expand=True)

# Charger les données existantes
afficher_biens()

fenetre.mainloop()

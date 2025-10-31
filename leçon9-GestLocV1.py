# =======================
# 🏠 GESTION DES LOCATAIRES v1.0
# =======================
import sqlite3
import customtkinter as ctk
from tkinter import ttk, messagebox

# --- Apparence générale ---
ctk.set_appearance_mode('system')
ctk.set_default_color_theme("blue")

# --- Fenêtre principale ---
fenetre = ctk.CTk()
fenetre.geometry("950x550")
fenetre.title("🏠 Gestion des Locataires")

# =======================
# 🔹 BASE DE DONNÉES
# =======================
conn = sqlite3.connect('Immobilier.db')
curseur = conn.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS locataire(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    prenoms TEXT,
    telephone TEXT,
    email TEXT,
    adresse TEXT
)
""")
conn.commit()

# =======================
# 🔹 FONCTIONS
# =======================

def afficher_locataires():
    """Affiche tous les locataires dans le tableau"""
    for item in tableau.get_children():
        tableau.delete(item)

    curseur.execute("SELECT * FROM locataire")
    locataires = curseur.fetchall()
    for loc in locataires:
        tableau.insert("", "end", values=loc)


def enregistrer():
    """Ajoute un nouveau locataire"""
    nom = txt_nom.get().strip()
    prenom = txt_prenom.get().strip()
    telephone = txt_telep.get().strip()
    email = txt_email.get().strip()
    adresse = txt_adresse.get().strip()

    if not nom or not prenom or not telephone or not email or not adresse:
        messagebox.showinfo("Champs manquants", "Veuillez remplir tous les champs.")
        return

    try:
        curseur.execute(
            "INSERT INTO locataire (nom, prenoms, telephone, email, adresse) VALUES (?, ?, ?, ?, ?)",
            (nom, prenom, telephone, email, adresse)
        )
        conn.commit()
        messagebox.showinfo("Succès", f"✅ {nom} ajouté avec succès !")
        reinitialiser_champs()
        afficher_locataires()

    except Exception as e:
        messagebox.showerror("Erreur", f"{e}")


def selectionner_locataire(event):
    """Remplit les champs lorsqu'on sélectionne un locataire"""
    selection = tableau.focus()
    if not selection:
        return
    valeurs = tableau.item(selection, "values")

    txt_nom.delete(0, 'end')
    txt_nom.insert(0, valeurs[1])

    txt_prenom.delete(0, 'end')
    txt_prenom.insert(0, valeurs[2])

    txt_telep.delete(0, 'end')
    txt_telep.insert(0, valeurs[3])

    txt_email.delete(0, 'end')
    txt_email.insert(0, valeurs[4])

    txt_adresse.delete(0, 'end')
    txt_adresse.insert(0, valeurs[5])


def modifier_locataire():
    """Met à jour les informations du locataire sélectionné"""
    selection = tableau.focus()
    if not selection:
        messagebox.showwarning("Attention", "Veuillez sélectionner un locataire à modifier.")
        return

    valeurs = tableau.item(selection, "values")
    loc_id = valeurs[0]

    nom = txt_nom.get().strip()
    prenom = txt_prenom.get().strip()
    telephone = txt_telep.get().strip()
    email = txt_email.get().strip()
    adresse = txt_adresse.get().strip()

    if not nom or not prenom or not telephone or not email or not adresse:
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs avant de modifier.")
        return

    try:
        curseur.execute("""
            UPDATE locataire 
            SET nom=?, prenoms=?, telephone=?, email=?, adresse=?
            WHERE id=?
        """, (nom, prenom, telephone, email, adresse, loc_id))
        conn.commit()
        messagebox.showinfo("Succès", "Les informations ont été modifiées avec succès ✅")
        reinitialiser_champs()
        afficher_locataires()
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la modification : {e}")


def supprimer_locataire():
    """Supprime le locataire sélectionné"""
    selection = tableau.focus()
    if not selection:
        messagebox.showwarning("Attention", "Veuillez sélectionner un locataire à supprimer.")
        return

    valeurs = tableau.item(selection, "values")
    loc_id = valeurs[0]

    confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer le locataire '{valeurs[1]}' ?")
    if confirmation:
        try:
            curseur.execute("DELETE FROM locataire WHERE id=?", (loc_id,))
            conn.commit()
            messagebox.showinfo("Succès", "Le locataire a été supprimé avec succès 🗑️")
            reinitialiser_champs()
            afficher_locataires()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la suppression : {e}")


def reinitialiser_champs():
    """Vide tous les champs de saisie"""
    txt_nom.delete(0, 'end')
    txt_prenom.delete(0, 'end')
    txt_telep.delete(0, 'end')
    txt_email.delete(0, 'end')
    txt_adresse.delete(0, 'end')

# =======================
# 🔹 INTERFACE GRAPHIQUE
# =======================

lbl_titre = ctk.CTkLabel(fenetre, text="👥 Gestion des Locataires", font=("Times New Roman", 22, "bold"))
lbl_titre.pack(pady=10)

# --- Frame saisie ---
frame_saisie = ctk.CTkFrame(fenetre, height=100, corner_radius=10)
frame_saisie.pack(pady=10, fill="x", padx=10)

txt_nom = ctk.CTkEntry(frame_saisie, placeholder_text="Nom")
txt_nom.grid(row=0, column=0, padx=5, pady=5)

txt_prenom = ctk.CTkEntry(frame_saisie, placeholder_text="Prénoms")
txt_prenom.grid(row=0, column=1, padx=5, pady=5)

txt_telep = ctk.CTkEntry(frame_saisie, placeholder_text="Téléphone")
txt_telep.grid(row=0, column=2, padx=5, pady=5)

txt_email = ctk.CTkEntry(frame_saisie, placeholder_text="Email")
txt_email.grid(row=0, column=3, padx=5, pady=5)

txt_adresse = ctk.CTkEntry(frame_saisie, placeholder_text="Adresse")
txt_adresse.grid(row=0, column=4, padx=5, pady=5)

btn_enr = ctk.CTkButton(frame_saisie, text="Enregistrer", font=("Arial", 14, "bold"), cursor="hand2", command=enregistrer)
btn_enr.grid(row=1, column=2, padx=10, pady=5)

btn_modifier = ctk.CTkButton(frame_saisie, text="Modifier", font=("Arial", 14), cursor="hand2", command=modifier_locataire)
btn_modifier.grid(row=1, column=3, padx=10, pady=5)

btn_supprimer = ctk.CTkButton(frame_saisie, text="Supprimer", font=("Arial", 14), cursor="hand2", fg_color="red", hover_color="#cc0000", command=supprimer_locataire)
btn_supprimer.grid(row=1, column=4, padx=10, pady=5)

# --- Frame contenu ---
frame_contenu = ctk.CTkFrame(fenetre, corner_radius=10)
frame_contenu.pack(padx=10, pady=10, fill="both", expand=True)

lbl_info = ctk.CTkLabel(frame_contenu, text="📋 Liste des locataires enregistrés", font=("Segoe UI", 18, "bold"))
lbl_info.pack(pady=10)

# --- Tableau des locataires ---
colonnes = ("ID", "Nom", "Prénoms", "Téléphone", "Email", "Adresse")
tableau = ttk.Treeview(frame_contenu, columns=colonnes, show="headings", height=10)

for col in colonnes:
    tableau.heading(col, text=col)
    tableau.column(col, width=150, anchor="center")

# Style du tableau
style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 12), rowheight=30)
style.configure("Treeview.Heading", font=("Segoe UI", 13, "bold"))

# Barre de défilement
scrollbar = ttk.Scrollbar(frame_contenu, orient="vertical", command=tableau.yview)
tableau.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tableau.pack(fill="both", expand=True)

# Événement sélection
tableau.bind("<ButtonRelease-1>", selectionner_locataire)

# Charger les données au démarrage
afficher_locataires()

# Fermer proprement la connexion à la fermeture
def fermer_app():
    conn.close()
    fenetre.destroy()

fenetre.protocol("WM_DELETE_WINDOW", fermer_app)

fenetre.mainloop()

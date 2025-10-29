import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Gestion Immobilière 🏠")
fenetre.geometry("900x500")
fenetre.config(bg="#ecf0f1")

# Frame principale : menu + contenu
menu_frame = tk.Frame(fenetre, bg="#2ecc71", width=200)
menu_frame.pack(side="left", fill="y")

conteneur = tk.Frame(fenetre, bg="#f7f9f9")
conteneur.pack(expand=True, fill="both")

# Définition des pages
page_accueil = tk.Frame(conteneur, bg="#f7f9f9")
page_biens = tk.Frame(conteneur, bg="#d6eaf8")
page_locataires = tk.Frame(conteneur, bg="#fad7a0")

for page in (page_accueil, page_biens, page_locataires):
    page.place(relwidth=1, relheight=1)

def afficher_page(page):
    page.tkraise()

# --- Contenu des pages ---
tk.Label(page_accueil, text="🏠 Tableau de bord", font=("Arial", 20, "bold"), bg="#f7f9f9").pack(pady=100)
tk.Label(page_biens, text="📋 Gestion des Biens", font=("Arial", 20, "bold"), bg="#d6eaf8").pack(pady=100)
tk.Label(page_locataires, text="👥 Gestion des Locataires", font=("Arial", 20, "bold"), bg="#fad7a0").pack(pady=100)

# --- Boutons du menu latéral ---
tk.Label(menu_frame, text="Menu", bg="#27ae60", fg="white", font=("Arial", 14, "bold")).pack(fill="x")

tk.Button(menu_frame, text="🏠 Accueil", bg="#2ecc71", fg="white", font=("Arial", 12),
          relief="flat", cursor="hand2", command=lambda: afficher_page(page_accueil)).pack(fill="x", pady=5)
tk.Button(menu_frame, text="📋 Biens", bg="#2ecc71", fg="white", font=("Arial", 12),
          relief="flat", cursor="hand2", command=lambda: afficher_page(page_biens)).pack(fill="x", pady=5)
tk.Button(menu_frame, text="👥 Locataires", bg="#2ecc71", fg="white", font=("Arial", 12),
          relief="flat", cursor="hand2", command=lambda: afficher_page(page_locataires)).pack(fill="x", pady=5)

# Page d'accueil affichée par défaut
afficher_page(page_accueil)

fenetre.mainloop()

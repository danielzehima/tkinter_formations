import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

fenetre = ctk.CTk()
fenetre.title("Gestion Immobilière Moderne 🏠")
fenetre.geometry("900x500")

# --- Frames principales ---
frame_menu = ctk.CTkFrame(fenetre, width=200, corner_radius=0)
frame_menu.pack(side="left", fill="y")

frame_contenu = ctk.CTkFrame(fenetre, corner_radius=15)
frame_contenu.pack(expand=True, fill="both", padx=20, pady=20)

# --- Contenu du menu ---
ctk.CTkLabel(frame_menu, text="Menu", font=("Segoe UI", 18, "bold")).pack(pady=20)

def afficher_message(texte):
    for widget in frame_contenu.winfo_children():
        widget.destroy()
    ctk.CTkLabel(frame_contenu, text=texte, font=("Segoe UI", 22, "bold")).pack(pady=150)

boutons = [
    ("🏠 Accueil", "Bienvenue dans votre tableau de bord"),
    ("📋 Biens", "Liste des biens enregistrés"),
    ("👥 Locataires", "Gestion des locataires"),
    ("💰 Paiements", "Historique des paiements")
]

for texte, contenu in boutons:
    ctk.CTkButton(frame_menu, text=texte, width=180, command=lambda c=contenu: afficher_message(c)).pack(pady=10)

# --- Page d'accueil ---
afficher_message("Bienvenue dans votre tableau de bord")

fenetre.mainloop()

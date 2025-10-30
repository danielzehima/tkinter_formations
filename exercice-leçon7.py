"""💪 Exercice pratique

Crée une interface moderne avec :

Thème sombre

Une barre latérale (menu) avec 4 boutons

Une zone centrale affichant un texte selon le bouton cliqué

Des coins arrondis et un design épuré
"""

import customtkinter as ctk

ctk.set_appearance_mode("ligth")
ctk.set_default_color_theme("blue")

fenetre=ctk.CTk()
fenetre.geometry("700x450")
fenetre.title("Apparence moderne avec customtkinter")

#definir le menu lateral contenant les boutons
menu_lateral=ctk.CTkFrame(fenetre,bg_color="#7e3c4c",width=180,corner_radius=10)
menu_lateral.pack(side="left",fill="y")

conteneur=ctk.CTkFrame(fenetre,corner_radius=10)
conteneur.pack(expand=True,fill="both",pady=10,padx=10)

def affiche_message(texte):
    for widget in conteneur.winfo_children():
        widget.destroy()
    ctk.CTkLabel(conteneur,text=texte,font=("Segoe UI", 22, "bold")).pack(pady=90)

boutons = [
    ("🏠 Accueil", "Bienvenue dans votre tableau de bord"),
    ("📋 Biens", "Liste des biens enregistrés"),
    ("👥 Locataires", "Gestion des locataires"),
    ("💰 Paiements", "Historique des paiements")
]

for texte, contenu in boutons:
    ctk.CTkButton(menu_lateral,text=texte,width=180,command=lambda c=contenu:affiche_message(c)).pack(pady=10)


affiche_message("Bienvenue dans votre tableau de bord")




fenetre.mainloop()
import tkinter as tk

def centrer_fenetre(fenetre, largeur, hauteur):
    ecran_largeur = fenetre.winfo_screenwidth()
    ecran_hauteur = fenetre.winfo_screenheight()
    x = (ecran_largeur // 2) - (largeur // 2)
    y = (ecran_hauteur // 2) - (hauteur // 2)
    fenetre.geometry(f"{largeur}x{hauteur}+{x}+{y}")

fenetre = tk.Tk()
fenetre.title("Gestion Immobilière")
centrer_fenetre(fenetre, 1200, 720)
fenetre.config(bg="#d6eaf8")
fenetre.resizable(False, False)
#fenetre.iconbitmap("mon_logo.ico")  # mets ton propre .ico

label = tk.Label(fenetre, text="Bienvenue Dans votre tableau de bord 🐱‍👓", bg="#d6eaf8", font=("Arial", 18, "bold"), fg="#2c3e50")
label.pack(pady=50)

fenetre.mainloop()

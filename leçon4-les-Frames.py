import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Application Gestion Immobilière 🏠")
fenetre.geometry("800x500")
fenetre.config(bg="#ecf0f1")

# Frame du haut (en-tête)
frame_header = tk.Frame(fenetre, bg="#3498db", height=80)
frame_header.pack(fill="x")

# Frame du menu (gauche)
frame_menu = tk.Frame(fenetre, bg="#2ecc71", width=180)
frame_menu.pack(side="left", fill="y")

# Frame principale (contenu)
frame_main = tk.Frame(fenetre, bg="#f7f9f9")
frame_main.pack(expand=True, fill="both")

# Contenu de l'en-tête
titre = tk.Label(frame_header, text="Gestion Immobilière 🏠", bg="#3498db", fg="white", font=("Arial", 18, "bold"))
titre.pack(pady=20)

# Contenu du menu
boutons = ["🏡 Accueil", "📋 Biens", "👥 Locataires", "💰 Paiements", "⚙️ Paramètres"]

for b in boutons:
    tk.Button(frame_menu, text=b, bg="#27ae60", fg="white", font=("Arial", 12), relief="flat", cursor="hand2").pack(pady=10, fill="x")

# Contenu principal
message = tk.Label(frame_main, text="Bienvenue Daniel 👋\nChoisissez une option à gauche.", bg="#f7f9f9", fg="#2c3e50", font=("Arial", 16))
message.pack(pady=100)

fenetre.mainloop()

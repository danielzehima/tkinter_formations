import customtkinter as ctk

# Thème général
ctk.set_appearance_mode("dark")#light" ou "dark"
ctk.set_default_color_theme("blue")#"green", "dark-blue"

# Fenêtre principale
fenetre = ctk.CTk()
fenetre.title("Application moderne 🌈")
fenetre.geometry("600x400")

# Widgets modernes
label = ctk.CTkLabel(fenetre, text="Bienvenue Daniel 👋", font=("Segoe UI", 20, "bold"))
label.pack(pady=20)

entry = ctk.CTkEntry(fenetre, placeholder_text="Entrez votre nom...")
entry.pack(pady=10)

bouton = ctk.CTkButton(fenetre, text="Valider", fg_color="#2ecc71", hover_color="#27ae60")
bouton.pack(pady=20)

fenetre.mainloop()

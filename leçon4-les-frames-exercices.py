import tkinter as tk 
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
fenetre=ctk.CTk()

fenetre.geometry("900x450")
fenetre.title("Exercice frame")

#creation des frames

frame_haut=ctk.CTkFrame(fenetre,bg_color="blue",height=50)
frame_haut.pack(fill="x")

frame_gauche=ctk.CTkFrame(fenetre,bg_color="#023441",width=200)
frame_gauche.pack(side="left",fill="y")

frame_centre=ctk.CTkFrame(fenetre,bg_color="#7e4c3c")
frame_centre.pack(expand=True,fill="both")

label_titre=ctk.CTkLabel(frame_haut,text="Mon application de Gestion 🥡",font=("Arial",14,"bold"))
label_titre.pack(pady=50)

lbl_contenu=ctk.CTkLabel(frame_centre,text="Bienvenu dans le tableau de bord",font=("Times new roman",15,"bold"))
lbl_contenu.pack(pady=50)

mes_actions=["clients 👩","Biens 🐱‍🏍","Factures 💌"]

for c in mes_actions:
    ctk.CTkButton(frame_gauche,text=c,font=("Arial",12),bg_color="#3498db",fg_color="#e74c3c",cursor='hand2').pack(pady=10,fill="x")

    
fenetre.mainloop()
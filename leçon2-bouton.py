#importation de la biblithèque tkinter

import tkinter as tk
from tkinter import messagebox

#création d'une fenêtre
fenetre=tk.Tk()

#Modification du titre de  la fenêtre
fenetre.title("Première fenêtre")
fenetre.geometry("400x300")# dimension largeurxhauteur

def direBonjour():
    message.config(text="Bonjour les amis",fg="green")
    
def direBonsoir():
    message.config(text="Bonsoir",fg="blue")

def ferme():
    if messagebox.askyesno("confirmer","Êtes-vous sur de vouloir fermer?"):
        fenetre.destroy()
        
      
message=tk.Label(fenetre,text="Bienvenu",font=("Arial",14))

message.pack(pady=30)

#Ajoter un bouton
btn_bonjour=tk.Button(fenetre,text=" bonjour",font=("Arial",12),fg="white",cursor='hand2',command=direBonjour,bg="#123458")

btn_bonsoir=tk.Button(fenetre,text="Bonsoir", fg="white",cursor="hand2",font=("Arial",12),command=direBonsoir,bg="#879521")

btn_ferme=tk.Button(fenetre,text="Quitter",fg="white",cursor="hand2",font=("Arial",12),command=ferme,bg='#965872')

btn_bonjour.pack(padx=3)
btn_bonsoir.pack(pady=5)
btn_ferme.pack(pady=7)

#lancer la boucle fenetre obligatoire
fenetre.mainloop()
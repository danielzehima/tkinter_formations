#importation de la biblithèque tkinter

import tkinter as tk

#création d'une fenêtre
fenetre=tk.Tk()

#Modification du titre de  la fenêtre
fenetre.title("Première fenêtre")
fenetre.geometry("400x300")# dimension largeurxhauteur

#Ajouter un label
label_text=tk.Label(fenetre,text="Formation rapide tkinter python",font=("Arial",14),fg="green")
label1_text=tk.Label(fenetre,text="Nous irons jusqu'au bout avec python",font=("comics",12),fg="red")
label_text.pack(pady=30)
label1_text.pack(pady=50)

#lancer la boucle fenetre obligatoire
fenetre.mainloop()
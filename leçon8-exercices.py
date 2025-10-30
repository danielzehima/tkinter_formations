"""️⃣ Mini exercice

👉 Crée un formulaire “Ajouter Locataire” avec :

Nom complet

Téléphone

Email

Type de contrat (CTkOptionMenu)

Statut (CTkRadioButton → “Actif”, “Inactif”)

Bouton “Enregistrer” → affiche les infos saisies dans la console
"""
import customtkinter as ctk

ctk.set_appearance_mode("ligth")
ctk.set_default_color_theme("dark-blue")

fenetre=ctk.CTk()
fenetre.geometry("600x500")
fenetre.title("Formulaire de saisie")

def enregistrer():
    if txt_entry.get() and txt_email.get() and tel_entry.get() and menu_contrat.get() and statut.get():
        print("Enregistrement effectué avec succès")
    else:
        print("Attention! tous les champs doivent être renseignés")
        
lbl_nom=ctk.CTkLabel(fenetre,text="Nom :",font=("Arial",12))
lbl_nom.pack(pady=5)
txt_entry=ctk.CTkEntry(fenetre,placeholder_text="ex: Zehima")
txt_entry.pack(pady=5)

lbl_Tel=ctk.CTkLabel(fenetre,text="Telephone :",font=("Arial",12))
lbl_Tel.pack(pady=5)
tel_entry=ctk.CTkEntry(fenetre,placeholder_text="ex: 0710203602")
tel_entry.pack(pady=5)

lbl_email=ctk.CTkLabel(fenetre,text="Email:",font=("Arial",12))
lbl_email.pack(pady=5)
txt_email=ctk.CTkEntry(fenetre,placeholder_text="g@mail.com")
txt_email.pack(pady=5)

lbl_menu=ctk.CTkLabel(fenetre,text="Type de contrat:",font=("Arial",12))
lbl_menu.pack(pady=5)
menu_contrat=ctk.CTkOptionMenu(fenetre,values=["mensuel","Bail","annuel"])
menu_contrat.pack(pady=5)

lbl_stat=ctk.CTkLabel(fenetre,text="Statut",font=("Arial ",12))
lbl_stat.pack(pady=5)

statut=ctk.StringVar(value="Actif")
ctk.CTkRadioButton(fenetre,text="Actif",variable=statut,value="Actif").pack(pady=5)
ctk.CTkRadioButton(fenetre,text="inactif",variable=statut,value="Inactif").pack(pady=5)


btn_valider=ctk.CTkButton(fenetre,text="Enregistrer",font=("Arial black",14),cursor="hand2" ,command=enregistrer)
btn_valider.pack(pady=5)



fenetre.mainloop()

import tkinter as tk 

fenetre=tk.Tk()
fenetre.geometry("700x400")
fenetre.config(bg="#ecf0f1")
fenetre.title("Naviguer entre les pages")



menu_lateral=tk.Frame(fenetre,bg="#ecf0f1",width=150)
menu_lateral.pack(side="left",fill="y")
#creer un conteneur
conteneur=tk.Frame(fenetre,bg="#7c5896")
conteneur.pack(expand=True,fill="both")


#Definir les pages

page_accueil=tk.Frame(conteneur,bg="#9c5972")
page_biens=tk.Frame(conteneur,bg="#ec4c3c")
page_locataire=tk.Frame(conteneur,bg="#3498db")
page_paiement=tk.Frame(conteneur,bg="#2ecc71")

for page in (page_accueil,page_biens,page_locataire,page_paiement):
    page.place(relwidth=1,relheight=1)
    
# definir la fonction de navigation

def affiche_page(page):
    page.tkraise()
    
lbl_menu=tk.Label(menu_lateral,text="Menu Principal ",font=("Arial",12,"bold"))
lbl_menu.pack(fill="x")

mes_actions=["Accueil 🏠","Biens 🦸‍♀️","Locataires 📖","Paiement 💌"]


tk.Button(menu_lateral,text="Accueil",relief='flat',command=lambda:affiche_page(page_accueil),cursor="hand2",bg="black",fg="white").pack(pady=5,fill="x")
lbl_accueil=tk.Label(page_accueil,text="🏠 Accueil", font=("Arial",20,"bold"))
lbl_accueil.pack(pady=30)

tk.Button(menu_lateral,text="Biens",relief='flat',command=lambda:affiche_page(page_biens),cursor="hand2",bg="black",fg="white").pack(pady=5,fill="x")
lbl_bien=tk.Label(page_biens,text="🎁 Gestion des Biens", font=("Arial",20,"bold"))
lbl_bien.pack(pady=30)

tk.Button(menu_lateral,text="Locataire",relief='flat',command=lambda:affiche_page(page_locataire),cursor="hand2",bg="black",fg="white").pack(pady=5,fill="x")
lbl_locataire=tk.Label(page_locataire,text="🤦‍♂️Gestion des Locataires", font=("Arial",20,"bold"))
lbl_locataire.pack(pady=30)

tk.Button(menu_lateral,text="Paiements",relief='flat',command=lambda:affiche_page(page_paiement),cursor="hand2",bg="black",fg="white").pack(pady=5,fill="x")
lbl_paiement=tk.Label(page_paiement,text="💰 Gestion des paiementss", font=("Arial",20,"bold"))
lbl_paiement.pack(pady=30)




affiche_page(page_accueil)



fenetre.mainloop()
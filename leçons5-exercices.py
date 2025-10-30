import tkinter as tk 

fenetre=tk.Tk()
fenetre.geometry("700x400")
fenetre.config(bg="#ecf0f1")
fenetre.title("Naviguer entre les pages")

men_lateral=tk.Frame(fenetre,bg="#2e4c3c",width=180)
men_lateral.pack(side="left",fill="y")
#contener
contener=tk.Frame(fenetre,bg="#7e59c9")
contener.pack(expand=True,fill="both")
lb_lateral=tk.Label(men_lateral,text="Menu Général",font=("Arial",12,"bold"),fg="white", bg="#2e4c3c")
lb_lateral.pack(pady=5,fill="x")

#creation des pages
page_accueil=tk.Frame(contener,bg="#3498db")
page_biens=tk.Frame(contener,bg="#ecf0f1")
page_locataires=tk.Frame(contener,bg="#e74c3c")
page_proprietaires=tk.Frame(contener,bg="#9b59b6")
page_paiements=tk.Frame(contener,bg="#2ecc71")

#Fonctions des pages

for page in (page_accueil,page_biens,page_locataires,page_proprietaires,page_paiements):
    page.place(relheight=1,relwidth=1)

def affiche(page):
    page.tkraise()
    
# creer des boutons sur le menu_lateral

btn_acc=tk.Button(men_lateral,text="Accueil",font=("Arial",12),bg="black",fg="white",cursor="hand2",relief="flat",command=lambda:affiche(page_accueil))
btn_acc.pack(fill="x",pady=5)

btn_biens=tk.Button(men_lateral,text="Biens",font=("Arial",12),bg="black",fg="white",cursor="hand2",relief="flat",command=lambda: affiche(page_biens))
btn_biens.pack(fill="x",pady=5)

btn_locataires=tk.Button(men_lateral,text="Locataires",font=("Arial",12),fg="white",cursor="hand2",relief="flat",bg="black" ,command=lambda: affiche(page_locataires))
btn_locataires.pack(fill="x" ,pady=5)

btn_proprietaires=tk.Button(men_lateral,text="Proprietaires",font=("Arial",12),fg="white",cursor="hand2",relief="flat" ,bg="black" ,command=lambda: affiche(page_proprietaires))
btn_proprietaires.pack(fill="x",pady=5)

btn_paiements=tk.Button(men_lateral,text="Paiements",font=("Arial",12),fg="white",cursor="hand2",relief="flat", bg="black",command=lambda: affiche(page_paiements))
btn_paiements.pack(fill="x",pady=5)

#les differents labels dans les differentes pages
lbl_acc=tk.Label(page_accueil,text="Bienvenu dans le tableau de bord",font=("Arial",14,"bold"))
lbl_acc.pack(pady=30)

lbl_loc=tk.Label(page_locataires,text="Gestion des locataires",font=("Arial",14,"bold"))
lbl_loc.pack(pady=30)

lbl_pro=tk.Label(page_proprietaires,text="Gestion des propriétaires",font=("Arial",14,"bold"))
lbl_pro.pack(pady=30)

lbl_biens=tk.Label(page_biens,text="Gestion des Biens",font=("Arial",14,"bold"))
lbl_biens.pack(pady=30)

lbl_paie=tk.Label(page_paiements,text="Gestion des paiements",font=("Arial",14,"bold"))
lbl_paie.pack(pady=30)

affiche(page_accueil)

fenetre.mainloop()
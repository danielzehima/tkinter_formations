import tkinter as tk 

fenetre=tk.Tk()
fenetre.geometry("700x400")
fenetre.title("Exercice frame")

#creation des frames

frame_haut=tk.Frame(fenetre,bg="blue",height=80)
frame_haut.pack(fill="x")

frame_gauche=tk.Frame(fenetre,bg="#023441",width=180)
frame_gauche.pack(side="left",fill="y")

frame_centre=tk.Frame(fenetre,bg="#ffffff")
frame_centre.pack(expand=True,fill="both")

label_titre=tk.Label(frame_haut,text="Mon application de Gestion 🥡",font=("Arial",14,"bold"))
label_titre.pack(pady=50)

lbl_contenu=tk.Label(frame_centre,text="Bienvenu dans le tableau de bord",font=("Times new roman",15,"bold"))
lbl_contenu.pack(pady=50)

mes_actions=["clients 👩","Biens 🐱‍🏍","Factures 💌"]

for c in mes_actions:
    tk.Button(frame_gauche,text=c,font=("Arial",12),bg="#3498db",fg="#e74c3c",cursor='hand2').pack(pady=10,fill="x")
    
fenetre.mainloop()
import tkinter as tk

"""
Créer 2 labels Nom et email avec la fonction .grid()

"""
fenetre=tk.Tk()
fenetre.geometry("400x300")

#reation des labels
tk.Label(fenetre,text="Nom : ").grid(row=0,column=0,padx=10,pady=10)
tk.Label(fenetre,text="Email: ").grid(row=1,column=0,padx=10,pady=10)
tk.Button(fenetre,text="Envoyer ").grid(row=2,column=0,columnspan=2,padx=10,pady=10)
tk.Entry(fenetre).grid(row=0,column=1,padx=10,pady=10)
tk.Entry(fenetre).grid(row=1,column=1,padx=10,pady=10)



fenetre.mainloop()


import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Disposition avec place()")
fenetre.geometry("400x300")

tk.Label(fenetre, text="Bonjour !", bg="yellow").place(x=150, y=50)
tk.Button(fenetre, text="Clique ici").place(x=160, y=100)

fenetre.mainloop()

import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Disposition avec pack()")
fenetre.geometry("400x300")

label1 = tk.Label(fenetre, text="Haut", bg="lightblue")
label1.pack(side="top", fill="x")

label2 = tk.Label(fenetre, text="Bas", bg="lightgreen")
label2.pack(side="bottom", fill="x",padx=5,pady=5)

label3 = tk.Label(fenetre, text="Gauche", bg="lightpink")
label3.pack(side="left", fill="y",padx=10,pady=5)

label4 = tk.Label(fenetre, text="Droite", bg="orange")
label4.pack(side="right", fill="y",padx=5,pady=5)

fenetre.mainloop()

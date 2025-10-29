import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Disposition avec grid()")
fenetre.geometry("400x200")

tk.Label(fenetre, text="Nom :").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(fenetre).grid(row=0, column=1, padx=10, pady=10)

tk.Label(fenetre, text="Email :").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(fenetre).grid(row=1, column=1, padx=10, pady=10)

tk.Button(fenetre, text="Envoyer").grid(row=2, column=0, columnspan=2, pady=10)

fenetre.mainloop()

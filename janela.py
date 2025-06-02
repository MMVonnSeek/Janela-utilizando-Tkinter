import tkinter as tk
root = tk.Tk()
root.title("Título da Janela")
label = tk.Label(root, text="A janela foi criada")
label.pack(padx=100, pady=100)
root.mainloop()
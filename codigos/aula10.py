import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

#Label estático
ctk.CTkLabel(janela, text="Neste Label temos um texto estático").pack()

#Label dinâmica
#Introduzindo texto por input
"""text_var= ctk.StringVar(value=input("Digite seu nome: "))
lab = ctk.CTkLabel(janela, textvariable= text_var, text_color="blue", font=("arial bold", 16))
lab.pack()"""

#Introduzindo texto por entry
def enviar():
    print(entry.get())
    lab.configure(text=str(entry.get()))
    pass
lab = ctk.CTkLabel(janela, text="", text_color="blue", font=("arial bold", 16))
lab.pack()
entry = ctk.CTkEntry(janela, width=250)
entry.pack()
btn = ctk.CTkButton(janela, text="Enviar", width=250, command=enviar).pack(pady=20)

janela.mainloop()
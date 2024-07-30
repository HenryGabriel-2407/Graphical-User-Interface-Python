import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 17 - CheckBox", font=("arial bold", 20)).pack(pady= 5)

checkvar = ctk.StringVar(value="Ativado")

def evento():
    print(checkvar.get())
checkbox = ctk.CTkCheckBox(janela,width=200, text="Limão", variable=checkvar, onvalue="Ativado", offvalue="Desativado", command=evento).pack(pady=20)

janela.mainloop()
import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 20 - Place", font=("arial bold", 20)).pack(pady= 5)
butao = ctk.CTkButton(janela).place(x=20, y=150)
butao2 = ctk.CTkButton(janela, text="Botão").place(x=40, y=170)
butao3 = ctk.CTkButton(janela, text="HEHE").place(relx=0.2, rely=0.3) #está no 20% de x e 30% no y

janela.mainloop()
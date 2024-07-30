import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Sistema de Login") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.grid_columnconfigure((0,1), weight=1)
#ctk.CTkLabel(janela, text="Aula 22 - Posicionamento Grid", font=("arial bold", 20)).pack(pady= 5)

def clicar():
    print("Botão clicado")

btn = ctk.CTkButton(janela, text="Botão", command=clicar)
btn.grid(row = 0, column = 0, sticky="ew", columnspan=2)

checbox = ctk.CTkCheckBox(janela, text="Olá")
checbox.grid(row = 1, column = 0, pady = 20, sticky = "w")

checkbox2 = ctk.CTkCheckBox(janela, text="Sigma da Bahea").grid(row=1, column = 1, pady= 20)

janela.mainloop()
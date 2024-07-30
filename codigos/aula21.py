import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Sistema de Login") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 21 - Posicionamento do Widget", font=("arial bold", 20)).pack(pady= 5)

def evento():
    # Obter os valores dos campos de entrada usando o método get()
    username_value = leitura.get()
    password_value = leitura2.get()
    # Imprimir os valores reais digitados pelo usuário
    print(username_value)
    print(password_value)


username = ctk.CTkEntry(janela, placeholder_text="Digite seu username: ").pack(pady=30)
leitura = ctk.StringVar(username)

password = ctk.CTkEntry(janela, placeholder_text="Digite a senha: ", show="*").pack()
leitura2 = ctk.StringVar(password)

botao_login = ctk.CTkButton(janela, text="Login", command=evento).pack(pady=20)

janela.mainloop()
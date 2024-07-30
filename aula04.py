import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo
#janela.resizable(width= True, height= False) #largura pode variar mas a altura não

def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="#3299CC")
    nova_janela.geometry("250x250")

button = ctk.CTkButton(janela, text="Clica para abrir nova janela", command=nova_tela).place(x=300, y = 150) #criando botão com posição definida


janela.mainloop()
import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

#Caixa de Dialogo

def abrir():
    dialogo = ctk.CTkInputDialog(title="Digite alguma coisa",text="Digite seu número", entry_border_color="red")
    print(dialogo.get_input())

btn = ctk.CTkButton(janela, text="Abrir a caixa de Dialogo", command= abrir)
btn.pack()

janela.mainloop()
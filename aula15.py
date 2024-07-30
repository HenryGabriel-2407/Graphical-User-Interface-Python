import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 15 - SegmentButton", font=("arial bold", 20)).pack(pady= 5)

def butao(valores):
    label = ctk.CTkLabel(janela, width=400, text="Olá mundo!", font=("arial", 18)).pack(pady=10)
    
valores = ["Nome dos Livros", "Autores", "Ano", "ISBN", "Avaliação"]
seg = ctk.CTkSegmentedButton(janela, width=140,values=valores, command=butao).pack(pady = 20)

janela.mainloop()
import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 19 - ProgressBar", font=("arial bold", 20)).pack(pady= 5)
progres = ctk.IntVar()

progresso = ctk.CTkProgressBar(janela, orientation="vertical", variable=progres)
progresso.start()
progresso.place(x=600, y=60)
janela.mainloop()
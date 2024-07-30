import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

#Frames
frame = ctk.CTkFrame(janela, width=200, height= 300, fg_color= "#9400d3", border_color= "white", border_width=10, corner_radius= 20).place(x=20, y = 20)
frame2 = ctk.CTkFrame(janela, width=200, height=300, fg_color="#00008b").place(x=230, y= 20)
frame3 = ctk.CTkFrame(janela, width=200, height= 300, fg_color="#fffafa").place(x=440, y=20)
janela.mainloop()
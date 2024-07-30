import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 14", font=("arial bold", 20)).pack(pady= 5)

def slider_valor(value):
    print(value)

slider = ctk.CTkSlider(janela, width=400, from_=0, to=100, command=slider_valor, button_hover_color="green", button_length=10)
slider.pack(pady=10)

janela.mainloop()
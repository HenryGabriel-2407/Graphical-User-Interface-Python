import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 18 - RadioButton", font=("arial bold", 20)).pack(pady= 5)

radio = ctk.IntVar(value=0)

def evento():
    if radio.get() == 1:
        print("Limão")
    elif radio.get() == 2:
        print("Laranja")

radiobutton = ctk.CTkRadioButton(janela, width=200, text="Limão", command=evento, variable=radio, value=1).pack(pady=20)
radiobutton2 = ctk.CTkRadioButton(janela, width=200, text="Laranja", command=evento, variable=radio, value=2).pack(pady=20)

janela.mainloop()
#cv@bo-italia.com
import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 16 - Switch", font=("arial bold", 20)).pack(pady= 5)

switch_var = ctk.StringVar()

def evento():
    if switch_var.get() == "Ativado":
        ctk.set_appearance_mode("dark")
    elif switch_var.get() == "Desativado":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("system")
    print("Switch está ", switch_var.get())

switch = ctk.CTkSwitch(janela, text="Clica", width=200, command=evento, variable=switch_var, onvalue="Ativado", offvalue="Desativado").pack(pady=20)

janela.mainloop()
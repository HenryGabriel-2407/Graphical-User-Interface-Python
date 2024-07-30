import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

#Opção de Menu
ctk.CTkLabel(janela, text= "Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=20)
ctk.CTkLabel(janela, text="Escolha seu mês de nascimento", font=("bold", 16)).pack()

mes_var = ctk.StringVar(value="Escolha o mês")
def mes_escolhido(escolha):
    print(escolha)
meses = ["Janeiro", "Feveiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes = ctk.CTkOptionMenu(janela, values=meses, command= mes_escolhido, variable=mes_var, width=200, corner_radius=40, dropdown_fg_color="green") 
mes.pack(pady = 20)
#mes.set("Escolha")

janela.mainloop()
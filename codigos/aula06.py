import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

#Tabview (abas)
tabview = ctk.CTkTabview(janela, width=400, border_color="white", border_width=2, corner_radius=20, height= 300)
tabview.pack()
tabview.add("Nomes").grid()
tabview.add("Idades").grid()
tabview.add("Notas").grid()

tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Notas").grid_columnconfigure(0, weight=1)

nomes = ["Henry Gabriel", "Alessandra Bregadioli", "Eva Marie", "Pedro Gustavo"]
idades = [19, 21, 8, 20]
notas = [9, 9.3, 10.0, 8]

#Criação de frames
nome_frame = ctk.CTkFrame(tabview.tab("Nomes"))
nome_frame.pack(fill="both", expand=True)
idade_frame = ctk.CTkFrame(tabview.tab("Idades"))
idade_frame.pack(fill="both", expand=True)
notas_frame = ctk.CTkFrame(tabview.tab("Notas"))
notas_frame.pack(fill="both", expand=True)

#adicionando elementos
for nome in nomes:
    texto_nomes = ctk.CTkLabel(nome_frame, text=f"{nome}")
    texto_nomes.pack(pady=5)

for idade in idades:
    texto_idade = ctk.CTkLabel(idade_frame, text= f"{idade}")
    texto_idade.pack(pady=5)

for nota in notas:
    texto_notas = ctk.CTkLabel(notas_frame, text=f"{nota}")
    texto_notas.pack(pady=5)

janela.mainloop()
import tkinter as tk

janela = tk.Tk()
janela.title("Algoritmo de Zeller")
janela.geometry("400x400")
janela.configure(bg="#00194a")
titulo = tk.Label(janela, text="Calculadora do Algoritmo de Zeller", bg="#00194a", fg="white", font=("Arial", 16, "bold"))
titulo.pack(pady=15)

rotulo_dia = tk.Label(janela, text="Dia:", bg="#00194a", fg="white", font=("Arial", 12))
rotulo_dia.pack(pady=5)
entrada_dia = tk.Entry(janela, width=20)
entrada_dia.pack(pady=5)
rotulo_mes = tk.Label(janela, text="Mês:", bg="#00194a", fg="white", font=("Arial", 12))
rotulo_mes.pack(pady=5)
entrada_mes = tk.Entry(janela, width=20)
entrada_mes.pack(pady=5)
rotulo_ano = tk.Label(janela, text="Ano:", bg="#00194a", fg="white", font=("Arial", 12))
rotulo_ano.pack(pady=5)
entrada_ano = tk.Entry(janela, width=20)
entrada_ano.pack(pady=5)
opcao = tk.StringVar()
opcao.set("dc")  # valor inicial

radio_ac = tk.Radiobutton(janela, text="Antes de Cristo", variable=opcao, value="ac",
                            bg="#00194a", fg="white", selectcolor="#00194a",
                            font=("Arial", 11), activebackground="#00194a", activeforeground="white")
radio_ac.pack(pady=5)

radio_dc = tk.Radiobutton(janela, text="Depois de Cristo", variable=opcao, value="dc",
                            bg="#00194a", fg="white", selectcolor="#00194a",
                            font=("Arial", 11), activebackground="#00194a", activeforeground="white")
radio_dc.pack(pady=5)
resultado_label = tk.Label(janela, text="", bg="#00194a", fg="#ffffff", font=("Arial", 14, "bold"))
resultado_label.pack(pady=5)
def calcular():
    dia = int(entrada_dia.get())
    mes = int(entrada_mes.get())
    ano = int(entrada_ano.get())
    opcao_escolhida = opcao.get()

    if opcao_escolhida == "ac":
        ano = 1 - ano
    mes_mostrar = mes
    ano_mostrar = ano

    if ano_mostrar <= 0:
        ano_texto = str(1 - ano_mostrar) + " a.C."
    else:
        ano_texto = str(ano_mostrar) + " d.C."

    valida = True
    if mes < 1 or mes > 12:
        valida = False
    else:
        dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_no_mes[1] = 29
        maximo = dias_no_mes[mes-1]
        if dia < 1 or dia > maximo:
            valida = False

    if valida:
        def ajustar_mes_ano(mes, ano):
            if mes < 3:
                mes = mes + 12
                ano = ano - 1
            return mes, ano
        mes, ano = ajustar_mes_ano(mes, ano)
        k = ano % 100
        j = ano // 100
        q = dia
        parte_a = 13*(mes+1)//5
        parte_b = k//4
        parte_c = j//4
        h = (q+parte_a+k+parte_b+parte_c+5*j) % 7
        dias = ["Sábado", "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
        resultado_label.config(text=f"{dia}/{mes_mostrar}/{ano_texto} cai em uma {dias[h]}")

botao = tk.Button(janela, text="Calcular", command=calcular, bg="#3498db", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
botao.pack(pady=5)
janela.mainloop()
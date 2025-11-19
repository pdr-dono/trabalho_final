from tkinter import messagebox
import tkinter as tk

class BiotechEquations(tk.Tk): #Classe do menu principal
    def __init__(self): #método init contendo as configs da janela inicial
        super().__init__()
        self.geometry("500x325")
        self.title("Menu inicial")
        self.configure(bg="#CBA9F5")

        def abrir_molaridade(self): #função que abre a janela de calculo de molaridade
            molaridade_window = Molaridade(self)
            molaridade_window.grab_set() # faz com que a somente a janela ativa fique em uso, as outras ficam block

        def abrir_calculadora(self): #função que abre a janela da calculadora
            calculadora_window = Calculadora(self)
            calculadora_window.grab_set() # faz com que a somente a janela ativa fique em uso, as outras ficam block
            
        def abrir_diluicao(self): #função que abre a janela de calculo de diluicao
            diluicao_window = Diluicao(self)
            diluicao_window.grab_set() # faz com que a somente a janela ativa fique em uso, as outras ficam block

        label_sobre = tk.Label(self, text="Lab hacks", fg="#ffe0f4", bg="#CBA9F5", font=("MV Boli", 50)) #label da tela principal
        label_sobre.pack()
        
        # Frame que vai conter os botões
        frame_botoes = tk.Frame(self, bg="#CBA9F5")
        frame_botoes.pack(pady=10, fill="both")
        
        # Configura o grid do frame contendo os botões
        frame_botoes.grid_columnconfigure(0, weight=1)
        frame_botoes.grid_rowconfigure(0, weight=1)
        frame_botoes.grid_rowconfigure(1, weight=1)
        
        # Botão molaridade
        botao_molaridade = tk.Button(
            frame_botoes, 
            text="Cálculo de Molaridade de uma solução", 
            command=self.abrir_molaridade,
            bg="#ffe0f4", fg="#CBA9F5",
            borderwidth=5, highlightthickness=0, relief="groove",
            font=("Times New Roman", 14))
        botao_molaridade.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Botão calculadora
        botao_calculadora = tk.Button(
            frame_botoes, 
            text="Calculadora simples", 
            command=self.abrir_calculadora,
            bg="#ffe0f4", fg="#CBA9F5",
            borderwidth=5, highlightthickness=0, relief="groove",
            font=("Times New Roman", 14))
        botao_calculadora.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        # Botão diluição
        botao_diluicao = tk.Button(
            frame_botoes, 
            text="Cálculo de diluição direta de solução estoque", 
            command=self.abrir_diluicao,
            bg="#ffe0f4", fg="#CBA9F5",
            borderwidth=5, highlightthickness=0, relief="groove",
            font=("Times New Roman", 14))
        botao_diluicao.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

#funções para abrir as janelas dentro da class BiotechEquations e fora da def init
    def abrir_molaridade(self): #função que abre a janela de calculo de molaridade
        molaridade_window = Molaridade(self)
        molaridade_window.grab_set()  # faz com que a somente a janela ativa fique em uso, as outras ficam block
        
    def abrir_calculadora(self): #função que abre a janela da calculadora
        calculadora_window = Calculadora(self)
        calculadora_window.grab_set() # faz com que a somente a janela ativa fique em uso, as outras ficam block
        
    def abrir_diluicao(self): #função que abre a janela de calculo de diluicao
        diluicao_window = Diluicao(self)
        diluicao_window.grab_set() # faz com que a somente a janela ativa fique em uso, as outras ficam block
        
#opções da janela inicial

class Molaridade(tk.Toplevel): #janela de calculo de molaridade
    def __init__(self, master=None): #função init contendo as configs da janela
        super().__init__(master)
        self.geometry("500x325")
        self.title("Molaridade")
        self.configure(bg="#ffe0f4") 

#Teclado numérico
        numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', 'Deletar','Retornar', 'Avançar']  
        for i, val in enumerate(numeros):
            row = i // 3
            col = i % 3
            btn = tk.Button(self, text=val, bg="#ffe0f4", fg="black",
                            borderwidth=0.5, highlightthickness=0, relief="ridge",
                            font=("Times New Roman", 14), width=6, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if val == "Deletar":
                btn.config(command=self.deletar_valor)
            elif val == "Avançar":
                btn.config(command=self.avancar_entrada)
            elif val == "Retornar":
                btn.config(command=self.retornar_entrada)
            else:
                btn.config(command=lambda v=val: self.inserir_valor(v))
                
        #entries da janela e suas configurações
        self.entries = []
        self.gramas = tk.Entry(self)
        self.gramas.config(width=20, borderwidth=5, relief="sunken", bg="#CBA9F5")
        self.gramas.place(x=264, y=40)
        self.entries.append(self.gramas)

        self.massamolar = tk.Entry(self)
        self.massamolar.config(width=20, borderwidth=5, relief="sunken", bg="#CBA9F5")
        self.massamolar.place(x=264, y=100)
        self.entries.append(self.massamolar)

        self.volume = tk.Entry(self)
        self.volume.config(width=20, borderwidth=5, relief="sunken", bg="#CBA9F5")
        self.volume.place(x=264, y=160)
        self.entries.append(self.volume)

        #labels associadas as entries informando o usuários o que deve escrevere suas configurações
        self.gramas2 = tk.Label(self)
        self.gramas2.place(x=264, y=10)
        self.gramas2.config(text="Massa(g) do soluto:", font=("Times New Roman", 12), fg="black", bg="#ffe0f4")
        
        self.massamolar2 = tk.Label(self)
        self.massamolar2.place(x=264, y=70)
        self.massamolar2.config(text="Massa molar(g/mol) do soluto:", font=("Times New Roman", 12), fg="black", bg="#ffe0f4")
        
        self.volume2 = tk.Label(self)
        self.volume2.place(x=264, y=130)
        self.volume2.config(text="Volume(L) da solução:", font=("Times New Roman", 12), fg="black", bg="#ffe0f4")
        
        self.res = tk.Label(self)
        self.res.place(x=250, y=205)
        self.res.config(text="Resultado:", font=("Times New Roman", 12), fg="black", bg="#ffe0f4")

        #inicializa a janela com a primeira entrada ja selecionada e identifica qual entrada está selecionada
        self.entrada_ativa = 0
        self.entries[self.entrada_ativa].focus_set()

        #Label que vai aparecer quando o botão avançar por apertado por ultimo para gerar o resultado
        self.resultado = tk.Label(self, text="", font=("Times New Roman", 12), fg="#F500A1", bg="#ffe0f4")
        self.resultado.place(x=316, y=205)

#Funções do teclado numérico
    def inserir_valor(self, valor): #função que conecta o teclado numérico a entrada selecionada no momento digitando o numero referente ao botao pressionado
        entrada = self.entries[self.entrada_ativa]
        entrada.insert(tk.END, valor)

    def deletar_valor(self): #função que deleta o valor digitado anteriormente
        entrada = self.entries[self.entrada_ativa]
        texto = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(0, texto[:-1])
        
    def retornar_entrada(self): #função que seleciona a entrada anterior
        if self.entrada_ativa > 0:
            self.entrada_ativa -= 1
            self.entries[self.entrada_ativa].focus_set()
        else:
            print("Primeira entrada já selecionada")

    def avancar_entrada(self): #função que seleciona a próxima entrada
        if self.entrada_ativa < len(self.entries) - 1:
            self.entrada_ativa += 1
            self.entries[self.entrada_ativa].focus_set()
        else:
            try: #detecta quando o avançar é clicado pela ultima vez e roda a equação com base nos dados fornecidos
                valor1 = float(self.gramas.get())
                valor2 = float(self.massamolar.get())
                valor3 = float(self.volume.get())
    
                if valor1 == 0 or valor2 == 0 or valor3 == 0:
                    messagebox.showerror("ERROR", "⚠️ Número inválido! ⚠️") #janela de mensagem de erro 
                else:
                    molaridade = valor1 / (valor2 * valor3)
                    self.resultado.config(text=f"Molaridade = {molaridade:.4f} mol/L") 
            except ValueError:
                messagebox.showerror("ERROR", "⚠️ Número inválido! ⚠️") #janela de mensagem de erro 
                return

class Calculadora(tk.Toplevel): #janela da calculadora
    def __init__(self, master=None): #função init contendo as configs da janela
        super().__init__(master)
        self.geometry("306x375")
        self.title("Calculadora simples")
        self.configure(bg="#ffe0f4")

#entry da calculadora
        self.entrada = tk.Entry(self)
        self.entrada.grid(row=0, column=0, columnspan=4, pady=(10, 20))
        self.entrada.config(width=45, borderwidth=5, relief="sunken", bg="#CBA9F5")
        
#Teclado numérico
        numeros = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '÷', '.', '0', 'Deletar','x', '(', ')', '=']  
        for i, val in enumerate(numeros):
            row = (i // 4) + 2  # começa na linha 2 (pulando linha 1)
            col = i % 4
            btn = tk.Button(self, text=val, bg="#ffe0f4", fg="black",
                            borderwidth=0.5, highlightthickness=0, relief="ridge",
                            font=("Times New Roman", 14), width=6, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if val == "Deletar":
                btn.config(command=self.deletar_valor)
            elif val == "=":
                btn.config(command=self.calcular)
            else:
                btn.config(command=lambda v=val: self.inserir_valor(v))

#Funções do teclado numérico
    def inserir_valor(self, valor): #função que conecta o teclado numérico a entrada selecionada no momento digitando o numero referente ao botao pressionado
        entrada = self.entrada
        entrada.insert(tk.END, valor)

    def deletar_valor(self): #função que deleta o valor digitado anteriormente
        entrada = self.entrada
        texto = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(0, texto[:-1])

    def calcular(self):
        try:
            expressao = self.entrada.get()
    
            # Substitui 'x' por '*', caso o usuário use 'x' para multiplicação.
            expressao = expressao.replace('x', '*').replace('÷', '/')
            
            # Avaliação segura da expressão (evita eval puro).
            resultado = eval(expressao, {"__builtins__": None}, {})
    
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except:
            self.entrada.delete(0, tk.END)
            messagebox.showerror("ERROR", "⚠️ Erro no cálculo! ⚠️") #janela de mensagem de erro 

#janela de calculo de diluição
class Diluicao(tk.Toplevel):
    #método init contendo as configs da janela
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("500x325")
        self.title("Diluição direta")
        self.configure(bg="#CBA9F5")

        # teclado numérico
        numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', 'Deletar','Retornar', 'Avançar']
        for i, val in enumerate(numeros):
            row = i // 3
            col = i % 3
            btn = tk.Button(self, text=val, bg="#CBA9F5", fg="black",
                            borderwidth=0.5, highlightthickness=0, relief="ridge",
                            font=("Times New Roman", 14), width=6, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if val == "Deletar":
                btn.config(command=self.deletar_valor)
            elif val == "Avançar":
                btn.config(command=self.avancar_entrada)
            elif val == "Retornar":
                btn.config(command=self.retornar_entrada)
            else:
                btn.config(command=lambda v=val: self.inserir_valor(v))

        # entradas da janela
        self.entries2 = []
        self.molari = tk.Entry(self)
        self.molari.config(width=20, borderwidth=5, relief="sunken", bg="#ffe0f4")
        self.molari.place(x=264, y=30)
        self.entries2.append(self.molari)

        self.concen = tk.Entry(self)
        self.concen.config(width=20, borderwidth=5, relief="sunken", bg="#ffe0f4")
        self.concen.place(x=264, y=75)
        self.entries2.append(self.concen)

        # labels da janela
        self.molari2 = tk.Label(self)
        self.molari2.place(x=264, y=10)
        self.molari2.config(text="Molaridade da solução estoque (M):", font=("Times New Roman", 12), fg="black", bg="#CBA9F5")

        self.concen2 = tk.Label(self)
        self.concen2.place(x=264, y=55)
        self.concen2.config(text="Concentração desejada (μM):", font=("Times New Roman", 12), fg="black", bg="#CBA9F5")

        self.res = tk.Label(self)
        self.res.place(x=264, y=110)
        self.res.config(text="""OBS: Volume retirado da
 solução estoque: 1 μL""", font=("Times New Roman", 12), fg="#A000F5", bg="#CBA9F5")

        #label que aparece somente quando o botao avançar é clicado pela ultima vez
        self.resultado = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#CBA9F5")
        self.resultado.place(x=264, y=170)
        self.resultado2 = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#CBA9F5")
        self.resultado2.place(x=264, y=220)

        # inicia a janela com a primeira entrada seleciona e detecta qual entry ta selecionada
        self.entrada_ativa = 0
        self.entries2[self.entrada_ativa].focus_set()

#funções da classe diluicao
    
    def inserir_valor(self, valor): #função que insere o valor referente ao botao selecionado no teclado numerico na entrada selecionada
        entrada = self.entries2[self.entrada_ativa]
        entrada.insert(tk.END, valor)

    
    def deletar_valor(self): #função que deleta o ultimo valor digitado na entrada selecionada
        entrada = self.entries2[self.entrada_ativa]
        texto = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(0, texto[:-1])

    
    def retornar_entrada(self): #função que seleciona a entrada anterior
        if self.entrada_ativa > 0:
            self.entrada_ativa -= 1
            self.entries2[self.entrada_ativa].focus_set()
        else:
            print("Primeira entrada já selecionada")

    
    def avancar_entrada(self): #função que seleciona a próxima entrada
        if self.entrada_ativa < len(self.entries2) - 1:
            self.entrada_ativa += 1
            self.entries2[self.entrada_ativa].focus_set()
        else:
            try: #detecta quando o avançar é clicado pela ultima vez e roda a equação com base nos dados fornecidos
                C1 = float(self.molari.get())        # solução estoque (M)
                C2 = float(self.concen.get())        # concentração desejada (μM)
                V_estoque = 1                        # volume retirado da solução estoque (μL)
                if C1 == 0 or C2 == 0:
                    messagebox.showerror("ERROR", "⚠️ Número inválido! ⚠️") #janela de mensagem de erro 
                else:
                    # transforma C1 para μM
                    C1_um = C1 * 1e6
                    # calcula volume final da solução diluída
                    V_final = (C1_um * V_estoque) / C2  # resultado em μL
                    solvente = V_final - V_estoque
                    self.resultado.config(text=f"Volume final = {V_final:.2f} μL") #converte o valor para a medida correta
                    self.resultado2.config(text=f"Adicione {solvente:.2f} μL de solvente")
            except ValueError:
                messagebox.showerror("ERROR", "⚠️ Número inválido! ⚠️") #janela de mensagem de erro 



if __name__ == "__main__": #garante que o código rodará bem em outra plataforma
    app = BiotechEquations() #anexa a classe no tkinter
    app.mainloop() #possibilita a abertura da janela 
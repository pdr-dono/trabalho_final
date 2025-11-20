from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class BiotechEquations(tk.Tk): #Classe do menu principal
    def __init__(self): #método init contendo as configs da janela inicial
        super().__init__()
        self.geometry("500x325")
        self.title("Menu inicial")
        self.configure(bg="#FACAE2")
        self.resizable(False, False)
       
        #estabelece a barra de menu no topo da janela
        menubar = tk.Menu(self)
        self.configure(menu=menubar)
        arqmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Conversões", menu=arqmenu)
        arqmenu.add_command(label="Unidades de massa",command=self.abrir_conversoes)
        arqmenu.add_command(label="Unidades de volume",command=self.abrir_conversoes2)
        
        #label do titulo principal da janela
        label_sobre = tk.Label(self, text="Lab hacks", fg="#501A35", bg="#FACAE2", font=("MV Boli", 50)) #label da tela principal
        label_sobre.pack()
        
        # Frame que vai conter os botões
        frame_botoes = tk.Frame(self, bg="#FACAE2")
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
            bg="#7A3C5B", fg="#FACAE2",
            borderwidth=5, highlightthickness=0, relief="groove",
            font=("Times New Roman", 14))
        botao_molaridade.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Botão calculadora
        botao_calculadora = tk.Button(
            frame_botoes, 
            text="Calculadora simples", 
            command=self.abrir_calculadora,
            bg="#7A3C5B", fg="#FACAE2",
            borderwidth=5, highlightthickness=0, relief="groove",
            font=("Times New Roman", 14))
        botao_calculadora.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        # Botão diluição
        botao_diluicao = tk.Button(
            frame_botoes, 
            text="Cálculo de diluição direta de solução estoque", 
            command=self.abrir_diluicao,
            bg="#7A3C5B", fg="#FACAE2",
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
        
    def abrir_conversoes(self):
        conversoes_window = Conversoes_massa(self)
        conversoes_window.grab_set()
        
    def abrir_conversoes2(self):
        conversoes_window = Conversoes_volume(self)
        conversoes_window.grab_set()
        
class Conversoes_massa(tk.Toplevel): #opções da janela inicial
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("450x400")
        self.title("Conversões")
        self.configure(bg="#BAE5FA")
        self.resizable(False, False)
        
        self.entries = []
        #entry da conversão de massas
        self.massa_entrada=tk.Entry(self)
        self.massa_entrada.grid(row=0, column=0, columnspan=4, pady=(10, 20))
        self.massa_entrada.config(width=35, borderwidth=5, relief="sunken", bg="#1F4050", fg="white")
        self.entries.append(self.massa_entrada)
        
        #inicializa a janela com a primeira entrada ja selecionada e identifica qual entrada está selecionada
        self.entrada_ativa = 0
        self.entries[self.entrada_ativa].focus_set()
        
        # Lista de unidades
        unidades = ["Quilograma (kg)", "Grama (g)", "Miligrama (mg)", "Micrograma (μg)", "Nanograma (ng)"]
        
        # Combobox para unidades
        self.combo_unidade = ttk.Combobox(self, values=unidades, font=("Times New Roman", 14), width=10, state="readonly")
        self.combo_unidade.set("unidade")  # define o valor inicial
        self.combo_unidade.grid(row=0, column=4, columnspan=4, pady=(10,20))
        
            #labels resultado
        self.resultados = []
        self.resultado_kg = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#BAE5FA")
        self.resultado_kg.place(x=250,y=63)
        self.resultados.append(self.resultado_kg)
        
        self.resultado_g = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#BAE5FA")
        self.resultado_g.place(x=250,y=123)
        self.resultados.append(self.resultado_g)
        
        self.resultado_mg = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#BAE5FA")
        self.resultado_mg.place(x=250,y=183)
        self.resultados.append(self.resultado_mg)
        
        self.resultado_μg = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#BAE5FA")
        self.resultado_μg.place(x=250,y=243)
        self.resultados.append(self.resultado_μg)
        
        self.resultado_ng = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#BAE5FA")
        self.resultado_ng.place(x=250,y=303)
        self.resultados.append(self.resultado_ng)
        
#Teclado numérico
        numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0','Deletar','Calcular']  
        for i, val in enumerate(numeros):
            row = (i // 3) + 2  # começa na linha 2 (pulando linha 1)
            col = i % 3
            btn = tk.Button(self, text=val, bg="#45687A", fg="white",
                            borderwidth=0.5, highlightthickness=0, relief="ridge",
                            font=("Times New Roman", 14), width=6, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if val == "Deletar":
                btn.config(command=self.deletar_valor)
            elif val == "Calcular":
                btn.grid(row=row, column=col, padx=5, pady=15, sticky="nsew", columnspan=3)
                btn.config(command=self.conversao)
            else:
                btn.config(command=lambda v=val: self.inserir_valor(v))

#Funções do teclado numérico
    def inserir_valor(self, valor): #função que conecta o teclado numérico a entrada selecionada no momento digitando o numero referente ao botao pressionado
        massa_entrada = self.massa_entrada
        massa_entrada.insert(tk.END, valor)

    def deletar_valor(self): #função que deleta o valor digitado anteriormente
        massa_entrada = self.massa_entrada
        texto = massa_entrada.get()
        massa_entrada.delete(0, tk.END)
        massa_entrada.insert(0, texto[:-1])
            
    #função que calcula a conversao de uma unidade para outra
    def conversao(self):
        valor = float(self.massa_entrada.get())
        unidade = self.combo_unidade.get()
        if unidade == "Quilograma (kg)":
            kg = valor
            g = kg * 1e3
            mg = kg * 1e6
            μg = kg * 1e9
            ng = kg * 1e12
        elif unidade == "Grama (g)":
            kg = valor / 1e3
            g = valor
            mg = valor * 1e3
            μg = valor * 1e6
            ng = valor * 1e9
        elif unidade == "Miligrama (mg)":
            kg = valor / 1e6
            g = valor / 1e3
            mg = valor
            μg = valor * 1e3
            ng = valor * 1e6
        elif unidade == "Micrograma (μg)":
            kg = valor / 1e9
            g = valor / 1e6
            mg = valor / 1e3
            μg = valor
            ng = valor * 1e3
        elif unidade == "Nanograma (ng)":
            kg = valor / 1e12
            g = valor / 1e9
            mg = valor / 1e6
            μg = valor / 1e3
            ng = valor
        else:
            messagebox.showerror("ERROR", "⚠️ Selecione uma unidade! ⚠️") #janela de mensagem de erro
            return
        self.resultado_kg.config(text=f"{kg:.6g} kg")
        self.resultado_g.config(text=f"{g:.6g} g")
        self.resultado_mg.config(text=f"{mg:.6g} mg")
        self.resultado_μg.config(text=f"{μg:.6g} μg")
        self.resultado_ng.config(text=f"{ng:.6g} ng")
        
class Conversoes_volume(tk.Toplevel):  # opções da janela inicial
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("450x400")
        self.title("Unidade de volume")
        self.configure(bg="#FAAC9F")
        self.resizable(False, False)

        self.entries = []
        # Entry da conversão de volumes
        self.volume_entrada = tk.Entry(self)
        self.volume_entrada.grid(row=0, column=0, columnspan=4, pady=(10, 20))
        self.volume_entrada.config(width=35, borderwidth=5, relief="sunken", bg="#502D27", fg="white")
        self.entries.append(self.volume_entrada)

        # Inicializa a janela com a primeira entrada já selecionada e identifica qual entrada está selecionada
        self.entrada_ativa = 0
        self.entries[self.entrada_ativa].focus_set()

        # Lista de unidades
        unidades = ["Litro (L)", "Mililitro (mL)", "Microlitro (µL)", "Nanolitro (nL)", "Picolitro (pL)"]

        # Combobox para unidades
        self.combo_unidade = ttk.Combobox(self, values=unidades, font=("Times New Roman", 14), width=12, state="readonly")
        self.combo_unidade.set("unidade")  # define o valor inicial
        self.combo_unidade.grid(row=0, column=4, columnspan=4, pady=(10, 20))

        # Labels para resultado, com nomes coerentes
        self.resultado_L = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#FAAC9F")
        self.resultado_L.place(x=250, y=63)

        self.resultado_mL = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#FAAC9F")
        self.resultado_mL.place(x=250, y=123)

        self.resultado_μL = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#FAAC9F")
        self.resultado_μL.place(x=250, y=183)

        self.resultado_nL = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#FAAC9F")
        self.resultado_nL.place(x=250, y=243)

        self.resultado_pL = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#FAAC9F")
        self.resultado_pL.place(x=250, y=303)

        # Teclado numérico
        numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', 'Deletar', 'Calcular']
        for i, val in enumerate(numeros):
            row = (i // 3) + 2  # começa na linha 2 (pulando linha 1)
            col = i % 3
            btn = tk.Button(self, text=val, bg="#502D27", fg="white",
                            borderwidth=0.5, highlightthickness=0, relief="ridge",
                            font=("Times New Roman", 14), width=6, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if val == "Deletar":
                btn.config(command=self.deletar_valor)
            elif val == "Calcular":
                btn.grid(row=row, column=col, padx=5, pady=15, sticky="nsew", columnspan=3)
                btn.config(command=self.conversao_volume)
            else:
                btn.config(command=lambda v=val: self.inserir_valor(v))

    # Funções do teclado numérico
    def inserir_valor(self, valor):
        self.volume_entrada.insert(tk.END, valor)

    def deletar_valor(self):
        texto = self.volume_entrada.get()
        self.volume_entrada.delete(0, tk.END)
        self.volume_entrada.insert(0, texto[:-1])

    # Função que calcula a conversão de volume entre as unidades selecionadas
    def conversao_volume(self):
        valor = float(self.volume_entrada.get())
        unidade = self.combo_unidade.get()
        if unidade == "Litro (L)":
            L = valor
            mL = valor * 1e3
            μL = valor * 1e6
            nL = valor * 1e9
            pL = valor * 1e12
        elif unidade == "Mililitro (mL)":
            L = valor / 1e3
            mL = valor
            μL = valor * 1e3
            nL = valor * 1e6
            pL = valor * 1e9
        elif unidade == "Microlitro (µL)":
            L = valor / 1e6
            mL = valor / 1e3
            μL = valor
            nL = valor * 1e3
            pL = valor * 1e6
        elif unidade == "Nanolitro (nL)":
            L = valor / 1e9
            mL = valor / 1e6
            μL = valor / 1e3
            nL = valor
            pL = valor * 1e3
        elif unidade == "Picolitro (pL)":
            L = valor / 1e12
            mL = valor / 1e9
            μL = valor / 1e6
            nL = valor / 1e3
            pL = valor
        else:
            messagebox.showerror("ERROR", "⚠️ Selecione uma unidade! ⚠️")
            return

        self.resultado_L.config(text=f"{L:.6g} L")
        self.resultado_mL.config(text=f"{mL:.6g} mL")
        self.resultado_μL.config(text=f"{μL:.6g} µL")
        self.resultado_nL.config(text=f"{nL:.6g} nL")
        self.resultado_pL.config(text=f"{pL:.6g} pL")


class Molaridade(tk.Toplevel): #janela de calculo de molaridade
    def __init__(self, master=None): #função init contendo as configs da janela
        super().__init__(master)
        self.master = master
        self.geometry("500x325")
        self.title("Molaridade")
        self.configure(bg="#9CCF9C") 
        self.resizable(False, False)

#configura a barra de menu na janela de molaridade
        menubar = tk.Menu(self)
        self.configure(menu=menubar)
        arqmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Conversões", menu=arqmenu)
        arqmenu.add_command(label="Unidades de massa",command=self.abrir_conversoes)
        arqmenu.add_command(label="Unidades de volume",command=self.abrir_conversoes2)
        
#Teclado numérico
        numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', 'Deletar','Retornar', 'Avançar']  
        for i, val in enumerate(numeros):
            row = i // 3
            col = i % 3
            btn = tk.Button(self, text=val, bg="#043304", fg="white",
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
        self.gramas.config(width=20, borderwidth=5, relief="sunken", bg="#043304", fg="white")
        self.gramas.place(x=264, y=40)
        self.entries.append(self.gramas)

        self.massamolar = tk.Entry(self)
        self.massamolar.config(width=20, borderwidth=5, relief="sunken", bg="#043304", fg="white")
        self.massamolar.place(x=264, y=100)
        self.entries.append(self.massamolar)

        self.volume = tk.Entry(self)
        self.volume.config(width=20, borderwidth=5, relief="sunken", bg="#043304", fg="white")
        self.volume.place(x=264, y=160)
        self.entries.append(self.volume)

        #labels associadas as entries informando o usuários o que deve escrevere suas configurações
        self.gramas2 = tk.Label(self)
        self.gramas2.place(x=264, y=10)
        self.gramas2.config(text="Massa(g) do soluto:", font=("Times New Roman", 12), fg="white", bg="#9CCF9C")
        
        self.massamolar2 = tk.Label(self)
        self.massamolar2.place(x=264, y=70)
        self.massamolar2.config(text="Massa molar(g/mol) do soluto:", font=("Times New Roman", 12), fg="white", bg="#9CCF9C")
        
        self.volume2 = tk.Label(self)
        self.volume2.place(x=264, y=130)
        self.volume2.config(text="Volume(L) da solução:", font=("Times New Roman", 12), fg="white", bg="#9CCF9C")
        
        self.res = tk.Label(self)
        self.res.place(x=250, y=205)
        self.res.config(text="Resultado:", font=("Times New Roman", 12), fg="white", bg="#9CCF9C")

        #inicializa a janela com a primeira entrada ja selecionada e identifica qual entrada está selecionada
        self.entrada_ativa = 0
        self.entries[self.entrada_ativa].focus_set()

        #Label que vai aparecer quando o botão avançar por apertado por ultimo para gerar o resultado
        self.resultado = tk.Label(self, text="", font=("Times New Roman", 12), fg="white", bg="#9CCF9C")
        self.resultado.place(x=316, y=205)

#função que permite abrir o menu de conversões
    def abrir_conversoes(self):
            self.master.abrir_conversoes()
            
    def abrir_conversoes2(self):
        conversoes_window = Conversoes_volume(self)
        conversoes_window.grab_set()
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
        self.master = master
        self.geometry("306x375")
        self.title("Calculadora simples")
        self.configure(bg="#FADF7A")
        self.resizable(False, False)

#configura a barra de menu na janela da calculadora
        menubar = tk.Menu(self)
        self.configure(menu=menubar)
        arqmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Conversões", menu=arqmenu)
        arqmenu.add_command(label="Unidades de massa",command=self.abrir_conversoes)
        arqmenu.add_command(label="Unidades de volume",command=self.abrir_conversoes2)
        
#entry da calculadora
        self.entrada = tk.Entry(self)
        self.entrada.grid(row=0, column=0, columnspan=4, pady=(10, 20))
        self.entrada.config(width=45, borderwidth=5, relief="sunken", bg="#332D18", fg="white")
        
#Teclado numérico
        numeros = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '÷', '.', '0', 'Deletar','x', '(', ')', '=']  
        for i, val in enumerate(numeros):
            row = (i // 4) + 2  # começa na linha 2 (pulando linha 1)
            col = i % 4
            btn = tk.Button(self, text=val, bg="#332D18", fg="white",
                            borderwidth=0.5, highlightthickness=0, relief="ridge",
                            font=("Times New Roman", 14), width=6, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if val == "Deletar":
                btn.config(command=self.deletar_valor)
            elif val == "=":
                btn.config(command=self.calcular)
            else:
                btn.config(command=lambda v=val: self.inserir_valor(v))

#função que permite abrir o menu de conversões
    def abrir_conversoes(self):
            self.master.abrir_conversoes()

    def abrir_conversoes2(self):
        conversoes_window = Conversoes_volume(self)
        conversoes_window.grab_set()
            
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
        self.master = master
        self.geometry("500x325")
        self.title("Diluição direta")
        self.configure(bg="#B888CF")
        self.resizable(False, False)

#configura a barra de menu na janela da diluição
        menubar = tk.Menu(self)
        self.configure(menu=menubar)
        arqmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Conversões", menu=arqmenu)
        arqmenu.add_command(label="Unidades de massa",command=self.abrir_conversoes)
        arqmenu.add_command(label="Unidades de volume",command=self.abrir_conversoes2)
        
        # teclado numérico
        numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', 'Deletar','Retornar', 'Avançar']
        for i, val in enumerate(numeros):
            row = i // 3
            col = i % 3
            btn = tk.Button(self, text=val, bg="#2A1833", fg="white",
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
        self.molari.config(width=20, borderwidth=5, relief="sunken", bg="#2A1833", fg="white")
        self.molari.place(x=264, y=30)
        self.entries2.append(self.molari)

        self.concen = tk.Entry(self)
        self.concen.config(width=20, borderwidth=5, relief="sunken", bg="#2A1833", fg="white")
        self.concen.place(x=264, y=75)
        self.entries2.append(self.concen)

        # labels da janela
        self.molari2 = tk.Label(self)
        self.molari2.place(x=264, y=10)
        self.molari2.config(text="Molaridade da solução estoque (M):", font=("Times New Roman", 12), fg="black", bg="#B888CF")

        self.concen2 = tk.Label(self)
        self.concen2.place(x=264, y=55)
        self.concen2.config(text="Concentração desejada (μM):", font=("Times New Roman", 12), fg="black", bg="#B888CF")

        self.res = tk.Label(self)
        self.res.place(x=264, y=110)
        self.res.config(text="""OBS: Volume retirado da
 solução estoque: 1 μL""", font=("Times New Roman", 12), fg="black", bg="#B888CF")

        #label que aparece somente quando o botao avançar é clicado pela ultima vez
        self.resultado = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#B888CF")
        self.resultado.place(x=264, y=170)
        self.resultado2 = tk.Label(self, text="", font=("Times New Roman", 12), fg="black", bg="#B888CF")
        self.resultado2.place(x=264, y=220)

        # inicia a janela com a primeira entrada seleciona e detecta qual entry ta selecionada
        self.entrada_ativa = 0
        self.entries2[self.entrada_ativa].focus_set()

#função que permite abrir o menu de conversões
    def abrir_conversoes(self):
            self.master.abrir_conversoes()
    def abrir_conversoes2(self):
        conversoes_window = Conversoes_volume(self)
        conversoes_window.grab_set()
            
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

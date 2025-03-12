#Importando a interface grafica
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#Importando o backend
from backend_calculadora import *

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avançada")
        self.root.geometry("300x500")
        self.root.resizable(False, False)
        
        # Variáveis
        self.valor_a = tk.StringVar()
        self.valor_b = tk.StringVar()
        self.valor_c = tk.StringVar(value="Resultado: ")
        
        # Criar interface
        self.criar_interface()


    def obter_valores(self):
        try:
            a = float(self.valor_a.get()) #Obtendo o valor A por passagem de parametro
            b = float(self.valor_b.get()) #Obtendo o valor B por passagem de parametro
            return a, b
        except ValueError:
            messagebox.showerror("Erro", "Por favor, informe valores numéricos válidos.")
            return None, None
                    
    def atualizar_resultado(self, operacao, nome_operacao):
        a, b = self.obter_valores()
        if a is not None and b is not None:
            try:
                resultado = operacao(a, b)
                resultado_formatado = f"{nome_operacao}: {resultado:.2f}"
                self.valor_c.set(resultado_formatado)
                # Display result in a popup
                messagebox.showinfo("Resultado da Operação", resultado_formatado)
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")  

    def criar_interface(self):
        # Estilo
        style = ttk.Style()
        style.configure("TButton", padding=10, font=("Arial", 10))
        style.configure("TLabel", font=("Arial", 11))
        style.configure("Resultado.TLabel", font=("Arial", 14, "bold"))
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="Calculadora Avançada", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 20))
        
        # Entradas de valores
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=10)
        
        ttk.Label(input_frame, text="Valor A:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.valor_a, width=15).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Valor B:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.valor_b, width=15).grid(row=1, column=1, padx=5, pady=5)
        
        # Frame para botões das operações
        op_frame = ttk.LabelFrame(main_frame, text="Operações", padding=10)
        op_frame.pack(fill="x", pady=15)
        
        # Primeira linha de botões
        btn_frame1 = ttk.Frame(op_frame)
        btn_frame1.pack(fill="x", pady=5)
        
        # Criando os botões com columnspan=1 para garantir espaçamento adequado
        ttk.Button(btn_frame1, text="Soma", 
                   command=lambda: self.atualizar_resultado(soma, "Soma")).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(btn_frame1, text="Subtração", 
                   command=lambda: self.atualizar_resultado(subtracao, "Subtração")).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Segunda linha de botões
        btn_frame2 = ttk.Frame(op_frame)
        btn_frame2.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame2, text="Multiplicação", 
                   command=lambda: self.atualizar_resultado(multiplicacao, "Multiplicação")).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(btn_frame2, text="Divisão", 
                   command=lambda: self.atualizar_resultado(divisao, "Divisão")).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Terceira linha de botões
        btn_frame3 = ttk.Frame(op_frame)
        btn_frame3.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame3, text="Potência", 
                   command=lambda: self.atualizar_resultado(potencia, "Potência")).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(btn_frame3, text="Raiz", 
                   command=lambda: self.atualizar_resultado(raiz, "Raiz")).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Resultado (criado uma única vez)
        resultado_frame = ttk.Frame(main_frame, padding=10)
        resultado_frame.pack(fill="x", pady=15)
        
        ttk.Label(resultado_frame, textvariable=self.valor_c, style="Resultado.TLabel").pack()
        
        # Limpar botão
        ttk.Button(main_frame, text="Limpar", command=self.limpar).pack(pady=10)


    def limpar(self):
        self.valor_a.set("")
        self.valor_b.set("")
        self.valor_c.set("Resultado: ")

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()

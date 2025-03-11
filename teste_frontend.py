#Importando a interface grafica
import tkinter as tk
from tkinter import ttk
#Importando o backend
import backend_calculadora

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avançada")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variáveis
        self.valor_a = tk.StringVar()
        self.valor_b = tk.StringVar()
        self.valor_c = tk.StringVar(value="Resultado: ")
        
        # Criar interface
        self.criar_widgets()

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
        
        ttk.Button(btn_frame1, text="1. Soma", command=lambda: self.calcular(1)).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame1, text="2. Subtração", command=lambda: self.calcular(2)).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame1, text="3. Multiplicação", command=lambda: self.calcular(3)).grid(row=0, column=2, padx=5, pady=5)
        
        # Segunda linha de botões
        btn_frame2 = ttk.Frame(op_frame)
        btn_frame2.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame2, text="4. Divisão", command=lambda: self.calcular(4)).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame2, text="5. Potência", command=lambda: self.calcular(5)).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame2, text="6. Raiz", command=lambda: self.calcular(6)).grid(row=0, column=2, padx=5, pady=5)
        
        # Resultado
        resultado_frame = ttk.Frame(main_frame, padding=10)
        resultado_frame.pack(fill="x", pady=15)
        
        ttk.Label(resultado_frame, textvariable=self.valor_c, style="Resultado.TLabel").pack()
        
        # Limpar botão
        ttk.Button(main_frame, text="Limpar", command=self.limpar).pack(pady=10)

    def obter_valores(self):
        try:
            a = float(self.valor_a.get()) #Obtendo o valor A por passagem de parametro
            b = float(self.valor_b.get()) #Obtendo o valor B por passagem de parametro
            return a, b
        except ValueError:
            messagebox.showerror("Erro", "Por favor, informe valores numéricos válidos.")
            return None, None
        
    def calcular(self, menu):
        a, b = self.obter_valores()
        try:
            c = None
            # Implementação do mesmo código switch/match que você forneceu
            match menu:
                # Soma
                case 1:
                    c = a + b
                    operacao = "Soma"
                # Subtração
                case 2:
                    c = a - b
                    operacao = "Subtração"
                # Multiplicação
                case 3:
                    c = a * b
                    operacao = "Multiplicação"
                # Divisão
                case 4:
                    if b == 0:
                        messagebox.showerror("Erro", "Não é possível dividir por zero.")
                        return
                    c = a / b
                    operacao = "Divisão"
                # Potência
                case 5:
                    c = a ** b
                    operacao = "Potência"
                # Raiz
                case 6:
                    c = a ** (1/b)
                    operacao = "Raiz"
                    
            except Exception:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
                    
    def limpar(self):
        self.valor_a.set("")
        self.valor_b.set("")
        self.valor_c.set("Resultado: ")

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
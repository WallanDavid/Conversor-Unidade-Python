import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
from PIL import Image, ImageTk

historico_conversoes = []

def converter_temperatura():
    try:
        temperatura_celsius = float(entry_celsius.get())
        temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
        resultado = f"Resultado: {temperatura_fahrenheit:.2f} °F"
        label_resultado.config(text=resultado)
        historico_conversoes.append(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico para Celsius.")

def converter_comprimento():
    try:
        comprimento_metros = float(entry_comprimento.get())
        comprimento_quilometros = metros_para_quilometros(comprimento_metros)
        resultado = f"Resultado: {comprimento_quilometros:.4f} km"
        label_resultado.config(text=resultado)
        historico_conversoes.append(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico para metros.")

def converter_peso():
    try:
        peso_quilogramas = float(entry_peso.get())
        peso_gramas = quilogramas_para_gramas(peso_quilogramas)
        resultado = f"Resultado: {peso_gramas:.2f} g"
        label_resultado.config(text=resultado)
        historico_conversoes.append(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico para quilogramas.")

def exibir_historico():
    historico_str = "\n".join(historico_conversoes)
    messagebox.showinfo("Histórico", f"Histórico:\n{historico_str}")

def salvar_historico():
    try:
        with open("historico_conversoes.json", "w") as file:
            json.dump(historico_conversoes, file)
        messagebox.showinfo("Salvo", "Histórico salvo com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o histórico: {e}")

def carregar_historico():
    global historico_conversoes
    try:
        if os.path.exists("historico_conversoes.json"):
            with open("historico_conversoes.json", "r") as file:
                historico_conversoes = json.load(file)
            messagebox.showinfo("Carregado", "Histórico carregado com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo de histórico encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar o histórico: {e}")

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def metros_para_quilometros(metros):
    return metros / 1000

def quilogramas_para_gramas(quilogramas):
    return quilogramas * 1000

def limpar_campos():
    entry_celsius.delete(0, tk.END)
    entry_comprimento.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="Resultado:")

# Configuração da interface
app = tk.Tk()
app.title("Conversor de Unidades")
app.geometry("500x300")

# Estilo ttk para uma aparência mais moderna
style = ttk.Style()
style.theme_use("clam")

# Criar guias usando o estilo ttk
notebook = ttk.Notebook(app)

# Aba de temperatura
tab_temperatura = ttk.Frame(notebook)
notebook.add(tab_temperatura, text="Temperatura")

label_celsius = ttk.Label(tab_temperatura, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=10)

entry_celsius = ttk.Entry(tab_temperatura)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

btn_converter_temperatura = ttk.Button(tab_temperatura, text="Converter", command=converter_temperatura)
btn_converter_temperatura.grid(row=1, column=0, columnspan=2, pady=10)

# Aba de comprimento
tab_comprimento = ttk.Frame(notebook)
notebook.add(tab_comprimento, text="Comprimento")

label_comprimento = ttk.Label(tab_comprimento, text="Comprimento (metros):")
label_comprimento.grid(row=0, column=0, padx=10, pady=10)

entry_comprimento = ttk.Entry(tab_comprimento)
entry_comprimento.grid(row=0, column=1, padx=10, pady=10)

btn_converter_comprimento = ttk.Button(tab_comprimento, text="Converter", command=converter_comprimento)
btn_converter_comprimento.grid(row=1, column=0, columnspan=2, pady=10)

# Aba de peso
tab_peso = ttk.Frame(notebook)
notebook.add(tab_peso, text="Peso")

label_peso = ttk.Label(tab_peso, text="Peso (quilogramas):")
label_peso.grid(row=0, column=0, padx=10, pady=10)

entry_peso = ttk.Entry(tab_peso)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

btn_converter_peso = ttk.Button(tab_peso, text="Converter", command=converter_peso)
btn_converter_peso.grid(row=1, column=0, columnspan=2, pady=10)

# Adiciona a aba de histórico
notebook.add(tk.Frame(notebook), text="Histórico")

# Organiza os componentes da interface
notebook.grid(row=0, column=0, padx=10, pady=10)

# Botão para exibir histórico
btn_exibir_historico = ttk.Button(app, text="Exibir Histórico", command=exibir_historico)
btn_exibir_historico.grid(row=1, column=0, pady=10)

# Botão para salvar histórico
btn_salvar_historico = ttk.Button(app, text="Salvar Histórico", command=salvar_historico)
btn_salvar_historico.grid(row=2, column=0, pady=10)

# Botão para carregar histórico
btn_carregar_historico = ttk.Button(app, text="Carregar Histórico", command=carregar_historico)
btn_carregar_historico.grid(row=3, column=0, pady=10)

# Botão para limpar os campos
btn_limpar_campos = ttk.Button(app, text="Limpar Campos", command=limpar_campos)
btn_limpar_campos.grid(row=4, column=0, pady=10)

# Resultado
label_resultado = ttk.Label(app, text="Resultado:")
label_resultado.grid(row=5, column=0, pady=10)

# Barra de status
status_bar = ttk.Label(app, text="Bem-vindo ao Conversor de Unidades!", anchor=tk.W)
status_bar.grid(row=6, column=0, pady=10, sticky=(tk.W, tk.E))

# Iniciar a interface
app.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk


# tela de mensagem

def show_message():
    messagebox.showinfo("Título da Mensagem", "Esta é uma mensagem de exemplo.")

# tela de entrada de texto
def show_entry():
    entry_window = tk.Toplevel(root)
    entry_window.title("Entrada de Texto")

    label = tk.Label(entry_window, text="Digite algo:")
    label.pack(pady=10)

    entry = tk.Entry(entry_window)
    entry.pack(pady=10)

    def submit():
        user_input = entry.get()
        messagebox.showinfo("Entrada", f"Você digitou: {user_input}")
        entry_window.destroy()

    submit_button = tk.Button(entry_window, text="Enviar", command=submit)
    submit_button.pack(pady=10)

def show_cadastro():
    cadastro_window = tk.Toplevel(root)
    cadastro_window.title("Tela de Cadastro")

    # Labels e Entrys
    tk.Label(cadastro_window, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_nome = tk.Entry(cadastro_window)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(cadastro_window, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_email = tk.Entry(cadastro_window)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(cadastro_window, text="Login:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_login = tk.Entry(cadastro_window)
    entry_login.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(cadastro_window, text="Senha:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_senha = tk.Entry(cadastro_window, show="*")
    entry_senha.grid(row=3, column=1, padx=10, pady=5)

    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        login = entry_login.get()
        senha = entry_senha.get()
        if not nome or not email or not login or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        messagebox.showinfo("Cadastro", f"Cadastro realizado!\nNome: {nome}\nEmail: {email}\nLogin: {login}")
        # Adiciona os dados na tabela principal
        tree.insert("", "end", values=(nome, email, login, senha))

    def limpar():
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_login.delete(0, tk.END)
        entry_senha.delete(0, tk.END)

    def sair():
        cadastro_window.destroy()

    # Botões
    tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(cadastro_window, text="Limpar", command=limpar).grid(row=4, column=1, padx=10, pady=10, sticky="w")
    tk.Button(cadastro_window, text="Sair", command=sair).grid(row=4, column=1, padx=10, pady=10, sticky="e")

# Janela principal
root = tk.Tk()
root.title("Cadastro JAVA em py")
root.geometry("500x400")
root.resizable(True, True)

# Botões principais
btn_msg = tk.Button(root, text="Mostrar Mensagem", command=show_message)
btn_msg.pack(pady=5)

btn_entry = tk.Button(root, text="Entrada de Texto", command=show_entry)
btn_entry.pack(pady=5)

btn_cadastro = tk.Button(root, text="Tela de Cadastro", command=show_cadastro)
btn_cadastro.pack(pady=5)

# Tabela para mostrar os dados cadastrados
tree = ttk.Treeview(root, columns=("Nome", "Email", "Login", "Senha"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Email", text="Email")
tree.heading("Login", text="Login")
tree.heading("Senha", text="Senha")
tree.pack(pady=10, fill="x", expand=True)

root.mainloop()


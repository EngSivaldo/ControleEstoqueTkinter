from tkinter import *
from tkinter import messagebox
import pyodbc

# Integracao com bd
dados_conexao = ("Driver={SQL Server};"
                 "Server=PCESTUDO;"
                 "Database=EstoqueMentoria")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Procurar insumo
def btn_clicked0():
    nome_insumo = entry1.get()
    if not nome_insumo:
        messagebox.showerror("Erro", "O campo nome do insumo está vazio.")
        return
    try:
        # Consulta SQL para buscar o insumo pelo nome
        comando = "SELECT * from Insumos WHERE nome_insumo = ?;"
        cursor.execute(comando, (nome_insumo,))
        entry0.delete('1.0', END)
        for linha in cursor.fetchall():
            # Formata e exibe os dados do insumo encontrado
            texto = f"Item: {linha.nome_insumo}\n Quantidade: {linha.qtde}\n Lote:{linha.lote}\n Validade:{linha.data_validade}\n"
            entry0.insert("1.0", texto)
    except pyodbc.Error as e:
        messagebox.showerror("Erro", f"Erro ao buscar dados: {e}")

# Deletar insumo
def btn_clicked1():
    nome_insumo = entry1.get()
    if not nome_insumo:
        messagebox.showerror("Erro", "O campo nome do insumo está vazio.")
        return
    try:
        # Verifica se o insumo existe e tem quantidade maior que zero
        comando = "SELECT qtde from Insumos WHERE nome_insumo = ?;"
        cursor.execute(comando, (nome_insumo,))
        resultado = cursor.fetchone()
        if resultado and resultado.qtde > 0:
            # Deleta o insumo do banco de dados
            comando = "DELETE from Insumos WHERE nome_insumo = ?;"
            cursor.execute(comando, (nome_insumo,))
            conexao.commit()
            messagebox.showinfo("Aviso", f"{nome_insumo} foi excluido do banco de dados!")
        else:
            messagebox.showerror("Erro", "Não é possível excluir um insumo com quantidade zero ou inexistente.")
    except pyodbc.Error as e:
        messagebox.showerror("Erro", f"Erro ao deletar dados: {e}")

# Consumir insumo (registrar uso insumo)
def btn_clicked2():
    nome_insumo = entry1.get()
    qtde_usada = entry4.get()
    if not nome_insumo or not qtde_usada:
        messagebox.showerror("Erro", "Os campos nome do insumo e quantidade usada devem ser preenchidos.")
        return
    try:
        qtde_usada = int(qtde_usada)
        # Verifica se há quantidade suficiente do insumo no estoque
        comando = "SELECT qtde from Insumos WHERE nome_insumo = ?;"
        cursor.execute(comando, (nome_insumo,))
        resultado = cursor.fetchone()
        if resultado and resultado.qtde >= qtde_usada:
            # Atualiza a quantidade do insumo no banco de dados
            comando = "UPDATE Insumos SET qtde = qtde - ? WHERE nome_insumo = ?;"
            cursor.execute(comando, (qtde_usada, nome_insumo))
            conexao.commit()
            messagebox.showinfo("Aviso", f"{qtde_usada} unidades do {nome_insumo} foram usadas")
        else:
            messagebox.showerror("Erro", "Quantidade insuficiente no estoque.")
    except ValueError:
        messagebox.showerror("Erro", "A quantidade usada deve ser um número inteiro.")
    except pyodbc.Error as e:
        messagebox.showerror("Erro", f"Erro ao atualizar dados: {e}")

# Adicionar insumo
def btn_clicked3():
    nome_insumo = entry1.get()
    data_validade = entry2.get()
    lote = entry3.get()
    qtde = entry4.get()
    if not nome_insumo or not data_validade or not lote ou not qtde:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    try:
        qtde = int(qtde)
        # Verifica se o insumo já existe no banco de dados
        comando = "SELECT * from Insumos WHERE nome_insumo = ?;"
        cursor.execute(comando, (nome_insumo,))
        resultado = cursor.fetchone()
        if resultado:
            messagebox.showerror("Erro", "O insumo já existe no banco de dados.")
        else:
            # Insere o novo insumo no banco de dados
            comando = "INSERT INTO Insumos(nome_insumo, data_validade, lote, qtde) VALUES (?, ?, ?, ?)"
            cursor.execute(comando, (nome_insumo, data_validade, lote, qtde))
            conexao.commit()
            messagebox.showinfo("Aviso", "Produto adicionado com sucesso")
    except ValueError:
        messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
    except pyodbc.Error as e:
        messagebox.showerror("Erro", f"Erro ao adicionar dados: {e}")

# Fechar a conexão ao sair
def on_closing():
    cursor.close()
    conexao.close()
    window.destroy()

window = Tk()
window.geometry("711x646")
window.configure(bg="#ffffff")
canvas = Canvas(window, bg="#ffffff", height=646, width=711, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"janela/background.png")
background = canvas.create_image(355.5, 323.0, image=background_img)

img0 = PhotoImage(file=f"janela/img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked0, relief="flat")
b0.place(x=479, y=195, width=178, height=38)

img1 = PhotoImage(file=f"janela/img1.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=btn_clicked1, relief="flat")
b1.place(x=247, y=197, width=178, height=36)

img2 = PhotoImage(file=f"janela/img2.png")
b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=btn_clicked2, relief="flat")
b2.place(x=479, y=123, width=178, height=35)

img3 = PhotoImage(file=f"janela/img3.png")
b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=btn_clicked3, relief="flat")
b3.place(x=247, y=125, width=178, height=34)

entry0_img = PhotoImage(file=f"janela/img_textBox0.png")
entry0_bg = canvas.create_image(455.0, 560.0, image=entry0_img)

entry0 = Text(bd=0, bg="#ffffff", highlightthickness=0)
entry0.place(x=250, y=502, width=410, height=114)

entry1_img = PhotoImage(file=f"janela/img_textBox1.png")
entry1_bg = canvas.create_image(517.0, 294.5, image=entry1_img)

entry1 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
entry1.place(x=377, y=278, width=280, height=31)

entry2_img = PhotoImage(file=f"janela/img_textBox2.png")
entry2_bg = canvas.create_image(517.0, 340.5, image=entry2_img)

entry2 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
entry2.place(x=377, y=324, width=280, height=31)

entry3_img = PhotoImage(file=f"janela/img_textBox3.png")
entry3_bg = canvas.create_image(517.0, 388.5, image=entry3_img)

entry3 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
entry3.place(x=377, y=372, width=280, height=31)

entry4_img = PhotoImage(file=f"janela/img_textBox4.png")
entry4_bg = canvas.create_image(517.0, 436.5, image=entry4_img)

entry4 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
entry4.place(x=377, y=420, width=280, height=31)

# Configura o fechamento da janela para garantir que a conexão com o banco de dados seja fechada corretamente
window.protocol("WM_DELETE_WINDOW", on_closing)
window.resizable(False, False)
window.mainloop()
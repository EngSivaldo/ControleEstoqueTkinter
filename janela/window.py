from tkinter import *
from tkinter import messagebox
import pyodbc

#integracao com bd
dados_conexao = ("Driver={SQL Server};"
                 "Server=PCESTUDO;"
                 "Database=EstoqueMentoria")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()



def btn_clicked0():
    print("Procurar insumo")
    #pegar a info no campo nome_insumo(entry1)
    nome_insumo = entry1.get()
    #buscar essa info do insumo no bd
    #colocar no entry0(caixa texto) as info do insumo do bd

def btn_clicked1():
    print("Deletar insumo")
     #pegar a info no campo nome_insumo(entry1)
    nome_insumo = entry1.get()
     #buscar e deletar essa info do insumo no bd
     #exibir msg que deletou o insumo no bd 

#consumir insumo(registrar uso insumo)
def btn_clicked2():
    print("Registrar Uso insumo")
    #pegar a info no campo nome_insumo(entry1)
    nome_insumo = entry1.get()
    #pegar a info no campo qtde(entry4)
    qtde_usada = entry4.get()
    #buscar o insumo pelo nome dele no bd
    #diminuir a qtde que consumi do bd
    # Atualizar
    comando = comando = f"""UPDATE Insumos
            SET qtde = qtde - {qtde_usada}
            WHERE nome_insumo = '{nome_insumo}';
            """
    cursor.execute(comando)
    cursor.commit()
    messagebox.showinfo(title="Aviso Uso Insumo", message=f"{qtde_usada}unidades do {nome_insumo} foram usados")
    print("Registrar Uso insumos")

 # Adicionar no banco de dados aquele insumo
def btn_clicked3():
    #pegar os campos(Values)
    nome_insumo = entry1.get()
    data_validade = entry2.get()
    lote = entry3.get()
    qtde = entry4.get()

    # Adicionar no banco de dados aquele insumo
    comando = f"""INSERT INTO Insumos(nome_insumo, data_validade, lote, qtde)
        VALUES
            ('{nome_insumo}', '{data_validade}', '{ lote}', '{qtde}')"""
    cursor.execute(comando)
    cursor.commit()
    messagebox.showinfo(title="Aviso Adicionar Produto", message="Produto adicionado com sucesso")
    print("Adicionar insumo")
    # entry1.delete() limpar campos apos adicionar
    # entry2.delete()
    # entry3.delete()
    # entry4.delete()

# def verificar_insercao():
#     try:
#         cursor.execute("SELECT * FROM Insumos")
#         resultados = cursor.fetchall()
#         for linha in resultados:
#             print(linha)
#     except pyodbc.Error as e:
#         print(f"Erro ao buscar dados: {e}")

# # Chamar a função para verificar a inserção
# verificar_insercao()
  
# print(entry1.get()) -> nome_insumo
# print(entry2.get()) -> data_validade
# print(entry3.get()) -> lote
# print(entry4.get()) -> quantidade
#entry0.get("1.0", end) -> campo para exibir produto do banco de dados

window = Tk()

window.geometry("711x646")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 646,
    width = 711,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"janela/background.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file = f"janela/img0.png")
#procurar insumo
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 479, y = 195,
    width = 178,
    height = 38)

img1 = PhotoImage(file = f"janela/img1.png")
#deletar insumo
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 247, y = 197,
    width = 178,
    height = 36)

img2 = PhotoImage(file = f"janela/img2.png")
#registrar Uso insumo
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 479, y = 123,
    width = 178,
    height = 35)

img3 = PhotoImage(file = f"janela/img3.png")

#adicionar insumo
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b3.place(
    x = 247, y = 125,
    width = 178,
    height = 34)

entry0_img = PhotoImage(file = f"janela/img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 250, y = 502,
    width = 410,
    height = 114)

entry1_img = PhotoImage(file = f"janela/img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 377, y = 278,
    width = 280,
    height = 31)

entry2_img = PhotoImage(file = f"janela/img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 377, y = 324,
    width = 280,
    height = 31)

entry3_img = PhotoImage(file = f"janela/img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 377, y = 372,
    width = 280,
    height = 31)

entry4_img = PhotoImage(file = f"janela/img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 377, y = 420,
    width = 280,
    height = 31)

window.resizable(False, False)
window.mainloop()

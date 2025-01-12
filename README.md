Sistema de Controle de Estoque

resumo das ferramentas usadas no seu aplicativo:

Tkinter: Biblioteca padrão do Python para criar interfaces gráficas (GUIs). Você usou vários componentes do Tkinter, como:

Tk(): Cria a janela principal.
Canvas: Área de desenho para adicionar widgets e gráficos.
Button: Botões interativos.
Entry: Campos de entrada de texto.
Text: Campo de texto para exibir múltiplas linhas.
PhotoImage: Para carregar e exibir imagens.
messagebox: Para exibir mensagens de erro e informações.
pyodbc: Biblioteca para conectar e interagir com bancos de dados SQL Server. Você usou:

pyodbc.connect(): Para estabelecer a conexão com o banco de dados.
cursor(): Para criar um cursor que permite executar comandos SQL.
execute(): Para executar comandos SQL.
fetchone() e fetchall(): Para recuperar resultados de consultas SQL.
commit(): Para salvar alterações no banco de dados.
Funções Personalizadas: Você criou várias funções para manipular os dados do banco de dados e atualizar a interface gráfica:

btn_clicked0(): Para procurar um insumo no banco de dados e exibir os resultados.
btn_clicked1(): Para deletar um insumo do banco de dados.
btn_clicked2(): Para registrar o uso de um insumo (diminuir a quantidade).
btn_clicked3(): Para adicionar um novo insumo ao banco de dados.
Essas ferramentas juntas permitem que seu aplicativo gerencie um estoque de insumos de forma eficiente, com uma interface gráfica amigável e integração com um banco de dados SQL Server











Essas funcionalidades permitem que o aplicativo gerencie o estoque de insumos de forma eficiente, garantindo que as informações estejam sempre atualizadas e acessíveis
Procurar Insumo:

Permite ao usuário buscar informações sobre um insumo específico no banco de dados.
Exibe detalhes como nome, quantidade, lote e data de validade do insumo.
Deletar Insumo:

Permite ao usuário excluir um insumo do banco de dados.
Verifica se o insumo possui quantidade maior que zero antes de permitir a exclusão.
Consumir Insumo:

Permite ao usuário registrar o uso de uma quantidade específica de um insumo.
Atualiza a quantidade do insumo no banco de dados após verificar se há quantidade suficiente disponível.
Adicionar Insumo:

Permite ao usuário adicionar um novo insumo ao banco de dados.
Verifica se todos os campos necessários estão preenchidos e se o insumo já não existe no banco de dados antes de adicionar.
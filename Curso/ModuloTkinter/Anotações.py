'''
TkInter = TK Interface
TkInter é uma biblioteca gráfica nativa do Python
A bibliotexa é um binding, ou seja, a biblioteca vem com o Python, mas não faz parte do desenvolvimento Python
GUI = Graphic User Interface
widget = todo componente que compõe uma interface gráfica, como botões, botões de opção, campos de texto, janelas e rótulos de texto.
container = um widget que pode conter outros widgets. Todo container também está contido em outro container, salvo a janela principal
window = um termo que possui significados diferentes em contextos diferentes. Em geral, se refere a uma área retangular em algum lugar na tela de exibição.
top-level window = uma janela independente e que normalmente está sendo exibida sob as demais
frame = a unidade básica de organização de layouts complexos.
child-parent = o nome da relação entre um widget e seu container. Um campo adicionado a uma janela é uma relação parent-child, onde a janela é o parent e o campo o child.


janela = Tk() = Inicialização do pacote sempre será feita pelo comando Tk(). Exemplo:

janela.mainloop() = Para fazer o comando funcionar, sempre haverá o comando mainloop().


.title() = Para atribuir um titulo a uma janela usa-se o comando
janela['bg'] = 'green' = Para atribuir uma cor de background para uma janela, usa-se a propriedade "bg".
.geometry(300x300+100+100) = Para atribuir a posição de algo usa-se o comando . Tendo como lógica LarguraxAltura+Esquerda+Topo.
Caso apenas seja necessário definir o tamanho em largura e altura, basta usar LarguraxAltura.
Caso apenas seja necessário definir a distância da janela da esquerda e do topo da tela, basta usar +Esquerda+Topo

.grid(row=0, column=0) = Para posicionar algo na tela, uma das maneiras de se fazer isso é através da função .grid, onde são apontadas as linhas e colunas do grid para posicionar os widgets do programa.
.grid_forget() = Sempre que for necessário tirar algo da tela, usa-se esta função

Button() = Função para criar um botão
Button(state=disabled) = state serve para determinar o estado do botão, nesse caso desabilitado
Button(padx=50, pady=50) = Determinar o tamanho do botão
Button(command=exemplo) = Passar a função que o comando ira executar
Button(fg="white", bg="black") = Definir a cor do que estiver dentro do botão como branca, e o background do botão como preto
As opções de grid do Tkinter são: -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, e -sticky


Entry() = Função para uma entrada, ou um campo de texto
Entry(width=50) = Apontar o tamanho do widget
Entry(borderwidth=5) = Determinar o tamanho da borda do campo
exemplo.get() = Capturar o que estiver escrito no campo de texto
exemplo.insert() = Inserir dentro do campo de texto algo assim que o programa for executado

Para fazer um botão interagir com o campo de texto, basta fazer a função que o botão está executando interagir com o campo de texto

button_example = Button(root, text="example", command=lambda: button_click(0))
= Toda vez que um parâmetro for passado através de um botão, o comando deverá começar com Lambda.


relief=SUNKEN = Afundar algo
sticky=W+E = Expandir algo a direita e esquerda
anchor=E = Fazer algo se alocado a direita da base


frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=100, pady=100)
= padx e pady dentro do frame significa que o padding ficara dentro do frame. padx e pady no frame.pack significa que o padding ficara ao redor do frame

Usando frames, pode-se misturar alinhamentos, .pack pode ser usado para o frame em si, e grid para os itens dentro do frame


Para criar popups, ou novas janelas em um programa, se usa o comando messagebox.
from tkinter import messagebox

messagebox.showinfo("Titulo da janela","Mensagem dentro do popup")
= popup para apenas mostrar informações através do popup

messagebox.showwarning("Titulo da janela","Mensagem dentro do popup")
= popup de alerta

messagebox.showerror("Titulo da janela","Mensagem dentro do popup")
= popup de erro

messagebox.askquestion("Titulo da janela","Mensagem dentro do popup")
= popup com opções de sim e não

messagebox.showinfo("Titulo da janela","Mensagem dentro do popup")
= popup com opções de ok ou cancelar

messagebox.askyesno("Titulo da janela","Mensagem dentro do popup")
= popup para perguntar sim ou não

exemplo = messagebox.askyesno("Titulo da janela","Mensagem dentro do popup")
= Para manipular o botão que foi apertado no popup basta atribuir o comando messagebox a uma variável.


janela = Toplevel() = Criar uma nova janela chamada janela


slider = Scale(root).pack = Para criar sliders usa-se a classe Scale
Scale(root, orient=HORIZONTAL) = Para colocar um slider na horizontal usa-se orient=HORIZONTAL


var = StringVar() OU var = IntVar()
= Sempre que se for usar as checkboxes, precisa-se antes de atribuir a uma variável o tipo de retorno da check box.

checkbox = Checkbutton(root, variable=var) = Para criar check boxes usa-se a classe Checkbutton

checkbox = Checkbutton(root, variable= var, onvalue="On", offvalue="Off")
= Para definir o retorno para variável da checkbox, usa-se os parametros onvalue e offvalue


clicked = StringVar()
drop = OptionMenu(root, clicked, *lista)
= Usa-se a classe OptionMenu para determinar algo como dropdown.
= As opções que apareceram no dropdown podem ser definidas em uma lista, basta colocar um * antes da lista para mostrar o dropdown da maneira correta
= Para usar o item selecionado no dropdown basta usar a variável atribuida, neste caso "clicked"


import sqlite3 = Pacote basico nativo Python para mexer com databases

nome = sqlite3.connect("nome_do_banco.db")
= Comando para criar ou conectar a um banco de dados

cursor = nome.cursor()
= Criar um cursor para lidar com o banco de dados. Sempre que um comando for dado em sql, o cursor servirá para realizar os comandos

cursor.execute("COMANDOS SQL")
= Execução de código SQL


example(font=("Helvetica", 20))
= Para mudar a fonte e o tamanho da mesma usa-se este método



'''

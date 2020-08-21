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
.geometr()00x300+100+100) = Para atribuir a posição de algo usa-se o comando . Tendo como lógica LarguraxAltura+Esquerda+Topo.
Caso apenas seja necessário definir o tamanho em largura e altura, basta usar LarguraxAltura.
Caso apenas seja necessário definir a distância da janela da esquerda e do topo da tela, basta usar +Esquerda+Topo

.grid(row=0, column=0) = Para posicionar algo na tela, uma das maneiras de se fazer isso é através da função .grid, onde são apontadas as linhas e colunas do grid para posicionar os widgets do programa.

Button() = Função para criar um botão
Button(state=disabled) = state serve para determinar o estado do botão, nesse caso desabilitado
Button(padx=50, pady=50) = Determinar o tamanho do botão
Button(command=exemplo) = Passar a função que o comando ira executar
Button(fg="white", bg="black") = Definir a cor do que estiver dentro do botão como branca, e o background do botão como preto


Entry() = Função para uma entrada, ou um campo de texto
Entry(width=50) = Apontar o tamanho do widget
Entry(borderwidth=5) = Determinar o tamanho da borda do campo
exemplo.get() = Capturar o que estiver escrito no campo de texto
exemplo.insert() = Inserir dentro do campo de texto algo assim que o programa for executado

Para fazer um botão interagir com o campo de texto, basta fazer a função que o botão está executando interagir com o campo de texto

'''
'''
TkInter == TK Interface
TkInter é uma biblioteca gráfica nativa do Python
A bibliotexa é um binding, ou seja, a biblioteca vem com o Python, mas não faz parte do desenvolvimento Python
GUI = Graphic User Interface
widget é todo componente que compõe uma interface gráfica, como botões, botões de opção, campos de texto, janelas e rótulos de texto.
container é um widget que pode conter outros widgets. Todo container também está contido em outro container, salvo a janela principal
window é um termo que possui significados diferentes em contextos diferentes. Em geral, se refere a uma área retangular em algum lugar na tela de exibição.
top-level window é uma janela independente e que normalmente está sendo exibida sob as demais
frame é a unidade básica de organização de layouts complexos.
child-parent é o nome da relação entre um widget e seu container. Um campo adicionado a uma janela é uma relação parent-child, onde a janela é o parent e o campo o child.


Inicialização do pacote sempre será feita pelo comando Tk(). Exemplo:
janela = Tk()

Para fazer o comando funcionar, sempre haverá o comando mainloop(). Exemplo
janela.mainloop()


Para atribuir um titulo a uma janela usa-se o comando .title()
Para atribuir uma cor de background para uma janela, usa-se a propriedade "bg". Exemplo: janela['bg'] = 'green'
Para atribuir a posição de algo usa-se o comando .geometr(). Tendo como lógica LarguraxAltura+Esquerda+Topo. Exemplo: 300x300+100+100
Caso apenas seja necessário definir o tamanho em largura e altura, basta usar LarguraxAltura.
Caso apenas seja necessário definir a distância da janela da esquerda e do topo da tela, basta usar +Esquerda+Topo


'''
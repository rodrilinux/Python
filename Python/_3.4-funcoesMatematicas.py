# coding: iso-8859-1_*_

''' Em matemática, você provavelmente já viu funções como seno (sen, sin em inglês) e logaritmo (log), e aprendeu
a resolver expressões como sen(pi/2) e log(1/x). Primeiro você resolve e expressão entre parênteses (o
argumento). Por exemplo, pi/2 é aproximadamente 1,571, e 1/x é 0.1 (se x for 10,0).
Aí você avalia a função propriamente dita, seja procurando numa tabela ou realizando vários cálculos. O sen de 1,571
é 1 e o log de 0,1 é -1 (assumindo que log indica o logaritmo na base 10).
Este processo pode ser aplicado repetidamente para avaliar expressões mais complicadas, como
log(1/sen(pi/2)). Primeiro você avalia o argumento na função mais interna, depois avalia a função e
assim por diante.
Python tem um módulo matemático que provê a maioria das funções matemáticas mais familiares. Um módulo é um
arquivo que contém uma coleção de funções relacionadas agrupadas juntas.
Antes de podermos usar as funções contidas em um módulo, temos de importá-lo: '''


import math

'''Para chamar uma das funções, temos que especificar o nome do módulo e o nome da função, separados por um ponto.
Esse formato é chamado de notação de ponto: '''

decibel = math.log10(17.0)
angulo = 1.5
altura = math.sin(angulo)

print(decibel)
print(angulo)
print(altura)

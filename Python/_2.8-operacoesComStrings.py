# coding: iso-8859-1_*_
from _ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER

# Interessante � o operador +, que funciona com strings, embora ele n�o fa�a exatamente o que voc� poderia esperar.
# Para strings, o operador + representa concatena��o, que significa juntar os dois operandos ligando-os pelos extremos.
# Por exemplo:

fruta = 'banana'
assada = ' com canela � muito bom!!!'
print(fruta + assada)

repetcao = 'Legal '
resultado = repetcao * 3
print(resultado)
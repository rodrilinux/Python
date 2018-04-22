# coding: iso-8859-1_*_
from _ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER

# Interessante é o operador +, que funciona com strings, embora ele não faça exatamente o que você poderia esperar.
# Para strings, o operador + representa concatenação, que significa juntar os dois operandos ligando-os pelos extremos.
# Por exemplo:

fruta = 'banana'
assada = ' com canela é muito bom!!!'
print(fruta + assada)

repetcao = 'Legal '
resultado = repetcao * 3
print(resultado)
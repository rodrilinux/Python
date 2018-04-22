# coding: iso-8859-1_*_
from builtins import str

# Python provê uma coleção de funções nativas que convertem valores de um tipo em outro. A função int recebe um
# valor e o converte para inteiro, se possível, ou, se não, reclama:

# Estou usando o type para mostrar o tio da variável:

linha = ('\n')
duasLinhas = (linha * 2)

a = type('23')
print(a)

a = type (int('23'))
print(a)
print ('####################################################################')

print(duasLinhas)
########################

# Convertendo tudo para inteiros:

int ('32')
print (int)
a = ('32')
print(int (a))
print(linha)
######################

int (3.1876)
print(int)
a = (3.1876)
print(int(a))
print(linha)
######################

int (-2.3)
print(int)
a = (-2.3)
print(int(a))
print(duasLinhas)

# Convertendo tudo para ponto flutuante:

float ('32')
print(float)
a = ('32')
print (float (a))
print(linha)
###########################

float (42)
print(float)
a = (42)
print(float(a))
print(duasLinhas)

# Convertendo tudo para String:

str (32)
print(str)
a = 32
print(str (a))





























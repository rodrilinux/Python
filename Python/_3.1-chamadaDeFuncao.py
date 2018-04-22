# coding: iso-8859-1_*_

# Voc� j� viu um exemplo de uma chamada de fun��o:

# >>> type(�32�)
# <class �str�>

# O nome da fun��o � type e ela exibe o tipo de um valor ou vari�vel. O valor ou vari�vel, que � chamado de
# argumento da fun��o, tem que vir entre par�nteses. � comum se dizer que uma fun��o �recebe� um valor ou mais
# valores e �retorna� um resultado. O resultado � chamado de valor de retorno.
# Em vez de imprimir um valor de retorno, podemos atribui-lo a uma vari�vel:

s = type('32')
print('O valor de s � do tipo:' , s)

n = type(10)
print('O valor de n � do tipo:' ,n)

f = type(3.14159)
print('O valor de f � do tipo:' ,f)

# Como outro exemplo, a fun��o id recebe um valor ou uma vari�vel e retorna um inteiro, que atua como um identificador
# �nico para aquele valor:

identificador = id (3)
print('O id de 3 �:' , identificador)

eu = identificador
print(eu)





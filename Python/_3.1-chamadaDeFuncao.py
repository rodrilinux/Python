# coding: iso-8859-1_*_

# Você já viu um exemplo de uma chamada de função:

# >>> type(’32’)
# <class ’str’>

# O nome da função é type e ela exibe o tipo de um valor ou variável. O valor ou variável, que é chamado de
# argumento da função, tem que vir entre parênteses. É comum se dizer que uma função ‘recebe’ um valor ou mais
# valores e ‘retorna’ um resultado. O resultado é chamado de valor de retorno.
# Em vez de imprimir um valor de retorno, podemos atribui-lo a uma variável:

s = type('32')
print('O valor de s é do tipo:' , s)

n = type(10)
print('O valor de n é do tipo:' ,n)

f = type(3.14159)
print('O valor de f é do tipo:' ,f)

# Como outro exemplo, a função id recebe um valor ou uma variável e retorna um inteiro, que atua como um identificador
# único para aquele valor:

identificador = id (3)
print('O id de 3 é:' , identificador)

eu = identificador
print(eu)





# coding: iso-8859-1_*_


''' Agora que podemos converter entre tipos, temos outra maneira de lidar com a divisão inteira. Voltando ao exemplo do
capítulo anterior, suponha que queiramos calcular a fração de hora que já passou. A expressão mais óbvia, minuto
 / 60, faz aritmética inteira, assim, o resultado é sempre 0, mesmo aos 59 minutos passados da hora. '''


# Uma solução é converter minuto para ponto flutuante e fazer a divisão em ponto flutuante:

minuto = 59
conversao = (float (minuto)) / 60
print (conversao) 

# Opcionalmente, podemos tirar vantagem das regras de conversão automática entre tipos, chamada de coerção de
# tipos. Para os operadores matemáticos, se qualquer operando for um float, o outro é automaticamente convertido
# para float:

minuto = 59
conversao = minuto / 60.0
print(conversao)

# Fazendo o denominador um float, forçamos o Python a fazer a divisão em ponto flutuante.
# coding: iso-8859-1_*_


''' Agora que podemos converter entre tipos, temos outra maneira de lidar com a divis�o inteira. Voltando ao exemplo do
cap�tulo anterior, suponha que queiramos calcular a fra��o de hora que j� passou. A express�o mais �bvia, minuto
 / 60, faz aritm�tica inteira, assim, o resultado � sempre 0, mesmo aos 59 minutos passados da hora. '''


# Uma solu��o � converter minuto para ponto flutuante e fazer a divis�o em ponto flutuante:

minuto = 59
conversao = (float (minuto)) / 60
print (conversao) 

# Opcionalmente, podemos tirar vantagem das regras de convers�o autom�tica entre tipos, chamada de coer��o de
# tipos. Para os operadores matem�ticos, se qualquer operando for um float, o outro � automaticamente convertido
# para float:

minuto = 59
conversao = minuto / 60.0
print(conversao)

# Fazendo o denominador um float, for�amos o Python a fazer a divis�o em ponto flutuante.
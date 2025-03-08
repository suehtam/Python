def soma(sequencia):
    resultado = 0
    for valor in sequencia:
        resultado += valor
    return resultado

#O que faz: Calcula a soma dos elementos de uma sequência numérica.
# resultado = 0 Inicializa a variável que armazenará a soma total.

#for valor in sequencia: Percorre cada elemento da sequência fornecida.

#resultado += valor Adiciona o valor atual ao total acumulado.

#return resultado Retorna a soma total após percorrer toda a sequência.

#Dica extra: Você poderia simplificar essa função usando a função embutida sum() do Python:
#Mas escrever a versão com o loop é ótimo para entender como a soma é acumulada passo a passo.
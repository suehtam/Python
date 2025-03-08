def fatorial_otimizado(n, acumulador=1):
    if n == 0:
        return acumulador
    else:
        return fatorial_otimizado(n-1, n * acumulador)
    
#O que faz: Calcula o fatorial de um número usando otimização de chamada de cauda (tail recursion), acumulando o resultado a cada chamada recursiva.
#Parâmetros:

#n: O número para o qual você quer calcular o fatorial.

#acumulador: Acumula o resultado das multiplicações, iniciando em 1.

#if n == 0: Condição base da recursão. Quando n chega a zero, a recursão termina.

#return fatorial_otimizado(n-1, n * acumulador) A função se chama recursivamente, reduzindo n e multiplicando o acumulador pelo valor atual de n.

#Comparação entre as duas funções fatoriais:

#fatorial_otimizado tenta minimizar o uso de memória acumulando o resultado, mas não evita o limite de recursão do Python.

#fatorial é mais direta, mas também está sujeita ao limite de profundidade de recursão.

#Nota importante: Embora essa abordagem tente otimizar a recursão, o Python não otimiza chamadas de cauda nativamente. 
#Isso significa que, para valores grandes de n, você ainda pode encontrar um erro de recursão máxima excedida.
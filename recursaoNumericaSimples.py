
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
#O que faz: Calcula o fatorial de um número usando recursão simples.

#if n == 0: Condição base da recursão. Define que o fatorial de 0 é 1.

#return n * fatorial(n-1) A função chama a si mesma com n-1, multiplicando o resultado por n atual.
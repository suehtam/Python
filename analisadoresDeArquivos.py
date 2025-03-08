import csv
def analisar_csv(nome_do_arquivo):
    with open(nome_do_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            yield linha

#O que faz: Lê um arquivo CSV e retorna um gerador que produz cada linha do arquivo, uma por vez.
#with open(nome_do_arquivo, 'r') as arquivo: Abre o arquivo especificado em modo leitura. 
#O uso do with garante que o arquivo será fechado corretamente após o uso.

#leitor = csv.reader(arquivo) Cria um objeto leitor que interpretará o arquivo como um CSV.

#for linha in leitor: Itera sobre cada linha do arquivo CSV.

#yield linha Em vez de retornar todas as linhas de uma vez, a função produz uma linha por vez, tornando-se um gerador. 
#Isso é eficiente em termos de memória, especialmente para arquivos grandes.

#Por que é útil: Geradores permitem processar grandes volumes de dados sem carregar tudo na memória.
#Isso é ideal para trabalhar com grandes conjuntos de dados em aplicativos de data science ou processamento de dados.
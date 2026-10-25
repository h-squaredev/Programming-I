# Função que lê um arquivo de números inteiros e imprime a soma desses números
def ler_e_soma():

    arquivo = open ('entrada.txt', 'r') #abrindo o arquivo no modo leitura
    soma = 0
    for linha in arquivo:
        soma += int( linha)

    arquivo.close() #fechando o arquivo
    print(soma)

if __name__ == "__main__":
    ler_e_soma()





# Função que escreve a soma dos números inteiros lidos de um arquivo em outro arquivo
def escreve_arquivo():

    arquivo2 = open ( 'saida.txt', 'w') #abrindo o arquivo no modo escrita
    for linha in range(4):
        arquivo2.write ("batata") #escrevendo no arquivo
    arquivo2.close() #fechando o arquivo
    
if __name__ == "__main__":
    escreve_arquivo()

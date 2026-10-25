'''
UFMT - Ciencia da Computacao
Programacao de computadores
prof. Ivairton

Exemplo de codigo que manipula matriz em Python
'''

# Funcao principal
def main():
    matriz = [] # Cria uma matriz vazia
    print("Digite os elementos da matriz 3x3:") # msg para o usuario
    for i in range(3):  # este laco irah percorrer as linhas
        linha = [] # cria um vetor que representa cada linha (uma matriz é um conjunto de linhas)
        for j in range(3): # este laco irah percorrer cada item (coluna) do vetor que representa a linha
            valor = int(input(f"Valor na posicao [{i}][{j}]: ")) # le o valor do usuario
            linha.append(valor) # adiciona o valor lido ao final do vetor
        matriz.append(linha) # adiciona a linha (vetor) na matriz
    
    print("\nSomatorio:")
    somatorio = 0 # inicializa somador
    for i in range(3): # laco que percorre as linhas
        for j in range(3): # laco que percorre as colunas de cada linha
            somatorio += matriz[i][j] # acumula/soma o valor da posicao [i][j] no somatorio
        
    print(f"A soma de todos os valores da matriz eh: {somatorio}")

if __name__ == "__main__":
    main()
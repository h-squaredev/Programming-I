'''
UFMT - Ciencia da Computacao
Programacao de computadores
prof. Ivairton

Exemplo de codigo que manipula vetor em Python
'''

# Funcao principal
def main():
    vetor = []  # cria um vetor vazio

    # laco para leitura dos valores
    for i in range(10):     # estabelece uma sequencia de valores de 0 a 9 (10 fica fora)
        numero = int(input(f"Digite o {i+1}o numero:"))    # le um numero inteiro e armazena na variavel chamada numero
        vetor.append(numero)    # adiciona o numero ao final do vetor (comando append)
    
    # vamos somar todos os valores armazenados no vetor
    soma = 0    # inicializa somador
    for num in vetor:       # este laco percorre todos os elementos do vetor, mas a variavel de controle (num) assume cada valor (e nao o indice)
        soma += num
            
    print(f"Soma dos valores = {soma}")

if __name__ == "__main__":
    main()
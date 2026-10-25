#Função que subtrai dois números
def subtracao(a, b):
    return a - b

#Função que soma dois números
def soma(a, b):
    return a + b

#Função que multiplica dois números
def multiplicacao(a, b):
    return a * b

#Função que divide dois números
def divisao(a, b):
    return a / b

#Função principal
def main():
    continua = True
    while (continua):
        operacao = int(input("Qual operação deseja realizar? \n 1 - subtração \n 2 - soma \n 3 - multiplicação \n 4 - divisão \n")) #Entrada da operação desejada
        result_op = operacao #Variável que armazena o nome da operação escolhida

        if result_op == 1:
            print("Você escolheu a operação de subtração")
            v1 = int(input("Digite o primeiro valor: ")) #Entrada do primeiro valor
            v2 = int(input("Digite o segundo valor: ")) #Entrada do segundo valor

            resultado = subtracao(v1, v2) #Calcula a subtração dos dois valores por meio da função soma

        elif result_op == 2:
            print("Você escolheu a operação de soma")
            v1 = int(input("Digite o primeiro valor: ")) #Entrada do primeiro valor
            v2 = int(input("Digite o segundo valor: ")) #Entrada do segundo valor

            resultado = soma(v1, v2) #Calcula a soma dos dois valores por meio da função soma

        elif result_op == 3:
            print("Você escolheu a operação de multiplicação")
            v1 = int(input("Digite o primeiro valor: ")) #Entrada do primeiro valor
            v2 = int(input("Digite o segundo valor: ")) #Entrada do segundo valor

            resultado = multiplicacao(v1, v2) #Calcula a multiplicação dos dois valores por meio da função soma

        elif result_op == 4:
            print("Você escolheu a operação de divisão")
            v1 = int(input("Digite o primeiro valor: ")) #Entrada do primeiro valor
            v2 = int(input("Digite o segundo valor: ")) #Entrada do segundo valor

            resultado = divisao(v1, v2) #Calcula a divisão dos dois valores por meio da função soma
            
        else:
            print("Operação inválida")
            return
        
        #Exibe o resultado final
        print(f"A soma entre {v1} e {v2} é igual a {resultado}")

        #Pergunta se o usuário deseja continuar
        continua = input("Deseja realizar outra operação? ( s / n ) ")

        if continua != "s":
            continua = False
            print("Programa finalizado")
        else:
            continua = True


if __name__ == "__main__":
    main()
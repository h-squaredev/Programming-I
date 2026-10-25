def calculo(preco_custo, valor_porcent):
    return preco_custo + (preco_custo * valor_porcent / 100)


def main():

    produtos, custo, porcentagem = [], [], []
    for i in range(8):
        nomes = input(f"Digite o nome do {i+1}o produto:")
        produtos.append(nomes)
        preco_custo = float(input(f"Escreva seu custo: "))
        custo.append(preco_custo)
        valor_porcent = float(input(f"Agora sua % sem o simbolo '%': "))
        porcentagem.append(valor_porcent)

    print("\nRELATORIO DE VENDAS")
    print("Produto\tCusto\tPorcentagem\tPreco de Venda")
    for i in range(8):
        preco_venda = calculo(custo[i], porcentagem[i])
        print(f"{produtos[i]}\t{custo[i]:.2f}\t{porcentagem[i]:.2f}\t\t{preco_venda:.2f}")

if __name__ == "__main__":
    main()
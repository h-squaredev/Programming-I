'''
UFMT - Ciencia da Computacao
Programacao de computadores
prof. Ivairton
Trabalho 1 - Programacao 1
Data: 13/09/2025

Aluno 1: Humberto Henrique Castro Rocha - 202512722003
Aluno 2: Joao Victor Brito do Nascimento - 202511722014

Introdução a Análise Explratoria de Dados com Python
'''

#Importando as bibliotecas necessárias
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

from sklearn.datasets import fetch_california_housing #Importando a base de dados (dataset) da fetch_california_housing

def main():
    california = fetch_california_housing() #Carregamos a base de dados
    X = california.data [:, 0:8] #Atribuímos as variáveis preditoras (features) a variável X, selecionando todas as linhas e as 8 primeiras colunas
    Y = california.target #Atribuímos a variável alvo (target) a variável y
    
    feature_names = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms','Population', 'AveOccup', 'Latitude', 'Longitude'] #Definimos os nomes das variáveis preditoras
    
    df = pd.DataFrame(X, columns = feature_names) #Criamos um DataFrame com os dados
    df['MedHouseVal'] = Y #Adicionamos a variável alvo ao DataFrame


#requisito 3
    print("\nCalculo das Métricas")

    colunas_interesse = ["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup"]
    
    for coluna  in colunas_interesse: #codigo que calcula as métricas
        print(f"\n variavel: {coluna}") #a variavel coluna recebe o primeiro item da lista e depois os outros 

        #média 
        media = df[coluna].mean() #"df" é o data frame ,"coluna" e a variavel dentro do for que muda a cada iteração e o "mean" metodo que soma todos os valores da coluna e divide pelo numeros de colunas para tem a média
        print(f"Média: {media: .4f}") #imprime o texto "média: e o seguido do vslor da variavel media" o 4f formata o numero para 4 casas decimais

        #mediana
        mediana = df[coluna].median() #mesma explicação da "média"
        print(f"Mediana: {mediana: .4f}")

        #moda
        moda = df[coluna].mode()[0] #mesma explicação da "média" mas com um detalhe o "[0]" serve para garantir que extraia o valor numérico para a variavel moda
        print(f"moda: {moda: .4f}")

        #variância 
        variancia = df[coluna].var() #mesma explicação da "média"
        print(f"variância: {variancia: .4f} ")

        #desvio padrão
        desvio_padrao = df[coluna].std() #mesma explicação da "média"
        print(f"desvio padrão: {desvio_padrao: .4f}")

        #intervalo interquantil\IQR
        Q1 = df[coluna].quantile(0.25) #o "quantile" calcula o quartil de uma série de dados ao passar pelo "(0.25)" ele retorna o valor que é igual 25º ou conhecido tbm como primeiro quartil  
        Q3 = df[coluna].quantile(0.75)  #este fas a mesma so que ele calcula o "(0.75)" ou 75º quartil ou conhecido tambem como terceiro quartil
        IQR = Q3 - Q1 #está é a variavel que irá guaradar o resultado final o "Q3 - Q1" é a diferença entre o 3º e 1º quartil 

        print(f"1º (Q1): {Q1: .4f}")
        print(f"2º (Q3): {Q3: .4f}")
        print(f"intervalo interquartil (IQR): {IQR: .4f}")



#Antes de fazer o requesito 1, adcionarei um dicionário para arredondar os valores do describe
    arredondamento_describe = {'MedInc': 2, 'HouseAge': 2, 'AveRooms': 2, 'AveBedrms': 2, 'Population': 0, 'AveOccup': 2, 'Latitude': 2, 'Longitude': 2, 'MedHouseVal': 3}


#requisito 1 ↓
    print("\n Gerando a tabela de descrição estatística")
    df_descricao = df.describe() #executa o describe e guarda na variável df_descricao
    df_descricao = df_descricao.round(arredondamento_describe) #aplica o arredondamento conforme o dicionário

#Configura a janela
    fig, axes = plt.subplots(2, 2, figsize = (14, 12)) # Ajuste o tamanho conforme necessário


#Cria a tabela
    ax_tabela = plt.subplot2grid((2, 2), (0, 0), colspan = 2) # Cria um subplot que ocupa 2 colunas
    ax_tabela.axis('off') # Desliga os eixos
    tabela = ax_tabela.table(

        #define os dados da tabela
        cellText = df_descricao.values,   #Adiciona os valores da tabela
        colLabels = df_descricao.columns, #Adiciona os nomes das colunas
        rowLabels = df_descricao.index,   #Adiciona os nomes das linhas
        loc = 'center',   #Centraliza a tabela
        cellLoc = 'center' #Centraliza os textos
    )

#retira os eixos
    
    tabela.set_fontsize(10) #Define o tamanho da fonte
    tabela.scale(1, 1.5)  #Ajusta o tamanho da tabela

    fig.suptitle('Descrição Estatística - California Housing', fontsize = 16,) #Adiciona o título
    fig.tight_layout() #Ajusta o layout





# fazendo o REQUISITO 2 ↓
    print("\n Gerando o mapa de dispersão (Latitude x Longitude)")
    ax_separacao = axes[1, 0] # Pega o subplot/coluna repartida de inferior esquerda

    sns.scatterplot(
        data = df,
        x = "Longitude",
        y = "Latitude",
        alpha = 0.4,
        ax = ax_separacao  # Diz ao Seaborn para desenhar neste subplot específico
    )
    
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    

# fazendo o REQUISITO 4 ↓

    print("\n Gerando o Boxplot")

    fig, axes = plt.subplots(2, 3, figsize = (18, 10)) # Criamos uma figura com uma grade de 2 linhas e 3 colunas
    fig.suptitle('Boxplot de Cada Variável', fontsize = 20)


    var_req4 = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']

    for coluna, ax in zip(var_req4, axes.flat):
        
     # Desenha um bloxplot para a 'coluna' atual no 'ax' (eixo) atual
        sns.boxplot(data = df, x = coluna, orient = "h", ax = ax)
        


    print("\n Gerando o Histograma em outra janela")
    
    fig, axes = plt.subplots(2, 3, figsize = (18, 10)) # Criamos uma figura com uma grade de 2 linhas e 3 colunas
    fig.suptitle('Histograma de Cada Variável', fontsize=20)

    # O 'axes.flat' transforma nossa grade 2x3 em uma lista simples para facilitar o loop
    for coluna, ax in zip(var_req4, axes.flat):  # O 'zip' nos permite percorrer a lista de colunas e a lista de eixos ao mesmo tempo

        sns.histplot(data = df, x = coluna, kde = True, ax = ax)
        ax.set_title(f'Distribuição de {coluna}', fontsize = 14)
        ax.set_xlabel('') # Opcional: remove o label x de cada subplot)


    plt.tight_layout(rect = [0, 0, 1, 0.96]) # Ajusta o layout para o título geral caber





#requisito 5
    print("\n Identificar correlações")
    matriz_correlacao = df.corr() #"corr" e a função que percorre todas as colunas numericas do df e calcula o coeficiente de correlação entre elas

    print("\n Matriz de Correlação")

    plt.figure(figsize = (12,10),) #ajusta o tamanho da figura largura e altura
    sns.heatmap(matriz_correlacao, ##"sns.heatmap" função que gera o mapa de calor
        annot = True, #"annot = true" mostra os valores numericos da correlação
        cmap = "coolwarm", #define as cores, cores quentes como vermelho define correlações positivas e cores frias como azul definem correlações negativas
        fmt = ".2f", #formata o numero para que tenham 2 casas decimais
        linewidths = .5 #define a espessura das linhas que separam os quadrados do mapa de calor
        ) 
    
    plt.yticks(rotation=0) #mantem os nomes das linhas na horizontal para não emabaraçar
    
    plt.title("Mapa de calor da Matriz de Correlação")


    print("\n Analisando as correlações com MedHouseVal")

    correlacao_with_target = matriz_correlacao["MedHouseVal"].sort_values(ascending = False) #seleciona a coluna "MedHouseVal" da matriz de correlação e ordena os valores em ordem decrescente
    print(correlacao_with_target) #imprime a série resultante no terminal





# EXIBIÇÃO FINAL
    plt.show()

    
if __name__ == "__main__":
    main()
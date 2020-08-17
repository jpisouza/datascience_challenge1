# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:38:18 2020

@author: João Paulo Innocente de Souza
"""
import pandas as pd
import numpy as np

report = pd.read_csv("Relatorio.csv", sep=';')#carrega o arquivo de input

#separa as colunas em listas------------------------
classificadas = report['Classificadas'].tolist()

reais = report['Reais'].tolist()
#---------------------------------------------------

lista_intencoes_unicas = [] #cria lista de intenções únicas
contador = 0

for intencao in reais:
    if intencao not in lista_intencoes_unicas:
        lista_intencoes_unicas.append(intencao)#atualiza a lista
        contador+=1
for intencao in classificadas:
    if intencao not in lista_intencoes_unicas:
        lista_intencoes_unicas.append(intencao)#atualiza a lista
        contador+=1

matriz_confusao = np.zeros((len(lista_intencoes_unicas),len(lista_intencoes_unicas))) #aloca a matriz de confusão
lista_agrupamento = []

#escreve na matriz de confusão a contagem errada, na qual o elemento i foi 'confundido' com o j. O elemento ii representa acerto
for i in range(len(classificadas)):
    matriz_confusao[lista_intencoes_unicas.index(classificadas[i]),lista_intencoes_unicas.index(reais[i])] +=1


for linha in range(len(matriz_confusao)): #percorre as linhas da matriz
    for coluna in range(len(matriz_confusao[0])):#percorre as colunas da matriz
    #verifica se os acertos dos elementos i e do elemento j somados são maiores que os erros de cada um, ou seja, as vezes em que o elemento i foi confundido
    #com o elemento j da lista de intenções únicas. Lembrando que os elementos ii e jj representam acertos (diagonal da matriz)
        if ((matriz_confusao[linha,coluna] + matriz_confusao[linha,coluna]>= matriz_confusao[linha,linha] + matriz_confusao[coluna,coluna]) and (linha != coluna)): 
            #verifica se o par de agrupamento já não consta na lista de agrupamentos
            if ([lista_intencoes_unicas[linha],lista_intencoes_unicas[coluna]] not in lista_agrupamento)  and ([lista_intencoes_unicas[coluna],lista_intencoes_unicas[linha]] not in lista_agrupamento):
                lista_agrupamento.append([lista_intencoes_unicas[linha],lista_intencoes_unicas[coluna]])
                

print(matriz_confusao)
print (lista_agrupamento)
            
        
    



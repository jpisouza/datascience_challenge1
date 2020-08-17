# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:38:18 2020

@author: João Paulo Innocente de Souza
"""
import pandas as pd

report = pd.read_csv("Relatorio.csv", sep=';') #carrega o arquivo de input

#separa as colunas em listas--------------------
classificadas = report['Classificadas'].tolist()

reais = report['Reais'].tolist()
#-----------------------------------------------

lista_intencoes_unicas = [] #criação de lista de intenções únicas
contador = 0 #conta as intençõs únicas adicionadas à lista

for intencao in reais: #loop na coluna de intenções reais
    if intencao not in lista_intencoes_unicas:
        lista_intencoes_unicas.append(intencao)
        contador+=1
for intencao in classificadas: #loop na coluna de intenções classificadas (pois pode ter intenções classificadas que, para esta amostra, não aparecem nas reais)
    if intencao not in lista_intencoes_unicas:
        lista_intencoes_unicas.append(intencao)
        contador+=1

#imprime os valores pedidos
print('O número de intenções únicas é %i.' %(contador))
print(lista_intencoes_unicas)

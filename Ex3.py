# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:38:18 2020

@author: João Paulo Innocente de Souza
"""
import pandas as pd

report = pd.read_csv("Relatorio.csv", sep=';')#carrega o arquivo de input

#separa as colunas em listas------------------------
classificadas = report['Classificadas'].tolist()

reais = report['Reais'].tolist()
#---------------------------------------------------

#cria dicionário de intenções únicas para guardar, em cada intenção, a incidência na lista de classificadas,
#os acertos e a precisão (acertos/incidência)
intencoes_unicas = {} 
lista_intencoes_unicas = []

for intencao in reais:
    if intencao not in intencoes_unicas:
        intencoes_unicas[intencao]=[0,0,0] #[incidência, acertos, precisão]
        lista_intencoes_unicas.append(intencao) #atualiza a lista
for intencao in classificadas:
    if intencao not in lista_intencoes_unicas:
        intencoes_unicas[intencao]=[0,0,0] #[incidência, acertos, precisão]
        lista_intencoes_unicas.append(intencao)#atualiza a lista

#dicionário dos extremos da precisão, em que o valor é [nome da intenção, valor da precisão]
extremos = {'menor precisao': [None,None], 'maior precisao': [None,None]} 
menor = 1.0
maior=0.0

for intencao in intencoes_unicas: #loop na lista de intenções únicas
    for i in range(len(classificadas)):
        if classificadas[i] == intencao:
           intencoes_unicas[intencao][0]+=1 #atualiza incidência
           if classificadas[i] == reais[i]:
               intencoes_unicas[intencao][1]+=1 #atualiza acertos
    intencoes_unicas[intencao][2]= float(intencoes_unicas[intencao][1])/float(intencoes_unicas[intencao][0]) #atualiza precisão
    if intencoes_unicas [intencao][2] <= menor:
        menor = intencoes_unicas [intencao][2] #calcula menor precisão e adiciona ao dicionário 
        extremos['menor precisao'] = [intencao, menor]
    elif intencoes_unicas [intencao][2] >= maior:
        maior = intencoes_unicas [intencao][2]#calcula maior precisão e adiciona ao dicionário
        extremos['maior precisao'] = [intencao, maior]

#imprime os resultados
print('A intenção com menor precisão é %s, com %f.A intenção com maior precisão é %s, com %f.' %(extremos['menor precisao'][0],extremos['menor precisao'][1],extremos['maior precisao'][0],extremos['maior precisao'][1]))
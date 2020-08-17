# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:38:18 2020

@author: João Paulo Innocente de Souza
"""
import pandas as pd

report = pd.read_csv("Relatorio.csv", sep=';') #carrega o arquivo de input

#separa as colunas em listas------------------------
classificadas = report['Classificadas'].tolist() 

reais = report['Reais'].tolist()
#----------------------------------------------------

acertos = 0

for i in range (len(reais)): #conta os acertos para calcular a acurácia
    if reais[i]==classificadas[i]: #verificação de acertos
        acertos+=1 #incremento de acertos
        
acuracia = float(acertos)/float(len(reais)) #calcula a acurácia

#imprime os valores pedidos
print('A acurácia do teste é %f.' %(acuracia))



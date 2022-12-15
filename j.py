import json
#Trabalhando com json em python

campos = ['title','url', 'lastVisitTimeLocal'] #Defina os campos que serão retornados

with open('arq.json') as f: #Abra o arquivo
    entrada = json.load(f)

saida = {campo:[] for campo in campos} 

for elemento in entrada:
    for campo in campos:
        saida[campo].append(elemento[campo])

print(saida) #A saída será em JSON
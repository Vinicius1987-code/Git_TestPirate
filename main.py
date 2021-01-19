from dados import *
import json


# Aqui é realizado a conversão de python para json.
# Dados.py --> Uf_dicionario.json

with open('UF_dicionario.json', 'w') as arquivo:
    json.dump(UF_dicionario, arquivo, indent=4)


# saída convertida em json (string)
dados = json.dumps(UF_dicionario, indent=4)
#print (type(dados))
print (dados)




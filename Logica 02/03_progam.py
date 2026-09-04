matriz_vazia = []

#exemplo de matriz 2x2 preenchidas com 0
linhas = 2
colunas = 2
for i in range(linhas):
 linha=[]
 for j in range(colunas):
    linha.append(0)
matriz_vazia.append(linha)

print("Matriz criada vazia e preenchida com zeros:")
print(matriz_vazia)
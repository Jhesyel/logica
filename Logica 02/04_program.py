jogo_velha = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("matriz estruturada")
print(jogo_velha[0])
print(jogo_velha[1])
print(jogo_velha[2])

print("\n---vez do x---")
escolha_x = int(input("Digite um número de 1 a 9:"))
#buscar o número para substituir por X
encontrou_x = False
for l in range(3):
    for c in range(3):
         if jogo_velha[l][c] == escolha_x:
              jogo_velha[l][c] = "X"
              encontrou_x = True

#exibe o tabuleiro atualizado para ver o resultado
if encontrou_x:
     print("\nApós jogada de X:")
     print(jogo_velha[0])
     print(jogo_velha[1])
     print(jogo_velha[2])

     print("\n---vez de O---")
     escolha_o = int(input("Digite um número de 1 a 9:"))
#buscar o número para substituir por O
     encontrou_o = False
for l in range(3):
    for c in range(3):
         if jogo_velha[l][c] == escolha_o:
              jogo_velha[l][c] = "O"
              encontrou_o = True

    if encontrou_o:
        print("\nApós jogada de O:")
        print(jogo_velha[0])
        print(jogo_velha[1])
        print(jogo_velha[2])
    else:
        print("Número inválido ou já ocupado!")
else:
    print("Número inválido")

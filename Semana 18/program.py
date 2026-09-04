print ("Bem-vindo professor")
#entrada de dados
nota1=float(input("digite a primeira nota: "))
nota2=float(input("digite a segunda nota: "))
nota3=float(input("digite a terceira nota: "))
frequencia=float(input("digite a frequência 0 a 100(%): "))

#validação (notas inválidas <0 ou >10)
if (nota1<0 or nota1>10 or
    nota2<0 or nota2>10 or
    nota3<0 or nota3>10):
    print("Erro:nota(s) inválida por favor digite uma nota de 0 a 10")

#validação de frequência
elif frequencia <0 or frequencia>100:
    print("Erro: frequência inválida por favor digite uma frequência de 0 a 100")
#calcular frequência
else:
    média=(nota1+nota2+nota3)/3
    print(f"media final:{média:.2f})")

    if frequencia <75:
        print("situação:Reprovado por faltas")
    elif média>=7:
        print("situação:Aprovado na média")
    elif média>=4:
        print("situação:Exame")
        print(f"faltam: {7-média:.2f} pontos para ser aprovado direto")
    else:
        print("situação:reprovado")
        print(f"faltam: {7-média:.2f} pontos para ser aprovado")
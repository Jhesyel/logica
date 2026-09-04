num1 =0.0
num2 =0.0
resultado =0.0
operador = ""

#criamos a função
def calcular(n1: float,n2: float,op: str)->float:
    "realiza o calculo com base no operador fornecido"
    if op == "+":
         return n1 + n2
    elif op == "-":
         return n1 - n2
    elif op == "*":
         return n1 * n2
    elif op == "/":
        if n2 !=0:
          return n1 / n2
        else: 
            print("Erro divisão por zero!")
            return 0.0
    else:
        print("Operador inválido!")
        return 0.0

#algoritmo principal
num1 = float(input("Digite o primeiro número:"))
operador = (input("Digite o operador(+)"))
num2 = float(input("Digite o segundo número:"))

resultado = calcular(num1, num2, operador)
print("O resultado da operação é: {resultado}") 
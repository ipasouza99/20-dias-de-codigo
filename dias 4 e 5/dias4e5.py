x = float(input("Digite o primeiro número:"))
y = float(input("Digite o segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = x + y
elif operação == "-":
    resultado = x - y
elif operação == "*":
    resultado = x * y
elif operação == "/":
    resultado = x / y
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)
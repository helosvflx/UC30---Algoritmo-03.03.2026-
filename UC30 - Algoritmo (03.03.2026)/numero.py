entrada = input("Digite um número inteiro positivo: ")
numero = int(entrada)

if numero % 2 == 0:
    resultado = numero ** 2
    print(f"O número {numero} é par. O seu cubo é: {resultado}")
else:
    resultado = numero ** 3
    print(f"O número {numero} é ímpar. O seu cubo é: {resultado}")

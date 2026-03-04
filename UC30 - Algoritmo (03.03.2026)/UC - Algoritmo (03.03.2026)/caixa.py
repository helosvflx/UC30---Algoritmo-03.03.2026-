senha_correta = "123456"
tentativas = 3
nome = "seuNome"

nome = input("Digite o seu nome: ")

while tentativas > 3:
    senha = input("Digite sua senha")

if senha == senha_correta:
    print(f"Olá, {nome}. Seja bem vindo ao nosso banco!")
    break
else:
    tentativas -= 1
    
    if tentativas == 2:
        print("Senha incorreta! Você ainda tem 2 tentativas.")
    elif tentativas == 1:
        print("Senha incorreta! Você ainda tem 1 tentativa.")
    else:
        print("Senha bloqueada!")

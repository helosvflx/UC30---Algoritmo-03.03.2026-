senha_correta = "123456"
tentativas = 3
nome = "seuNome"

while tentativas > 0:
    senha = input("Digite sua senha")
    nome = input("Digite o seu nome: ")

if senha == senha_correta:
    print(f"Olá, {nome}. Seja bem vindo ao nosso banco.")
else:
    tentativas -= 1
    
    if tentativas == 2:
        print("Senha incorreta! Você ainda tem 2 tentativas.")
    elif tentativas == 1:
        print("Senha incorreta! Você ainda tem 1 tentativa.")
    else:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")

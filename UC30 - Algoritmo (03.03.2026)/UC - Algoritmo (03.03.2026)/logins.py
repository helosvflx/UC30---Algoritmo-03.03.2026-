login1 = "procopio"
senha1 = 12345
login2 = "paiva"
senha2 = 54321

login1 = input("Digite o seu primeiro login: ")
senha1 = input("Digite a senha: ")

if login1 == "procopio" and senha1 == 12345:
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem.")


login2 = input("Digite o seu segundo login: ")
senha2 = input("Digite a senha: ")

if login2 == "paiva" and senha2 == 54321:
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem.")
cadastrarUsuario = (lambda: open("q2_ItaloSantos.txt", "a").write(input("Digite o nome de usuario: ") + " " + input("Digite a senha: ") + "\n"))

fazerLogin = (lambda: print("SUCESSO") if any((lambda login, senha: login + " " + senha)(input("Digite o nome de usuario: "), input("Digite a senha: ")) in line for line in open("q2_ItaloSantos.txt")) else print("FRACASSO"))

while True:
    print("\nBem-vindo! Escolha uma opcao:")
    print("(1) Cadastrar-se")
    print("(2) Logar-se")
    print("(3) Sair")


    opc = input("Escolha a opção: ")
    match opc:

        case '1':
            cadastrarUsuario
        case '2':
            fazerLogin
        case '3':
            exit()
        case _:
            print("Opção inválida. Tente novamente.")

from challenge.Bank import BankAccount

def access_account() -> BankAccount:
    bank_account = BankAccount(0, "Indigente", "0", 0) # Inicializar uma variável para definir que o usuário está sem Login
    return bank_account

user_bank = access_account()
if user_bank.name == "Indigente": # Caso o nome seja "indigente" significa que o usuário acabou de abrir o programa, então ele deve realizar o acesso em sua conta
    print("\n" * 30) # 'Limpar' o CMD para facilitar a leitura dos textos
    print(f"Olá usuário! Seja bem-vindo(a) ao sistema de banco!\nFunciona da seguinte forma:\n- Se você preencher com as informações abaixo, você acessa a conta\n- Se optar por criar uma nova conta, basta preencher com informações diferentes das de baixo!")

    user_bank.list_accounts()

    account_id = int(input("Digite o ID da conta que deseja acessar - "))
    account_name = input("Digite o Nome da conta que deseja acessar - ")
    account_cpf = input("Quase lá... para confirmar, digite o CPF - ")

    user_bank = BankAccount(account_id, account_name, account_cpf, 0) # Agora o usuário acessa essa conta e realiza saques e tranferências por ela

    if not user_bank.check_creation():  # Se a conta não existir, cria uma nova
        print("Conta não encontrada. Criando uma nova conta...")
        new_account = user_bank.create_account_data()  # Cria o dicionário de uma nova conta
        user_bank.update_system(new_account)  # Atualiza o sistema com a nova conta
    else:
        print("*" * 40)
        print(f"Conta já existente, acesso liberado. Saldo atual: {user_bank.balance}")


while True:
    print("*" * 40)
    print(f"Banco Pegazus\n- Usuário logado: {user_bank.name}")
    print("*" * 40)
    print("1 - Listar contas")
    print("2 - Realizar depósito")
    print("3 - Realizar saque")
    print("4 - Listar suas contas")
    print("5 - Sair")
    print("*" * 40)

    # Tratamento de exceções para evitar que o usuário digite um valor que não seja um número inteiro
    try:
        user_choice = int(input("Para continuar selecione uma opção - "))
    except ValueError:
        print("O programa só aceita números!")

    # Verificar a opção digitada pelo usuário e chamar uma função baseada nessa informação
    match user_choice:
        case 1:
            user_bank.list_accounts()
        case 2:
            user_bank.deposit_account()
        case 3:
            user_bank.withdraw_account()
        case 4:
            print("Encerrando o programa...")
            break
        case _:
            print("Opção inválida, encerrando o programa!")
            break

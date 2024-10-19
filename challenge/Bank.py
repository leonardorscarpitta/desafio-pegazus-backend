import json

class BankAccount:
    def __init__(self, account_id: int, name: str, cpf: str , balance: float ):
        self.id: int = account_id
        self.name: str = name
        self.cpf: str = cpf
        self.balance: float = balance


    def read_data(self) -> dict:
        try:
            with open("accounts.json", "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {} # Caso não exista o arquivo JSON, o programa deve criar um novo


    def list_accounts(self) -> None:
        account_list = self.read_data()
        count = 1
        print("ID".center(5) + " | " + "Nome da conta".center(30) + " | " + "CPF".center(15))
        for k,v in account_list.items():
            counter = str(count)
            print(counter.center(5) + " | " + k.center(30) + " | " + v["cpf"].center(15))
            count += 1

    def check_creation(self) -> dict:
        """
        Verifica se a conta já existe no sistema e retorna o saldo se existir.
        Se não existir, atribui o próximo ID disponível.
        """
        bank_data = self.read_data()

        # Verificar pelo CPF se a conta já existe
        for account_name, account_info in bank_data.items():
            if account_info["cpf"] == self.cpf:
                self.id = account_info["id"]  # Atualiza o ID da conta
                self.balance = account_info["balance"]  # Carrega o saldo existente
                return True  # Conta encontrada

        # Se a conta não existe, atribuir o próximo ID disponível
        if bank_data:
            max_id = max(account_info["id"] for account_info in bank_data.values())
            self.id = max_id + 1  # Atribui o próximo ID disponível
        else:
            self.id = 1  # Se não houver contas, inicia o ID como 1
        return False  # Conta não encontrada


    def create_account_data(self) -> dict:
        """
        Cria os dados da conta, caso ela não exista.
        :return: dict
        """
        return {
            self.name: {
                "id": self.id,
                "cpf": self.cpf,
                "balance": self.balance,
            }
        }


    def update_system(self, new_data: dict) -> None:
        """
        Atualiza os dados do sistema com uma nova conta.
        """
        bank_data = self.read_data()

        # Atualiza os dados existentes com a nova conta
        bank_data.update(new_data)

        # Grava os dados atualizados no arquivo JSON
        with open("accounts.json", "w", encoding="utf-8") as json_file:
            json.dump(bank_data, json_file, ensure_ascii=False, indent=4)
        print("Sistema atualizado com sucesso!")


    def withdraw_account(self) -> None:
        try:
            value: float = float(input("Digite o valor a ser sacado - "))
        except ValueError:
            print("Valor Inválido!")
        accounts_data = self.read_data()
        for account in accounts_data.values():
            if account["cpf"] == self.cpf:
                if value <= account["balance"]:
                    account["balance"] -= value
                    new_data = {self.name: {"id": self.id, "cpf": self.cpf, "balance": account["balance"]}}
                    self.update_system(new_data)
                    print(f"Valor de {value} sacado com sucesso!")
                else:
                    print("Saldo insuficiente!")


    def deposit_account(self) -> None:
        try:
            value: float = float(input("Digite o valor a ser depositado - "))
        except ValueError:
            print("Valor Inválido!")
        accounts_data = self.read_data()
        for account in accounts_data.values():
            if account["cpf"] == self.cpf:
                account["balance"] += value
                new_data = {self.name: {"id": self.id, "cpf": self.cpf, "balance": account["balance"]}}
                self.update_system(new_data)
                print(f"Valor de {value} depositado com sucesso!")

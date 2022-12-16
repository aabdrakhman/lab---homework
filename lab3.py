from enum import Enum

class Account(Enum):
    KZT = 'KZT'
    USD = 'USD'


class BankAccount:
    name: str
    surname: str
    cash: float=0
    wallet_type: Account

    def __init__(self, name:str, surname:str, wallet_type:Account):
        self.name = name
        self.surname = surname
        self.wallet_type = wallet_type


    def add_to_bank_account(self, sum:float)->None:
        self.cash += sum
    

    def substract_from_bank_account(self, sum:float)->None:
        self.cash -= sum


    def get_cash(self) -> str:
        return f'{self.cash} {self.wallet_type.value}'


    def wallet_conversation(self, new_wallet_type:Account) -> None:
        if new_wallet_type == Account.KZT:
            if self.wallet_type == Account.USD:
                self.cash *= 470
                self.wallet_type = Account.KZT
        elif new_wallet_type == Account.USD:
            if self.wallet_type == Account.KZT:
                self.cash /= 470
                self.wallet_type = Account.USD


    def __repr__(self) -> str:
        return self.get_cash()
    

accounts = []

while True:
    command = int(input(
        'Выберите команду:\n 1.Создание пользователя\n 2.Выбрать пользователя\n 0.Выйти\n'
    ))

    if command==1:
        name = input('Имя: ')
        surname = input('Фамилия: ')
        wallet_type = Account(input('Валюта: '))
        user = BankAccount(name, surname, wallet_type)
        users = {'name':user.name, 'surname':user.surname, 'wallet_type':user.wallet_type}
        accounts.append(users)
        print('Пользователь успешно создан')

    elif command==2:
        for i in range(len(accounts)):
            print(i, accounts[i]['name'], accounts[i]['surname'], '\n')
        choise = int(input())
        if choise==0:
            user = BankAccount(users['name'], users['surname'], users['wallet_type'])
            while True:
                command = int(input(
                    'Выберите команду:\n 1.Пополнить счет\n 2.Снять с счета\n 3.Выбрать тип валюты\n 4.Вывести баланс\n 0.Завершить\n'
                ))
                match command:
                    case 1:
                        sum = int(input('Введите сумму: '))
                        user.add_to_bank_account(sum)
                        print(user.cash)
                    case 2:
                        sum = int(input('Введите сумму: '))
                        user.substract_from_bank_account(sum)
                        print(user.cash)
                    case 3:
                        new_wallet_type = Account(input('Выберите тип валюты: '))
                        user.wallet_conversation(new_wallet_type)
                        print(user.cash)
                    case 4:
                        print(user)
                    case 0:
                        break

    elif command==0:
        break    

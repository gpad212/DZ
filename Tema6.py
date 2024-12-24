from datetime import datetime
import os
def log(name,balance,action):
    # d = [datetime.strftime(datetime.now(),'%d:%b:%Y %H:%M:%S'), action + name, "Баланс - " + str(balance)]
    # print(d)
    with open("balance_log_tema6.txt", 'a', encoding="utf-8") as f:
        d = datetime.strftime(datetime.now(),'%d:%b:%Y %H:%M:%S') + action + name + "Баланс - " + str(balance) + "/n"
        f.write(f'{datetime.strftime(datetime.now(),"%d:%b:%Y %H:%M:%S")} : {action} - {name} : Баланс - {str(balance)} \n')
class Account():
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        log(self.name,self.balance,"Создание аккаунта")

    def withdraw_money(self):
        try:
            money = int(input(f"Введите сумму которую хотите снять со счета {self.name}: "))
            if money > self.balance:
                print("Недостаточно средств")
            else:
                self.balance -= money
                print(f'Ваш баланс: {self.balance}')
                log(self.name, self.balance, "Списание средств")
        except:
            print("Вы ввели не число, попробуйте еще раз")
    def deposit_money(self):
        try:
            money = int(input(f"Введите сумму которую хотите положить на счет {self.name}: "))
            self.balance += money
            print(f'Ваш баланс: {self.balance}')
            log(self.name, self.balance, "Пополнение средств")
        except:
            print("Вы ввели не число, попробуйте еще раз")


if not os.path.exists("balance_log_tema6.txt"):
    with open("balance_log_tema6.txt", "w") : pass
egor = Account('Egor')
elena = Account('Elene',100)
egor.deposit_money()
elena.withdraw_money()
egor.withdraw_money()
elena.deposit_money()
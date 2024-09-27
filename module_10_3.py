import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            time.sleep(0.001)  # Имитация скорости выполнения пополнения
            self.balance += amount
            if self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {amount}. Баланс: {self.balance}")


    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")

            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()  # Блокируем поток
            time.sleep(0.001)  # Имитация скорости выполнения снятия

if __name__ == "__main__":
    bank = Bank()

    thread_deposit = threading.Thread(target=bank.deposit)
    thread_take = threading.Thread(target=bank.take)

    thread_deposit.start()
    thread_take.start()

    thread_deposit.join()
    thread_take.join()

    print(f"Итоговый баланс: {bank.balance}")
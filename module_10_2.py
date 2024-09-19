import threading
import time


class Knight(threading.Thread):
	def __init__(self, name, power):
		super().__init__()
		self.name = name
		self.power = power
		self.enemies = 100  # Изначально 100 врагов
		self.days = 0

	def run(self):
		print(f"{self.name}, на нас напали!")
		while self.enemies > 0:
			time.sleep(1)  # Пауза на 1 секунду, чтобы имитировать день битвы
			self.enemies -= self.power
			self.days += 1


			if self.enemies < 0:
				self.enemies = 0

			print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

		print(f"{self.name} одержал победу спустя {self.days} день(дня)!")



knight1 = Knight("Рыцарь Артур", 30)
knight2 = Knight("Рыцарь Ланселот", 20)

knight1.start()
knight2.start()

# Ожидаем завершения обоих потоков
knight1.join()
knight2.join()

print("Битвы окончены!")

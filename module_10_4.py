import random
import time
from queue import Queue
from threading import Thread


class Table:
	def __init__(self, number):
		self.number = number
		self.guest = None  # Гость за столом, по умолчанию None


class Guest(Thread):
	def __init__(self, name):
		super().__init__()
		self.name = name

	def run(self):
		time.sleep(random.randint(3, 10))


class Cafe:
	def __init__(self, *tables):
		self.queue = Queue()
		self.tables = tables

	def guest_arrival(self, *guests):
		for guest in guests:
			table = self.find_free_table()
			if table:
				table.guest = guest
				guest.start()
				print(f"{guest.name} сел(-а) за стол номер {table.number}")
			else:
				self.queue.put(guest)
				print(f"{guest.name} в очереди")

	def find_free_table(self):
		for table in self.tables:
			if table.guest is None:
				return table
		return None

	def discuss_guests(self):
		while not self.queue.empty() or any(table.guest for table in self.tables):
			for table in self.tables:
				if table.guest and not table.guest.is_alive():
					print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
					print(f"Стол номер {table.number} свободен")
					table.guest = None

				if table.guest is None and not self.queue.empty():
					guest_from_queue = self.queue.get()
					table.guest = guest_from_queue
					guest_from_queue.start()
					print(f"{guest_from_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

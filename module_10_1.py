import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

def time_it(func, *args):
    start_time = time()
    func(*args)
    end_time = time()
    return end_time - start_time

print("Запуск записи без потоков:")
times = []
times.append(time_it(write_words, 10, 'example1.txt'))
times.append(time_it(write_words, 30, 'example2.txt'))
times.append(time_it(write_words, 200, 'example3.txt'))
times.append(time_it(write_words, 100, 'example4.txt'))

for i, duration in enumerate(times):
    print(f"Время записи в example{i + 1}.txt: {duration:.2f} секунд")

print("\nЗапуск записи с потоками:")
threads = []
file_params = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt'),
]

for params in file_params:
    thread = threading.Thread(target=write_words, args=params)
    threads.append(thread)

start_time_threads = time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Общее время выполнения потоков: {end_time_threads - start_time_threads:.2f} секунд")


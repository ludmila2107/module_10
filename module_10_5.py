import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line.strip())
    return all_data


if __name__ == '__main__':
    filenames = [f'file_{number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f'{linear_time} (линейный)')

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f'{multiprocessing_time} (многопроцессный)')

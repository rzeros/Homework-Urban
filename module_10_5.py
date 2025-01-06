import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line.strip())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time1 = time.time()
for filename in filenames:
    read_info(filename)
end_time1 = time.time()
print(f"{end_time1 - start_time1} (линейный)")


if __name__ == '__main__':
    start_time2 = time.time()
    with Pool(4) as p:
        p.map(read_info, filenames)
    end_time2 = time.time()
    print(f"{end_time2 - start_time2} (многопроцессный)")
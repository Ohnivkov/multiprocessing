from multiprocessing import Pool,cpu_count
def all_dividers(number):
    list_dividers=[]
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            list_dividers.append(i)
    list_dividers.append(number)
    return list_dividers
def factorize(*numbers):
    with Pool(cpu_count()) as pool:
        mapped=pool.map(all_dividers,numbers)
    return mapped

if __name__ == '__main__':
    a, b, c, d = factorize(128, 255, 99999, 10651060)
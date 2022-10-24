from random import randint
from time import time
from statistics import mean

import task2.task2


def calcHist(mass: list) -> list:
    hist = [0] * 10
    for i in mass:
        hist[i // 100] += 1

    return hist


def main():
    # mass = [randint(0, 999) for i in range (0, 1000000)]
    # hist = calcHist(mass)  # Сохраним одну гистограмму
    # times = []
    # for i in range (0, 100):
    #     star_time = time()
    #     calcHist(mass)
    #     times.append(time() - star_time)
    #
    # print("Значения гистограммы от 0..99 до 900..999: " + str(hist))
    # print("Максимальное время: " + str(max(times)) + " секунд")
    # print("Минимальное время: " + str(min(times)) + " секунд")
    # print("Среднее время: " + str(mean(times)) + " секунд")

    mass1 = [randint(0, 999) for i in range(0, 1000000)]
    mass2 = [randint(0, 999) for i in range(0, 1000000)]

    hist1 = calcHist(mass1)
    hist2 = calcHist(mass2)

    print(hist1)
    print(hist2)
    print(task2.task2.histDistanve(hist1, hist2))

    task2.task2.saveHistToFile(hist1, 'SaveTest.txt')
    print(task2.task2.readHistFromFile('SaveTest.txt'))


if __name__ == "__main__":
    main()

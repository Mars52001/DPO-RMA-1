from random import randint
from time import time
from statistics import mean

import task2.task2
from task3.task3 import NNClassifier


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
    mass3 = [randint(0, 999) for i in range(0, 1000000)]
    mass_test = [randint(0, 999) for i in range(0, 1000000)]

    hist1 = calcHist(mass1)
    hist2 = calcHist(mass2)
    hist3 = calcHist(mass3)
    hist_test = calcHist(mass_test)


    task2.task2.saveHistToFile(hist1, 'hist1.txt')
    task2.task2.saveHistToFile(hist2, 'hist2.txt')
    task2.task2.saveHistToFile(hist3, 'hist3.txt')
    # print(task2.task2.readHistFromFile('SaveTest.txt'))

    clasifier = NNClassifier()
    clasifier.addHist('hist1.txt', 'Тип 1')
    clasifier.addHist('hist2.txt', 'Тип 2')
    clasifier.addHist('hist3.txt', 'Тип 3')
    print(clasifier.checkHistBelonging(hist_test))




if __name__ == "__main__":
    main()

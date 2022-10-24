from math import sqrt
import os

# Функция создания пирамиды
def triangle(a: int):
    rows = a + 1  # Число рядов
    for i in range(rows):
        row = '*' * (2 * i + 1)  # Текущий ряд
        print(row.center(2 * rows))


# Функция для вычисления декартова расстояния между гистограммами
# Для реализации используются гистограммы из первого задания
def histDistanve(hist1: list, hist2: list) -> float:
    sqr_sum = 0  # Сумма расстояний точек под корнем
    for i in range(len(hist1)):
        sqr_sum += (hist1[i] + hist2[i]) ** 2

    return (sqrt(sqr_sum))


# Функция созранения гистограммы в файл
def saveHistToFile(hist: list, file_path: str):
    hist = [str(h) for h in hist]  # Cписок (гистограмму) из int в список (гистограмму) из str

    file = open(file_path, 'w')
    # for h in hist:
    #     file.write(h)
    #     file.write(';')
    for i in range(len(hist)):
        file.write(hist[i])
        if i != len(hist) - 1:
            file.write(';')
    file.close()

# Функция чтения гистограммы из файл (строки будут конвертированы в числа)
def readHistFromFile(file_path: str) -> list:
    file = open(file_path, 'r')
    hist_str = file.readline()
    hist = hist_str.split(';')
    return [int(h) for h in hist]
    # return hist


def main():
    a = input()
    triangle(int(a))


if __name__ == "__main__":
    main()

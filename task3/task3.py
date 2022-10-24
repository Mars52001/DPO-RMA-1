from task2.task2 import histDistanve, readHistFromFile


class NNClassifier:
    ob_hists = {}

    # Функция добавления гистограмму (с типом объекта) в список из файла
    def addHist(self, filepath: str, hist_type: str):
        hist = readHistFromFile(filepath)
        self.ob_hists[hist_type] = hist

    # Функция определения принадлежности гистограммы к объек
    def checkHistBelonging(self, hist: list):
        hist_distances = {}
        for h in self.ob_hists:
            hist_distances[h] = histDistanve(hist, self.ob_hists[h])
        return min(hist_distances, key=hist_distances.get)

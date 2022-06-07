import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv("data.csv", sep=";")
a = data.shape[1]
arr = np.zeros((a, a), dtype="float32")
k = len(arr) // 2
_num = list(range(1, len(arr) + 1, 1))
numbers = [str(numeric_string) for numeric_string in _num]


def get_ind_of_min():
    b = arr[arr > 0]
    _min = b.min()
    for j in range(len(arr)):
        for i in range(j):
            if arr[i, j] == _min:
                return np.array([i, j])


def mix_columns(a):
    for i in range(len(arr)):
        if arr[i, a[1]] < arr[i, a[0]]:
            arr[i, a[0]] = arr[i, a[1]]
    for i in range(len(arr)):
        if arr[a[0], i] > arr[a[1], i]:
            arr[a[0], i] = arr[a[1], i]


def make_scatter(numbers):
    fig, ax = plt.subplots()
    colors = "bgrcmykw"
    color_index = 0
    ax.set_xlabel("Объем продаж")
    ax.set_ylabel("Среднегод. стоимость")
    mas = []
    for i in numbers:
        _a = [int(numeric_string) for numeric_string in i]
        x = data.iloc[0]
        y = data.iloc[1]
        x = x[str(min(_a)):str(max(_a)):1]
        y = y[str(min(_a)):str(max(_a)):1]
        ax.scatter(x, y, c=colors[color_index])
        color_index += 1
    plt.show()

for j in range(len(arr)):
    for i in range(len(arr)):
        arr[i][j] = np.round(math.sqrt(
            math.pow((data.iloc[0, i] - data.iloc[0, j]), 2) + math.pow((data.iloc[1, i] - data.iloc[1, j]), 2)), 2)
print(arr)
print("\n")
while len(arr) > k:
    ind = get_ind_of_min()
    print("min:")
    print(arr[ind[0], ind[1]])
    mix_columns(ind)
    arr = np.delete(arr, ind[1], 1)
    arr = np.delete(arr, ind[1], 0)
    print(arr)
    numbers[ind[0]] += numbers[ind[1]]
    numbers.pop(ind[1])
    print('\n')
numbers = numbers[:k]
print(numbers)
make_scatter(numbers)

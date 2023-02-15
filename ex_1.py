# Задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.
import matplotlib.pyplot as plt

list_x = []
list_y = []

for x in range(-10, 11):
    y = 5 * x * x + 10 * x - 30
    list_x.append(x)
    list_y.append(y)

plt.axhline(y=0, color='r', linestyle='solid')
plt.plot(list_y)
plt.show()

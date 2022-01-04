import matplotlib.pyplot as plt

# Grafik Bubble Sort vs. Selection Sort
x1 = [10, 100, 1000, 10000, 100000]
y1 = [112.5, 10102.5, 1001002.5, 100010002.5, 10000100002.5]

x2 = [10, 100, 1000, 10000, 100000]
y2 = [99.5, 9999.5, 999999.5, 99999999.5, 9999999999.5]

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (detik)")
plt.legend(["Bubble Sort", "Selection Sort"])

plt.show()
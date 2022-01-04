import matplotlib.pyplot as plt

# Grafik Bubble Sort vs. Selection Sort
x1 = [10, 20, 30, 40, 50]
y1 = [112.5, 422.5, 932.5, 1642.5, 2552.5]

x2 = [10, 20, 30, 40, 50]
y2 = [99.5, 399.5, 899.5, 1599.5, 2499.5]

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (detik)")
plt.legend(["Bubble Sort", "Selection Sort"])

plt.show()
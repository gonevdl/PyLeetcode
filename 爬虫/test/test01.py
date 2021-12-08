import matplotlib.pyplot as plt

input_values = [0, 1, 2, 3, 4]
data = [1, 2, 4, 8, 16]
plt.plot(input_values, data, linewidth=2)

# 设置图表标题，并加标签
plt.title("2的n次方", fontsize=18)
plt.xlabel("n", fontsize=14)
plt.ylabel("2^n", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=10)

# 显示图
plt.show()

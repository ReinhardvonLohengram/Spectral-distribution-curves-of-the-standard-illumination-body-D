import matplotlib.pyplot as plt
import numpy as np
from S0 import S0_array
from S1 import S1_array
from S2 import S2_array


def calculate( t, S0, S1, S2):
    if 4000 <= t <= 7000:
        x = -4.607 * pow(10, 9) / pow(t, 3) + 2.9678 * pow(10, 6) / pow(t, 2) + 0.09911 * pow(10, 3) / t + 0.244063

    elif 7000 <= t <= 25000:
        x = -2.0064 * pow(10, 9) / pow(t, 3) + 1.9018 * pow(10, 6) / pow(t, 2) + 0.24748 * pow(10, 3) / t + 0.23704

    y = -3 * x * x + 2.87 * x - 0.275
    M1 = (-1.3515 - 1.7703 * x + 5.9114 * y) / (0.0241 + 0.2562 * x - 0.7341 * y)
    M2 = (0.03 - 31.4424 * x + 30.0717 * y) / (0.0241 + 0.2562 * x - 0.7341 * y)
    S = S0 + M1 * S1 + M2 * S2
    return S

S0=np.asarray(S0_array)
S1 = np.asarray(S1_array)
S2 = np.asarray(S2_array)
S5000 = calculate(5503,S0, S1, S2)
S6500 = calculate(6504,S0, S1, S2)
S7500 = calculate(7504,S0, S1, S2)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig, ax = plt.subplots() # 创建图实例
x = np.arange(300, 840, 10)
ax.plot(x, S5000, label='5503k') # 作y1 = x 图，并标记此线名为linear
ax.plot(x, S6500, label='6504k') #作y2 = x^2 图，并标记此线名为quadratic
ax.plot(x, S7500, label='7504k') # 作y3 = x^3 图，并标记此线名为cubic
plt.xlabel('波长λ（nm）')  # 为x轴命名为“x”
plt.ylabel('相对辐射功率（W）')  # 为y轴命名为“y”
ax.legend()
plt.show()
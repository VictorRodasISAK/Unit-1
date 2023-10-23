import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 70)
participants = {
    'p1': [-1.15, 8.07, 3.58, 2.19, 3.69, 2.07, 11.08, -7.5, -1.85, -3.12, -18.23, -27.46, -22.15, -14.65, -10.5, -7.15,
           -4.62, 4.38, 2.07, -5.77, 3.34, -6.35, 0.57, -8.77, 8, -8.65, -1.5, 1.85, 1.62, 3.92, 101.23, 86, 86, 86.11,
           84, 67.38, 76.15, 67.27, 69.46, 60.23, 55.61, 62.77, 56.88, 64.27, 56.31, 49.04, 59.42, 53.08, 42.46, 41.65,
           22.85, 7.73, 10.96, 11.77, 4.154, 4.038, 6, 0.46, 7.38, 7.27, -38.54, -27.23, -25.73, -25.04, -19.85, -24,
           -32.08, -21.58, -12.12, -18.11]
}

y = participants['p1']
for i in [0]:
    plt.axhline(y=i, linestyle='solid', c='black')
for l in [5, 10, 30, 50, 60, 70]:
    plt.axvline(x=l, linestyle='--', c='black')

plt.text(-4, 103, '$BEFORE_Ov$', fontsize=8)
plt.text(5, 103, '$BEFORE_Un$', fontsize=8)
plt.text(15, 103, '$LEARN_{Ov-}$', fontsize=8)
plt.text(35, 103, '$LEARN_{Un+}$', fontsize=8)
plt.text(50, 103, '$AFTER_Ov$', fontsize=8)
plt.text(60, 103, '$AFTER_Un$', fontsize=8)

plt.title('Hirata Sensei, Over/Under, w/left and right goggles')
plt.xlabel('Amount of throws')
plt.ylabel('Horizontal Displacement (cm)')
plt.ylim([-110, 110])

plt.scatter(x, y)
plt.show()
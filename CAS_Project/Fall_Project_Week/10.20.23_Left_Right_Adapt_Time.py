import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 55)
participants = {
    'p2': [31.97, 6, -2.967, 0.21, 3.2, -21.67, -8.496, -4.713, -2.614, 0, -6.261, -6.378, -8.025, -9.32, -10.14, 1.875,
           -8.261, 2.563, -3.672, -10.97, 2.328, -12.03, -12.14, -14.14, -13.08, 113.39, 79.15, 75.5, 75.86, 74.2,
           45.45, 43.68, 47.45, 47.15, 48.86, 46.27, 44.5, 44.5, 41.86, 42.33, 43.74, 43.15, 37.74, 37.5, 41.86, -12.61,
           -14.85, -9.2, -3.2, -3.5, -3.261, -5.2, -3.6, 4.739, 5.975]
}

plt.rcParams['figure.dpi'] = 300
y = participants['p2']
for i in [0]:
    plt.axhline(y=i, linestyle='solid', c='black')
for l in [5, 25, 45, 55]:
    plt.axvline(x=l, linestyle='--', c='black')

plt.text(-2, 120, '$BEFORE_Ov$', fontsize=8)
plt.text(12, 120, '$LEARN_{Ov-}$', fontsize=8)
plt.text(33, 120, '$LEARN_{Ov+}$', fontsize=8)
plt.text(48, 120, '$AFTER_Ov$', fontsize=8)

plt.title('Dr. Ruben, Over, w/left and right goggles')
plt.xlabel('Amount of throws')
plt.ylabel('Horizontal Displacement (cm)')
plt.ylim([-130, 130])

plt.scatter(x, y)
plt.show()
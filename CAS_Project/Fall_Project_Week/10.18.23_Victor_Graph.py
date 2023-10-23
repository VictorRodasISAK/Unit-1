import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 85)
participants = {
    'p2': [11.14, -15.22, 26.21, 0.83, 2.84, -10.22, -13.91, 17.75, -13.1, -13.86, 6.16, -6.92, -36.77, 4.47, 6.02,
           12.16, 8.78, -23.57, -2.28, 4.12, -16.48, -11.26, -3.82, -13.73, 9.28, 0.9, -16.48, 20.53, -20.7, 3.09,
           -3.45, 14.73, 15.48, -5.3, 15.48, 85, 85, 85, 85, 85, 85, 61.41, 62.95, 64.39, 73.28, 44.5, 66.18, 74.63,
           75.56, 70.54, 71.76, 63.7, 57.13, 60.43, 59.62, 30.1, 56.46, 40.66, 39.32, 12.91, 21.44, 14.04, 19.74, 6.88,
           48.61, -3.68, -3.26, 2.74, -6.36, -0.93, -1.22, 2.75, 1.3, -10.23, -11.53, 9.82, 12.55, 0.24, -5.52, 13.46,
           1.39, 3.48, -7.39, 13.46, -17.15]
}

plt.rcParams['figure.dpi'] = 300
y = participants['p2']
for i in [0]:
    plt.axhline(y=i, linestyle='solid', c='black')
for l in [5, 35, 65, 85]:
    plt.axvline(x=l, linestyle='--', c='black')

plt.text(-5, 90, '$BEFORE_Ov$', fontsize=8)
plt.text(15, 90, '$LEARN_{Ov-}$', fontsize=8)
plt.text(45, 90, '$LEARN_{Ov+}$', fontsize=8)
plt.text(70, 90, '$AFTER_Ov$', fontsize=8)

plt.title('Victor, Over, w/left and right goggles')
plt.xlabel('Amount of throws')
plt.ylabel('Horizontal Displacement (cm)')
plt.ylim([-100, 100])

plt.scatter(x, y)
plt.show()

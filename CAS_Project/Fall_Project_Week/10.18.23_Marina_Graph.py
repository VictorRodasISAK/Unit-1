import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 85)
participants = {
    'p2': [20.75, 11.33, -9.71, -7.1, 7.87, 85, 34.7, 85, 69.45, 79.01, 72.09, 47.77, 85, 74.62, 68.56, 85, 85, 85, 85,
           74.76, 54.33, 70.24, 77.53, 85, 37.4, 67.16, 43.93, 52.58, 60.04, 54.77, 36.55, 62.76, 71.04, 45.77, 59.56,
           -85, -85, -85, -48.93, -85, -85, -66.33, -61.81, -58.22, -85, -31.73, -85, -66.12, -58.61, -85, -85, -30.5,
           -45.37, -19.83, -25.25, -38.85, -57.187, -49.39, -41.74, -85, -40.2, -20.66, -31.84, -29.57, -47.09, 30.78,
           16.89, 18.11, 3.98, 19.61, 19.06, 6.02, 15.16, 10.05, 2.88, 3.85, 4.66, 16.94, 6.08, 11.77, 18.09, 5.67,
           3.65, 12.98, -23.01]
}

y = participants['p2']
for i in [0]:
    plt.axhline(y=i, linestyle='solid', c='black')
for l in [5, 35, 65, 85]:
    plt.axvline(x=l, linestyle='--', c='black')

plt.text(-5, 90, '$BEFORE_Ov$', fontsize=8)
plt.text(15, 90, '$LEARN_{Ov+}$', fontsize=8)
plt.text(45, 90, '$LEARN_{Ov-}$', fontsize=8)
plt.text(70, 90, '$AFTER_Ov$', fontsize=8)

plt.title('Marina, Over, w/right and left goggles')
plt.xlabel('Amount of throws')
plt.ylabel('Horizontal Displacement (cm)')
plt.ylim([-100, 100])

plt.scatter(x, y)
plt.show()

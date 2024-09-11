import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.optimize import curve_fit

x = [1,
     0.9,
     0.8,
     0.6,
     0.5,
     0.4,
     0.2,
     0.1,
     0
     ]
y = [0,
     266.8538908,
     332.8994102,
     131.5897407,
     -11.89821864,
     -214.6925011,
     -704.8440979,
     -606.5646233,
     0
     ]

x = np.asarray(x)
y = np.asarray(y)

z, res, _, _, _ = np.polyfit(x=x, y=y, deg=8, full=True)

# z, V = np.polyfit(x, y, 6, cov=True)

f = np.poly1d(z)

print(f"The function is: {z}")
print(f"The residuals are: {res}")

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x, y, 'o', x_new, y_new)

plt.show()

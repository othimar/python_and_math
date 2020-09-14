import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = Symbol('x')
nb_periods = 3
x_end = nb_periods*np.pi
x_values = np.linspace(-x_end, x_end, 1000)
#calcul du sinus
y_values_sin = np.sin(x_values)

#calcul du sinus cardinal
y_values_sinc = np.sinc(x_values)

#calcul du sinus hyperbolique
x_values_sinh = np.linspace(-3,3, 1000)
y_values_sinh = np.sinh(x_values_sinh)

#calul du sinus integral
x_values_si = np.linspace(0,10)
y_values_si = np.empty(x_values_si.size)
for i in range(y_values_si.size):
    y_values_si[i] = N(Si(x_values_si[i]))

#tracé des fonctions
figure = plt.figure()
axes0 = figure.add_subplot('111')
axes0.spines['top'].set_visible(False)
axes0.spines['right'].set_visible(False)
axes0.spines['left'].set_position('zero')
axes0.spines['bottom'].set_position('zero')
axes0.xaxis.set_major_locator(plt.MultipleLocator(np.pi))

def format_func_x(value, pos):
    if pos == 0:
        return 'O'
    elif pos == 1:
        return 'I'
    else:
        lab_value = value/np.pi
        if lab_value == 1:
            return r'$\pi$'
        elif lab_value == -1:
            return r'$-\pi$'
        else:
            return r'${0}\pi$'.format(int(lab_value))

axes0.xaxis.set_major_formatter(plt.FuncFormatter(format_func_x))

axes0.plot(x_values, y_values_sin, label='Sinus')
axes0.plot(x_values, y_values_sinc, label='Sinus Cardinal')
axes0.plot(x_values_sinh, y_values_sinh, label='Sinus Hyperbolique')
axes0.plot(x_values_si, y_values_si, label='Sinus integral')
axes0.legend()
#plt.gca().set_aspect('equal',adjustable='box')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

#dT/dt = v(x,t)
#dv/dt = V^2/a^2[T(x+a,t)+T(x-a,t)-2T(x,t)]

#phi(x) = C x(L-x)/L^2 exp[- (x-d)^2/2s^2]

def phi(x, L, C, s):
    return C*((x*(L-x))/L**2)*np.exp((-1*(x-d)**2)/(2*s**2))


if __name__ == '__main__':
    V = 100 #m/s
    a = 0.01
    L = 1 #m
    d = 10 #cm
    C = 1 #m/s
    s = 0.3 #m
    h = 1e-6 #s
    t = 0


    X = np.arange()
    Y = np.zeros()
    update = Y.copy()

    iteration = 0

    for i in range(len(y)):
        iteration += 1
        part_1 = V**2 / a**2
        part_a = phi(X[1]+a, L, C, s, h)
        part_b = phi(X[1]-a, L, C, s, h)
        part_c = phi(X[1], L, C, s, h)

        update[1] = Y[1] + (part_1 * part_a + part_b - 2*part_c)
        t += h

    plt.plot(X, update)
    plt.draw()
    plt.show()



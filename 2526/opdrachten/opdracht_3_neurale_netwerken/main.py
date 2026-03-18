import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def excitation(x, I, alpha, theta, h):
    # thresholded saturating nonlinearity
    if x <= h:
        return 0.0
    return (I / theta) * (1.0 - np.exp(-alpha * theta * (x - h)))

def model(state, t, params):
    e1, e2 = state

    I1 = params["I1"]
    I2 = params["I2"]
    alpha1 = params["alpha1"]
    alpha2 = params["alpha2"]
    theta1 = params["theta1"]
    theta2 = params["theta2"]
    h1 = params["h1"]
    h2 = params["h2"]
    A1 = params["A1"]
    A2 = params["A2"]
    gamma1 = params["gamma1"]
    gamma2 = params["gamma2"]

    E1 = excitation(e1, I1, alpha1, theta1, h1)
    E2 = excitation(e2, I2, alpha2, theta2, h2)

    de1dt = A1 * E2 - gamma1 * e1
    de2dt = A2 * E1 - gamma2 * e2

    return [de1dt, de2dt]

params = {
    "I1": 1.0, "I2": 1.0,
    "alpha1": 1.0, "alpha2": 1.0,
    "theta1": 1.0, "theta2": 1.0,
    "h1": 0.2, "h2": 0.2,
    "A1": 1.2, "A2": 1.2,
    "gamma1": 0.8, "gamma2": 0.8,
}

t = np.linspace(0, 30, 1000)
x0 = [0.0, 0.5]

sol = odeint(model, x0, t, args=(params,))

plt.plot(t, sol[:, 0], label="e1")
plt.plot(t, sol[:, 1], label="e2")
plt.xlabel("time")
plt.ylabel("activation")
plt.legend()
plt.show()

## Problem Description

This project models the transient behavior of a series **LCR (Inductor-Capacitor-Resistor) circuit** connected to a direct current (DC) voltage source. Using Kirchhoff's Voltage Law (KVL), the voltage loop equation is written as:

$$L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = E$$

Where:
* $q(t)$ is the charge on the capacitor at time $t$
* $i(t) = \frac{dq}{dt}$ is the current through the circuit
* $E$ is the source electromotive force (EMF) ($1 \text{ V}$)
* $L$ is the inductance ($1 \text{ H}$)
* $C$ is the capacitance ($1 \text{ F}$)
* $R$ is the circuit resistance ($\Omega$)

### Numerical Approach (RK4 Method)

To solve this second-order system numerically, it is converted into a system of two coupled first-order Ordinary Differential Equations (ODEs):

1.  $$\frac{dq}{dt} = i$$
2.  $$\frac{di}{dt} = \frac{E - \frac{q}{C} - Ri}{L}$$

The system is evaluated over $t \in [0, 20]$ seconds using a custom **4th-order Runge-Kutta (RK4)** integration loop.

### Damping Cases Evaluated

The code dynamically calculates the critical damping resistance value using the formula:
$$R_c = 2\sqrt{\frac{L}{C}}$$

It then simulates and plots three standard physical conditions to demonstrate how resistance alters the system's return to equilibrium:
* **Overdamped ($R > R_c$):** The charge approaches the steady-state slowly without any oscillations.
* **Critically Damped ($R = R_c$):** The charge approaches the steady-state as rapidly as possible without oscillating.
* **Underdamped ($R < R_c$):** The charge oscillates back and forth around the steady-state value with decreasing amplitude.

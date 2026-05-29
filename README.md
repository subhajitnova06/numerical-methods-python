# Numerical Physics Simulations using RK4

This repository contains Python implementations of numerical simulations for classical physical systems. It leverages the **4th-order Runge-Kutta (RK4)** numerical method to solve the non-linear and linear Ordinary Differential Equations (ODEs) governing these systems.

## 📌 Repository Overview

The repository is structured into two primary simulation projects:

| Project Folder / File | System Type | Mathematical Nature | Physical Phenomenon |
| :--- | :--- | :--- | :--- |
| `01_Simple_Pendulum/` | Mechanical | Non-linear Second-Order ODE | Angular displacement & Period lengthening |
| `02_LCR_Circuit/` | Electrical | Linear Second-Order ODE | Damping states (Over, Critical, Under) |

---

## 🛠️ Mathematical Framework: The RK4 Method

Both simulations break down their respective second-order differential equations into a coupled system of two first-order ODEs:

$$\frac{dx}{dt} = f_1(t, x, y), \quad \frac{dy}{dt} = f_2(t, x, y)$$

The **Runge-Kutta 4th-order algorithm** approximates the next step by calculating a weighted average of four incremental slopes ($k_1, k_2, k_3, k_4$), achieving a local truncation error of $O(h^5)$.

---

## 📂 Project Modules

### 1. Simple Pendulum Simulation
Models the chaotic-capable, non-linear dynamics of a rigid simple pendulum of length $L=1\text{ m}$ under gravity ($g=9.8\text{ m/s}^2$). 

* **Governing Equation:** $$\frac{d^2\theta}{dt^2} + \frac{g}{L}\sin(\theta) = 0$$
* **Key Insight:** Demonstrates how the small-angle approximation ($\sin(\theta) \approx \theta$) fails at larger initial displacements ($\theta_0 = 2.5\text{ rad}$), resulting in a visibly longer oscillation period.

### 2. Series LCR Circuit Transient Response
Models the transient charging response of an Inductor ($L$), Capacitor ($C$), and Resistor ($R$) network connected to a constant DC voltage source ($E=1\text{ V}$).

* **Governing Equation:** $$L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = E$$
* **Key Insight:** Evaluates the system across three boundary states calculated from the critical damping resistance ($R_c = 2\sqrt{L/C}$):
    * **Overdamped ($1.5 \cdot R_c$):** Slow, non-oscillatory approach to steady-state.
    * **Critically Damped ($R_c$):** Fastest possible approach to equilibrium without overshoot.
    * **Underdamped ($0.5 \cdot R_c$):** Decaying oscillations around the final charge state ($q = E \cdot C$).

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3 installed along with the required scientific computing libraries:
```bash
pip install numpy matplotlib

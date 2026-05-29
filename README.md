# numerical-methods-python
Python implementations of interpolation, integration, differential equation solvers, and linear algebra methods.

# Simple Pendulum Simulation using RK4 Method

This repository contains a Python implementation that numerically solves the non-linear equations of motion for a simple pendulum. It utilizes the **4th-order Runge-Kutta (RK4)** mathematical framework to simulate how the pendulum's angle changes over time.

## Mathematical Overview

The motion of a simple pendulum is described by the following second-order non-linear ordinary differential equation (ODE):

$$\frac{d^2\theta}{dt^2} + \frac{g}{L}\sin(\theta) = 0$$

Where:
* $\theta$: Angular displacement (radians)
* $g$: Acceleration due to gravity ($9.8 \text{ m/s}^2$)
* $L$: Length of the pendulum ($1 \text{ m}$)

To solve this numerically, the second-order ODE is broken down into a system of two coupled first-order ODEs:

1.  $\frac{d\theta}{dt} = \omega$
2.  $\frac{d\omega}{dt} = -\frac{g}{L}\sin(\theta)$

The **RK4 method** is then applied to iteratively compute the values of $\theta$ and $\omega$ across a discrete time domain.

## Features

* **Custom RK4 Solver:** A pure Python implementation of the Runge-Kutta 4th-order algorithm.
* **Non-linear Dynamics:** Handles large initial angles where the small-angle approximation ($\sin(\theta) \approx \theta$) breaks down.
* **Multi-case Comparison:** Simulates and compares three different initial angular displacements ($\theta_0 = 0.1, 1.0,$ and $2.5$ radians).

## Dependencies

Make sure you have the following Python packages installed:

```bash
pip install numpy matplotlib

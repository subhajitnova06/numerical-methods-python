import numpy as np
import matplotlib.pyplot as plt
E,C = 1,1
L=1
n=1000
def f1(t,q,i):
    return i
def f2(t,q,i,R):
    return (E-q/C -R*i)/L
h=(20-0)/1000
T=np.linspace(0,20,1000)
def Rk(R):
    q_arr=[0]
    i_arr=[0]
    for _ in range(n-1):
        q=q_arr[_]
        i=i_arr[_]
        t=T[_]
        
        k1=h*f1(t,q,i)
        l1=h*f2(t,q,i,R)
        
        k2=h*f1(t+h/2,q+k1/2,i+l1/2)
        l2=h*f2(t+h/2,q+k1/2,i+l1/2,R)
        
        k3=h*f1(t+h/2,q+k2/2,i+l2/2)
        l3=h*f2(t+h/2,q+k2/2,i+l2/2,R)
        
        k4=h*f1(t+h,q+k3,i+l3)
        l4=h*f2(t+h,q+k3,i+l3,R)
        
        k_f=(k1+2*k2+2*k3+k4)/6
        i_f=(l1+2*l2+2*l3+l4)/6
        q_arr.append(q+k_f)
        i_arr.append(i+i_f)
        
    return q_arr,i_arr
m=2*np.sqrt(L/C)
R_values=[1.5*m,m,0.5*m]

for j in range(3) :
    q, i = Rk(R_values[j]) 
    plt.plot(T,q) 
    
plt.title("Transient Response of a Series LCR Circuit (RK4 Simulation)", fontsize=14, fontweight='bold')
plt.xlabel("Time (seconds)", fontsize=12)
plt.ylabel("Capacitor Charge q(t) (Coulombs)", fontsize=12)
plt.axhline(y=E*C, color='r', linestyle=':', label='Steady State (q = E*C)') # Reference line for final charge
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc="lower right", fontsize=11)

plt.tight_layout()
plt.show()

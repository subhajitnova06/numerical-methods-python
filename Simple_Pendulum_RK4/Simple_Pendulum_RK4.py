
import numpy as np
import matplotlib.pyplot as plt

g,L=9.8,1
a,b=0,10
n=1000

def f1(t,th,w):
    return w
def f2(t,th,w):
    return (-g/L)*(np.sin(th))
T=np.linspace(a,b,n)
h=(b-a)/n

def Rk(t0):
    W=[0]
    theta=[t0]
    for _ in range(n-1):
        t=T[_]
        w=W[_]
        th=theta[_]
        k1=h*f1(t,th,w)
        l1=h*f2(t,th,w)
        
        k2=h*f1(t+h/2,th+k1/2,w+l1/2)
        l2=h*f2(t+h/2,th+k1/2,w+l1/2)
        
        k3=h*f1(t+h/2,th+k2/2,w+l2/2)
        l3=h*f2(t+h/2,th+k2/2,w+l2/2)
        
        k4=h*f1(t+h,th+k3,w+l3)
        l4=h*f2(t+h,th+k3,w+l3)
        
        k_f= (k1+2*k2+2*k3+k4)/6
        l_f= (l1+2*l2+2*l3+l4)/6
        
        theta.append(th+k_f)
        W.append(w+l_f)
        
    return theta,W         
m=[0.1,1,2.5]
for j in range(3):
    th_eff,w_eff=Rk(m[j])
    plt.plot(T,th_eff)

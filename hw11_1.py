import numpy as np
import matplotlib.pyplot as plt
import numba

#phi=-(rho/E0)
#(%(x+a,y)+%(x-a,y)+%(x,y-a)+%(x,y-a)-y%(x,y))/a^2
#1/%[*]+a^2/%E0

#E0 = 1
#Rho charge density

#def poisson(Rho=None, E0=None):
#    return phi=-Rho/E0
    
#def relax():

#def gauss():
    
def iterate(phi):
    phiprime = np.zeros(phi.shape)
    for i in range(gridsize+1):
        for j in range(gridsize+1):
            if i==0 or i==gridsize or j==0 or j==gridsize:
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = 0.25*(phi[i+1, j] +
                                      phi[i-1, j] +
                                      phi[i, j+1] +
                                      phi[i, j-1])
    return phiprime

if __name__ == '__main__':
    E0 = 1
  
    gridsize = 100 #nxn grid across box
    target = 1e-6 #target accuracy, in volts
    V = 1 #voltage at top of box
    L = 1 #m
    a = gridsize/L
    #boundary condition
    phi = np.zeros((gridsize+1, gridsize+1))
    phi[20:40,60:80] = 1
    phi[60:80,20:40] = -1
    phiprime = np.zeros(phi.shape)

    max_diff = 1.0
    iteration = 0
    while max_diff > target:
        #calculate new values of potential
        phiprime = iterate(phi)
        ##loop over grid x and y points
        #for i in range(gridsize+1):
        #    for j in range(gridsize+1):
        #        #if at boundary, do nothing
        #        if i==0 or i==gridsize or j==0 or j==gridsize:
        #            phiprime[i,j] = phi[i,j]
        #        #otherwise apply Laplacian operator
        #        else:
        #            phiprime[i,j] = 0.25*(phi[i+1, j] +
        #                                  phi[i-1, j] +
        #                                  phi[i, j+1] +
        #                                  phi[i, j-1])
        max_diff = np.max(abs(phi-phiprime))
        phi, phiprime = phiprime, phi
        #print(iteration, max_diff)
        #iteration=iteration+1
    plt.xlim(0,100)
    plt.imshow(phi)
    plt.show()

#Zeros[(XS > 5) & (XS < 10)]=1

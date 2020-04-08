import numpy as np
import matplotlib.pyplot as plt



def unit_ball():
    dim= 100      
    N = 200                                              #空间维度
    norm= np.random.normal
    U = norm(size=(dim, N))                                   #随机生成d维空间中的N个坐标点
    dev= np.sqrt(np.sum(U**2, axis=0))
    radius= np.power(np.random.random(size=(1, N)), 1/dim)    #对N个坐标点分别随机生成一个半径
    X = np.multiply(radius, U)/dev
    return X


def Cube_dis(A):
    '''calculate the distance between each point'''
    Dis = np.zeros((200,200))
    D = 0
    for i in range(0,200):
        for k in range(0,200):
            sum = 0
            for j in range(0,100):
                D = A[j:j+1,i:i+1]-A[j:j+1,k:k+1]
                D = D**2
                sum = sum + D
                Dis[i][k]= sum

    B = np.tril(Dis)
    Distance = np.sqrt(B)
    Distance = Distance[np.nonzero(Distance)]   
    return Distance

def Cube_angle(A):
    
    Dot = Vector_dot(A)
    Norm = Vector_length(A)
    Cosine = Dot/Norm
    Cosine = np.tril(Cosine)
    theta = np.arccos(Cosine)
    theta = theta[np.nonzero(theta)]
    return theta
    

    
def Vector_length(A):
    L = np.zeros((1,200))
    
    for i in range(0,200):
        sum = 0
        for j in range(0,100):
            sum = sum + A[j,i]**2
            L[0][i] = sum
    
    L = np.sqrt(L)
    L = np.dot(np.transpose(L),L)
    L = np.tril(L)
    return L


def Vector_dot(A):
    Dot = np.zeros((200,200))
    for i in range(0,200):
        for j in range (0,200):
            M = np.dot(np.transpose(A[:,j:j+1]),A[:,i:i+1])
            Dot[i][j] = M
    
    Dot = np.tril(Dot)
    return Dot
    
    
A = unit_ball()
# A = np.random.uniform(-0.5,0.5, size = (100,200))    

theta = Cube_dis(A)
plt.xlabel('Distance')
plt.ylabel('Number of points')
# plt.xlim(1, 2)
plt.grid(True)
plt.hist(theta, bins = 60)
plt.savefig('Distance_Ball_3D.png') 
plt.show
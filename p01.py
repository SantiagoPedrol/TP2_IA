import numpy as np
import math as m

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def escalonada(x):
    return np.where(x >= 0, 1, 0)

def foward_primer_capa(x):
    #1b     W = np.array([[-1, 0], [0, -1], [1, 1]])  # 3x2
    #1b     b = np.array([[0.5], [0.5], [-4.25]])  # 3x1

    W = np.random.rand(3, 2)
    
    b = np.random.rand(3, 1)

    # print(W.shape, b.shape)
    Z = W.dot(x) + b  # 3x1
    # print(Z)
    A = sigmoide(Z)

    #1b     A = escalonada(Z)  # 3x1
    # print(A)
    return A


def foward_segunda_capa(A1):
    #1b     W = np.array([1, 1, 4.25])  # 1x3
    #1b     b = np.array([-1])  # 1x1

    W = np.random.rand(1, 3)

    b = np.random.rand(1, 1)

    # print(W.shape, b.shape)
    Z = W.dot(A1) + b  # 1x1

    A = sigmoide(Z)
    #1b A = escalonada(Z)  # 1x1

    print(A)
    # print(Z.shape, A.shape)
    return A


# test
x = np.array([2.5, 3.25]).reshape(2,1)  # 2x1

A1 = foward_primer_capa(x)
A2 = foward_segunda_capa(A1)

# W = np.random.rand(3, 2)
    
# b = np.random.rand(3, 1)

# print(W, b)
# print(W.shape, b.shape)
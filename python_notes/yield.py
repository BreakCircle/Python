def triangles():
    L = [1]
    while True:
        yield L
        L1 = [0] + L[:]
        L = [L[i]+L1[i] for i in range(len(L))] + [1]
triangles()

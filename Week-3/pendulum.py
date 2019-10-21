import math
def period(L,g):
    try:
        float(L)
    except:
        print('new value of L')
    try:
        float(g)
    except:
        print('new value of g')
    try:
        float(1/g)
    except:
        print('g should not be 0')
    T = 2*math.pi * math.sqrt(L/g)
    return(T)
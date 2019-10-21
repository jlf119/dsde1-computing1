import math
def period(L,g):
    x = isinstance(L,(float,int))
    y = isinstance(g,(float,int))
    if x == False:
       raise(TypeError)
    elif y == False:
        raise(TypeError)
    elif g == 0:
        raise(ValueError)
    else: 
        T = 2*math.pi * math.sqrt(L/g)
        return(T)
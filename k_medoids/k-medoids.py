import numpy as np
from sklearn.metrics.pairwise import manhattan_distances as dist




def int_medoids(x,k):
    a=[]
    for j in range(k):
        r1=np.random.choice(range(1,len(x)))
        m=x[(r1),:]
        a.append(m)
    int_mediods=np.array(a)   
    return int_mediods

def K_medoids_min_cost(x,k,iteration):
    a=[]
    b=[]
    c=[]
    for i in range(iteration):
        medoids=int_medoids(x,k)
        d=dist(x,medoids)
        a.append(d)
        target_class=d.argmin(axis=1)
        b.append(target_class)
        iteration_cost=sum(d.min(axis=1))
        c.append(iteration_cost)
    return a,b,c

def K_Medoids(x,k,iteration):
    medoids=int_medoids(x,k)
    a,b,c=K_medoids_min_cost(x,k,iteration)
    c=np.array(c)
    return {'Iteration no' :c.argmin() ,
           'Iteration cost': c[c.argmin()],
           'Target' :b[c.argmin()],'distance':a[c.argmin()],'min_distance':a[c.argmin()].min(axis=1)}

import numpy
N,M= map(int,input().split())
A=[]
for i in range(N):
    A.append(list(map(int,input().split(' ',M-1))))

print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(round(numpy.std(A,axis=None),11))
    

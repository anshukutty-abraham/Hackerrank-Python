import re
T=int(input())
if T>0 and T<10:
    X=[]
    for i in range(T):
        N=input()
        try:
            if bool(re.search(".[0-9]+",N)):#to handle integers/no decimal value e.g. 0,12.
                X.append(isinstance(float(N),float))#check if convertible to float--handles signed and unsigned numbers
            else:#to handle strings
                X.append("False")
        except:#to handle float conversion errors
            X.append("False")
    for j in X:
        print(j)

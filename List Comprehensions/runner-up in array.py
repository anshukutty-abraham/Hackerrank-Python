if __name__ == '__main__':
    n = int(input())
    A = list(set(map(int, input().split(' ',n))))
    
    print(sorted(A)[-2])
    
    #A.sort(reverse=True)
    #print(A[1])
    
    #A.sort(reverse=True)
    #A.remove(max(A))
    #print(A[0])

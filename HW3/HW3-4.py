m=[[1,2,3],[7,6,8],[11,10,5]]

def getEntry(a):
    m=3
    n=3
    for i in range(m):
        for j in range(n):
            
            flag=1
            for k in range(m):
                if(k==i):
                    continue
                if(a[k][j]>a[i][j]):
                    flag=0
                    break
            for k in range(n):
                if(k==j):
                    continue
                if(a[i][k]<a[i][j]):
                    flag=0
                    break
            if(flag==1):
                return True
    return False
            

print(getEntry(m))
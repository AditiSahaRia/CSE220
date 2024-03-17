#Aditi Saha Ria
#ID: 20101238
#Task_07

A = list()
def F(n):
    if (n==0 or n==1):
        return 1
    else:
        return F(n-1)+F(n-2)
def FM(n):
    if(A[n] > 0):
        return A[n]
    if(n == 0 or n==1):
        return 1
    else:
        return A[n].append(FM(n-1)+FM(n-2))
def CalcFib(n):
    A.insert(0,0)
    A.insert(1,1)
    if n>1:
        for i in range(2,n+1):
            A.insert(i,A[i-1]+A[i-2])

a = 8
CalcFib(a)
print(FM(a))
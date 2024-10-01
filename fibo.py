
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    


def fibdynamic(n,iguais=[]):
    if n == 1 or n == 0:
        return n
    
    if iguais[n] == None:
        iguais[n] = fibdynamic(n - 1, iguais) + fibdynamic(n - 2, iguais)
    return iguais[n]



def fib2(n):
    iguais = [None] * (n + 1)
    return fibdynamic(n, iguais)





print(fib2(6))
        

def fibonachi(n):
    if (n == 1) or (n==2):
        return 1
    else:
        return fibonachi(n-1)
    
def fibo_memorization(n):
    g
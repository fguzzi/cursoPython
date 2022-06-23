def fatorial(num, b):
    res = 1
    if b != True:
        for c in range(1, num + 1):
           res = res * c
        print(res)
    if b == True:
        for c in range(1, num + 1):
            res = res * c
            print(res)



fatorial(5, True)

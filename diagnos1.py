def diagnos(n):
    lista= list(range(2,n+1))
    for x in lista:
        if x>0:
            for i in range(2*x,n+1,x):
                lista[i-2]=0
    for nummer in lista:
        if nummer > 0:
            print(nummer)
n=int(input("skriv in ett nummer mellan 2 och 99: "))
diagnos(n)
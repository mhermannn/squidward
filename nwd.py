def nwd(x,y):
    wynik = 0
    if x >y:
        w = x
        m = y
    else:
        w = y
        m = x
    for i in range(2,m):
        if m%i==0 and w%i==0:
            wynik = i
    return wynik
print(nwd(12,18))

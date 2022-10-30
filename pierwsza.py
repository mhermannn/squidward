def czyPierwsza(x):
    licznik = 0
    for i in range(2,x):
        if x%i==0:
            licznik += 1
    if licznik != 0:
        return("nie jest pierwsza")
    else:
        return("jest pierwsza")

print(czyPierwsza(7))

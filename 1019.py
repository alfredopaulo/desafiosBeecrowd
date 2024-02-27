N = int(input(""))

horas = 0
minutos = 0
segundos  = 0

while N > 0:
    if N >= 3600:
        N -=3600
        horas+=1
    if N <= 3600 and N>=60:
        N -=60
        minutos+=1
    else:
        N-=1
        segundos+=1
print(f"{horas}:{minutos}:{segundos}")
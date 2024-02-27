n = int(input(""))
cedulas = [100, 50 , 20, 10, 5, 2, 1]
aux = n

print(n)
for i in cedulas:
    notas = 0
    while aux >= i:
        notas+=1
        aux-=i
    print(f"{notas} nota(s) de R$ {i},00") 




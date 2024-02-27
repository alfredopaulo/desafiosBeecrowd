valor = float(input(""))

notas = [100,50,20,10,5,2]
moedas = [1.0,0.5,0.25,0.10,0.05,0.01]


def calcular(lista , msg, valor, titulo):
    aux = valor
    notas = 0
    print(f"{titulo}:")
    for i in lista:
        notas = 0 
        while aux >= i:
            notas+=1
            aux-=i
        print(f"{notas} {msg}(s) de R$ {i}{(lista[1]>1) ? ".00" : }")
    return aux


(x % 2 == 0) ? "par" : "impar"

valor = calcular(notas,"nota",valor,"NOTAS")
calcular(moedas,"moeda", valor, "MOEDAS")

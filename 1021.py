valor = float(input(""))

notas = [100,50,20,10,5,2]
moedas = [1.0,0.50,0.25,0.10,0.05,0.01]

def calcular(lista , msg, valor, titulo):
    aux = valor
    qnotas = 0
    print(f"{titulo}:")
    for i in lista:
        qnotas = 0 
        while round(aux,2) >= i:
            qnotas+=1
            aux-=i
        print(f"{qnotas} {msg}(s) de R$ {i}.00") if lista[1]>1 else print(f"{qnotas} {msg}(s) de R$ {i:.2f}")
    return aux

valor = calcular(notas,"nota",valor,"NOTAS")
calcular(moedas,"moeda", round(valor,2), "MOEDAS")

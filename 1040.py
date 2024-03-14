N1, N2,N3,N4 = [float(x) for x in input().split(' ')]

#2 3 4 1 

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + N4)/10

print(f"Media: {media}")
if(media>= 7.0):
    print("Aluno aprovado.")
if(media<5):
    print("Aluno reprovado.")
if(media>= 5.0 and media <= 6.9):
    print("Aluno em exame.")
    notaExame = float(input(""))
    media = (media + notaExame)/2
    print(f"Nota do exame: {notaExame}")
    if(media>=5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")






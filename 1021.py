A, B, C = [float(x) for x in input().split(' ')]
pi = 3.14159

areaTriangulo = (A * C)/2
areaCirculo = (C ** 2) * pi
areaTrapezio = ((A + B) * C)/2
areaQuadrado = B ** 2
areaRetangulo = A * B

print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO: {areaCirculo:.3f}")
print(f"TRAPEZIO: {areaTrapezio:.3f}")
print(f"QUADRADO: {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")


from math import sqrt

A, B ,C = [float(x) for x in input().split(' ')]

delta = (B * B) - (4 * A * C)

try:
    X1 = (-B + sqrt(delta))/(2 * A)
    X2 = (-B - sqrt(delta))/(2 * A)
    print(f"R1 = {X1:.5f}")
    print(f"R2 = {X2:.5f}")
except:
    print("Impossivel calcular")




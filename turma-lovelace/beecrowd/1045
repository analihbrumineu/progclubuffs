import math

Lado = list(map(float, input().split()))
Lado.sort(reverse=True)

A, B, C = Lado

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if math.pow(A, 2) == math.pow(B, 2) + math.pow(C, 2):
        print("TRIANGULO RETANGULO")
    elif math.pow(A, 2) > math.pow(B, 2) + math.pow(C, 2):
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")

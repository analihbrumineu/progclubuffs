dados = input().split()
N = int(dados[0])
R = int(dados[1])

if 10 <= N:
    ir = R
    print(R)
else:
    ir = 100 * (10 - N)
    ir = ir + R
    print(ir)
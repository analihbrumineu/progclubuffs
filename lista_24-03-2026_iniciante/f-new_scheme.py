dados = list(map(int, input().split()))

verif = True

for i in range(len(dados)):
    if i < len(dados) - 1:
        if dados[i] > dados[i + 1]:
            verif = False
            break
    if not(100 <= dados[i] <= 675):
        verif = False
        break
    if dados[i] % 25 != 0:
        verif = False
        break

if verif:
    print('Yes')
else:
    print('No')
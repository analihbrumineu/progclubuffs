while True:
    linha = list(map(int, input().split()))
    a, b = linha
    if a == b:
        break
    else:
        if a > b:
            print('Decrescente')
        else:
            print('Crescente')

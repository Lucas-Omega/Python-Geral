achou = False
for i in range(1000, 100000):
    if achou:
        print("o primeiro numero primo entre 1000 e 100000 e {}".format(i - 1))
        break
    div = 0
    for j in range(2,i+1):
        if(i%j == 0):
            div = div + 1
        if (div > 1):
            break
    if div == 1:
        achou = True

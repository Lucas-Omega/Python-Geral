quatidade = int(input("quantos alunos voce tem na sala: "))

for i in range(quatidade):
    n1 = int(input("digite a primeira nota: "))
    n2 = int(input("digite a segunda nota: "))

    m = (n1 + n2) / 2

    print("a media do aluno {} e = {}".format(i, m))
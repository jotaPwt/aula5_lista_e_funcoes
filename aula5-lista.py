notas = []

n1 = float(input('>>'))
n2 = float(input('>>'))
n3 = float(input('>>'))

notas.append(n1)
notas.append(n2)
notas.append(n3)

print(notas)

media = sum(notas)// len(notas)

print('A média do aluno é', media)


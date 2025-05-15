p1 = input('palavra 1: ')
p2 = input('palavra 2: ')

if len(p1) > len(p2):
    print(p1)
elif len(p1) == len(p2):
    print("São iguais de tamanho")
else:
    print(p2)
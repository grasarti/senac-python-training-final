# expressões regulares

import re
import random


print(re.search("[A-Z]","Senha"))
print(re.search("[A-Z]","seNha"))
print(re.search("[a-z]","senha"))
print(re.search("[0-9]","Senh1a"))

numero_secreto = random.randint(1,200)
print(numero_secreto)
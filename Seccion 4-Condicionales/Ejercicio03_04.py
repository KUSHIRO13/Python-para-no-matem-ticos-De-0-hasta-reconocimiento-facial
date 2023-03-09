#nombres
name1 = input("Nombre 1: ")
name2 = input("Nombre 1: ")

name1 = name1.lower()
name2 = name2.lower()

if name1[0] == name2[0] and name1[-1] == name2[-1]:
    print("Ambos empiezan y terminan igual")
elif name1[0] == name2[0]:
    print("Ambos empiezan igual")
elif name1[-1] == name2[-1]:
    print("Ambos terminan igual")
else:
    print("No empiezan ni terminan igual")
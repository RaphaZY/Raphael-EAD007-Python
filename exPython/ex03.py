n = int(input("Digite um número: "))
print("Tabuada do",n)
for ix in range(0,11,1):
    r = ix * n
    print(n,"x",ix,"=",r)
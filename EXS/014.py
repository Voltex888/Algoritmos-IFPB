n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 == n2 == n3:
    print("Todos os números são iguais")
elif n1 > n2 and n1 == n3:
    print("Existe dois valores iguais")
elif n1 > n3 and n1 == n2:
    print("Existe dois valores iguais")
elif n2 > n1 and n2 == n3:
    print("Existe dois valores iguais")
elif n2 > n3 and n2 == n1:
    print("Existe dois valores iguais")
elif n3 > n1 and n3 == n2:
    print("Existe dois valores iguais")
elif n3 > n2 and n3 == n1:
    print("Existe dois valores iguais")
elif n1 == n2 < n3:
    print(f"O maior é {n3}")
elif n2 == n3 < n1:
    print(f"O maior é {n1}")
elif n1 == n3 < n2:
    print(f"O maior é {n2}")
elif n1 > n2 and n1 > n3:
    print(f"O maior é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior é {n2}")
elif n3 > n2 and n3 > n1:
    print(f"O maior é {n3}")
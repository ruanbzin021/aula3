int1 = int(input("Informe um numero inteiro: "))

int2 = int(input("Informe outro numero inteiro: "))

int3 = int(input("Informe um numero inteiro: "))

if int1 > int2 and int1 > int3:
    print(f"{int1} é maior")

elif int2 > int1 and int2 > int3:
    print(f"{int2} é maior")    

elif int3 > int1 and int3 > int2:
    print(f"{int3} é maior")

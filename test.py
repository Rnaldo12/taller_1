import random

vocales = ['a', 'e', 'i', 'o', 'u']
palabra = input('Ingrese una palabra: ')
cont = sum(1 for letra in palabra if letra in vocales)
print(cont, "Vocales ")
print("Vocales", " ".join([letra for letra in palabra if letra in vocales]))





numeros = [random.randint(1, 10) for _ in range(10)]
print("Número | Cuadrado | Cubo")
for num in numeros:
    print(f"{num:^6}  {num**2:^8}  {num**3:^4}")
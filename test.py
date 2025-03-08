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


def eliminar_multiples_n(listaabecedario, n):
    return [letra for i, letra in enumerate(listaabecedario) if (i + 1) % n != 0]
listaabecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
print(listaabecedario)
n = int(input("Introduce el valor de n: "))
resultado = eliminar_multiples_n(listaabecedario, n)
print("Lista resultante:", resultado)

frase = "El mejor regalo? El perdón..."
list_frase = list(frase)
print(frase)
print(list_frase) #deben jugar con esta lista
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(9)
list_frase.pop(16)
list_frase.pop(16)
list_frase.pop(15)


nueva_frase = ''.join(list_frase)
print(list_frase)
print(nueva_frase)


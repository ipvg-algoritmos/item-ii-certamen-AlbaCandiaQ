# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código
palabra_usuario = str(input("Ingrese una palabra: "))
def es_palindromo(palabra) :
    palabra_minuscula = palabra.lower()
    palabra_sin_espacios = palabra_minuscula.replace(" ", "")
    palabra_reverso = palabra_sin_espacios [::-1]
    return palabra_sin_espacios == palabra_reverso
if es_palindromo(palabra_usuario) :
    print(f"{palabra_usuario} es un palindromo")
else :
    print(f"{palabra_usuario} no es un palindromo")


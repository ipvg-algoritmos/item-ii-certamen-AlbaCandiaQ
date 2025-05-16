# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
cantidad_notas = int(input("Cuantas notas ingresará?"))
notas = []
for i in range (cantidad_notas) :
    nota = float(input(f"Ingrese la nota {i +1}: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
promedio_redondeado = round(promedio, 2)
print("Notas ingresadas: ", notas)
print("El promedio es: ", promedio_redondeado)
if promedio_redondeado >= 4.0:
    print("Suficiente para aprobar")
else:
    print("No suficiente para aprobar")
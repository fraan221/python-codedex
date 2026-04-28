# EJERCICIOS

## if-else Ternario

### Ejercicio 1: Determinar el mayor de dos números ✅

Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales

### Ejercicio 2: Calculadora simple ✅

Pide al usuario dos números y una operación (+, -, \*, /) Realiza la operación y muestra el resultado (maneja la división entre zero)

### Ejercicio 3: Año bisiesto ✅

Pide al usuario que introduzca un año y determina si es bisiesto. Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

### Ejercicio 4: Categorizar edades ✅

Pide al usuario que introduzca una edad y la clasifique en:

- Bebé (0-2 años)
- Niño (3-12 años)
- Adolescente (13-17 años)
- Adulto (18-64 años)
- Adulto mayor (65 años o más)

# Regex

**01_re.py**

1. **Ejercicio 1** — Encontrá la primera ocurrencia de la palabra "IA" en el siguiente texto e indicá en qué posición empieza y termina: `"Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"` ✅

2. **Ejercicio 2** — Encontrá todas las ocurrencias de la palabra "midu" en el siguiente texto, indicá en qué posición empieza y termina cada una, y cuántas veces se encontró: `"Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"` ✅

3. **Ejercicio 3** — Encontrá todas las ocurrencias de la palabra "python" en el siguiente texto sin distinguir entre mayúsculas y minúsculas: `"Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"` ✅

---

**02_metachars.py**

4. **Ejercicio 4** — Validá que un correo electrónico pertenezca a Gmail: `"miduga@hotmail.com"` ✅

5. **Ejercicio 5** — Dada una cadena con nombres de archivos, encontrá los nombres de los ficheros con extensión `.txt`: `"file1.txt file2.pdf midu-of.webp secret.txt"` ✅

---

**03_quantifiers.py**

6. **Ejercicio 6** — ¿Cuántas palabras tienen de 0 o más "a" seguidas de una "b"? ✅

7. **Ejercicio 7** — Hacé opcional que aparezca el prefijo `+34` en el siguiente número de teléfono: `"+34 688999999"` ✅

8. **Ejercicio 8** — Encontrá las palabras de entre 4 y 6 letras en el siguiente texto: `"ala casa árbol león cinco murcielago"` ✅

9. **Ejercicio 9** — Encontrá las palabras de más de 6 letras en el siguiente texto: `"ala fantastico casa árbol león cinco murcielago"` ✅

---

**04_sets.py**

10. **Ejercicio 10** — Dado el siguiente texto, encontrá únicamente las palabras `man`, `fan` y `ban`, ignorando el resto: `"man ran fan ñan ban"`

11. **Ejercicio 11** — Igual que el anterior pero ahora con coincidencias parciales en el medio — encontrá solo las palabras exactas `man`, `fan` y `ban`: `"omniman fanatico man bandana"`

12. **Ejercicio 12** — Ejercicio final combinando todo lo aprendido: mejorá y corregí la regex de validación de email cubriendo casos borde como `"lo.que+sea@shopping.online"` y `"michael@gov.co.uk"`

###################################################
# Curso de python desde cero
# 03/03/2026
# print("I'm the best person in the World!")
###################################################

#Diferencia entre intrepretado y compilado

# Los objetivos de python es que es facil de entender, de codigo abierto, 
# el codigo es comprensible como el ingles simple, 
# adecuado para desarrollo de tareas cotidianas.

###################################################
# 11/03/2026
# Python Software Foundation (PSF)

# Hay varios python entre ellos Cython, que es Python pasado a lenguaje C;
# Tambien existe Jython, que es Python pasado a lenguaje de Java, pero desarrollado con Python2;
# Ademas, hay un PyPy python dentro del mismo python;
# Por ultimo tambien hay una implementacion llamada MicroPython 

# IDLE es un acrónimo de: Integrated Development and Learning Environment
# (Desarrollo Integrado y Entorno de Aprendizaje)

###########################################################################

# Cython — es Python que se convierte a C para volverse más rápido. 
# Imagínalo así: Python normal es un carro automático, fácil de manejar 
# pero no el más rápido. Cython es ese mismo carro pero con motor turbo. 
# Lo usan cuando necesitan velocidad extrema.

###########################################################################

# Jython — es Python que corre dentro del mundo de Java. Útil para empresas 
# que ya tienen sistemas en Java y quieren agregar Python sin reescribir todo. 
# Pero como dices está basado en Python 2, está prácticamente muerto hoy.

###########################################################################

# PyPy — es Python corriendo dentro de Python pero optimizado. 
# El Python normal interpreta el código línea por línea, PyPy lo analiza completo y 
# lo optimiza antes de ejecutar. Resultado: hasta 10 veces más rápido que Python normal 
# sin cambiar nada de tu código.

###########################################################################

# MicroPython — es Python reducido al mínimo para correr en microcontroladores tiny
# como Arduino o Raspberry Pi. Imagínalo como Python en modo dieta, solo lo esencial 
# para caber en dispositivos con poca memoria.

###########################################################################

#12/03/2026

# print("La Witsi Witsi Araña \nsubió a su telaraña.")
# print()
# print("Vino la lluvia \ny se la llevó.")

# \n = Caracter de Nueva Linea 
# print("La Witsi Witsi Araña","subio","a su telaraña")

# print("Mi nombre es", "Python.", end="\n") #Formacion posicional
# print("Monty Python.")

# print("Mi nombre es ", end="")
# print("Monty Python.")

# Lo que puede procesar espacios es la palabra clave sep=
# print("My","name","is","Monty",sep="-")


# print("Mi", "nombre", "es", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*\n")
# print("Hello World!")

# print("Programming","Essentials","in",sep="***", end="...")
# print("Python")

########################################################

#Original
# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

#En una sola linea
# print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#El doble de grande
# print("         *")
# print("        * *")
# print("       *   *")
# print("      *     *")
# print("     *       *")
# print("    *         *")
# print("   *           *")
# print("  *             *")
# print(" *               *")
# print("*                 *")
# print("******       ******")
# print("     *       *")
# print("     *       *")
# print("     *       *")
# print("     *       *")
# print("     *       *")
# print("     *********")

#Doble
# print("    *","           ","    *")
# print("   * *","          ","   * *")
# print("  *   *","         ","  *   *")
# print(" *     *","        "," *     *")
# print("***   ***","       ","***   ***")
# print("  *   *","         ","  *   *")
# print("  *   *","         ","  *   *")
# print("  *****","         ","  *****")

#Doble*2
# print("    *    "*10)
# print("   * *   "*10)
# print("  *   *  "*10)
# print(" *     * "*10)
# print("***   ***"*10)
# print("  *   *  "*10)
# print("  *   *  "*10)
# print("  *****  "*10)

###########################################################################

# print("Mi\nnombre\nes\nBond.", end=" ")
# print("James Bond.", "El mejor")

# print(sep="&", "fish", "chips")
#Recuerda: Los argumentos de palabras clave deben pasarse después de cualquier argumento posicional requerido.

###########################################################################
###########################################################################

#13/03/2026

# print("2")
# print(2)

# #Valores tanto Octal como Hexadecimal
# print(0o123)
# print(0x123)

# #Flotantes
# print(3e10)
# print(6.62607E-34)
# print(0.0000000000000000000001)

#Cadenas
# print("Me gusta \"Monty python\"")
# print("Me gusta 'Monty python'")
# print('Me gusta "Monty python"')

# print("I'm Monty Python")
# print('I\'m Monty Python.')

#Boleanos
# print(True > False) #-> True siempre va a ser mayor que False
# print(True < False) #-> False nunca sera mayor que True

# print('"Estoy"\n""aprendiendo""\n"""Python"""')

# Ojo Jhon Edward, siempre en la division el resultado es flotante /, pero con la division sencilla
# Por eso se utiliza la otra solucion que es //, ahi es donde el resultado es Entero.

# print(12 % 4.5)
# 3.0 – no 3 pero 3.0. La regla aun funciona:

# 12 // 4.5 da 2.0,
# 2.0 * 4.5 da 9.0,
# 12 - 9.0 da 3.0. -> de ahi sale el 3
# print(9 % 6 % 2)
# print(2 ** 2 ** 3)

# print(-3 ** 2)
# print(-2 ** 3)
# print(-(3 ** 2))

##Prioridades 
# 1.** 
# 2.(+,-)-> Unario 
# 3.*,/,//,% 
# 4.+,- -> Binario

# print(2 * 3 % 5)
##############################################################################
#15/03/2026

# print((560/26)//2)

# print((2 ** 4), (2 * 4.), (2 * 4))
# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# print((2 % -4), (2 % 4), (2 ** 3 ** 2))

##############################################################################

#################################Variables####################################

# var = 1
# account_balance = 1000.0
# client_name = 'John Doe'
# print(var, account_balance, client_name)
# print(var)

# var = "3.5.8"
# print("Version de Python:" + var)

# var = 1
# print(var)
# var = var + 1
# print(var)
#560

# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5
# print("c =", c)

# John = 3
# Mary = 5
# Adan = 6
# print(John, Mary, Adan, sep=",") #-> Ojo Jhon Edward hay que utilizar el end, 
#                                     #que es para seguir y el sep que es para separar
# TotalManzanas = John + Mary + Adan
# print("Suma de las manzanas:" , TotalManzanas)

# x = x + 1 === x *= 1
# sheep = sheep + 1 === sheep += 1 -> Son la forma abreviada de conseguir lo mismo, que lo anterior

# variable = variable op expresión -> Es exactamente lo mismo
# variable op= expresión

#############################################################################

# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = miles * 1.61
# kilometers_to_miles =  kilometers / 1.61

# print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
# print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

#El dolar Hoy 15/03/2026
# Euro = 7.38
# Dolar = 12.25

# Euro_a_Dolar = Euro / 0.87
# Dolar_a_Euro =  Dolar * 0.87

# print(Euro, "Euros son", round(Euro_a_Dolar, 2), "Dolares")
# print(Dolar, "Dolares son", round(Dolar_a_Euro, 2), "Euros")

############################################################################

#16/03/2026

# Escenario
# Observa el código en el editor: lee un valor float, 
# lo coloca en una variable llamada x, e imprime 
# el valor de la variable llamada y. Tu tarea es completar el código para evaluar 
# la siguiente expresión:

# 3x3 - 2x2 + 3x - 1

# El resultado debe ser asignado a y.

# x =  0
# x = float(x)
# # Escribe tu código aquí.
# y = 3*x**3 - 2*x**2 + 3*x - 1
# print("y =", y)

# x =  1
# x = float(x)
# # Escribe tu código aquí.
# y = 3*x**3 - 2*x**2 + 3*x - 1
# print("y =", y)

# x =  -1
# x = float(x)
# # Escribe tu código aquí.
# y = 3*x**3 - 2*x**2 + 3*x - 1
# print("y =", y)

# var = 2
# print(var)
 
# var = 3
# print(var)
 
# var += 1
# print(var)
################################################################################

# print("Dime lo que sea!")
# anything = input()
# print("Mmm...", anything, "Es enserio?")
 
# anything = input("Dime lo que sea...!\n")
# print("Mmm...", anything, "Es enserio?")

# anything = float(input("Ingresa un Numero: "))
# something = anything ** 2
# print(anything, "Elevado al cuadrado es:", something)

# anything = float(input("Ingresa un número: "))
# something = anything ** 2.0
# print(anything, "al cuadrado es", something)

# print("Analizador del teorema de pitagoras")
# cat_1 = int(input("Ingrese el primer numero: "))
# cat_2 = int(input("Ingrese el segundo numero: "))
# hip = (cat_1 ** 2 + cat_2 ** 2) ** 0.5
# print("La longitud de la hipotenusa es:", hip)

##############################################################

#17/03/2026
# print("+" + "-"*10 + "+")
# print(("|" + " "*10 + "|\n")*5, end="") # -> Ese end sirve para que se quite el espacio
# print("+" + "-"*10 + "+")

# leg_a = float(input("Ingresa la longitud del primer cateto: "))
# leg_b = float(input("Ingresa la longitud del segundo cateto: "))
# print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))


# # ingresa un valor flotante para la variable a aquí
# print("Escribe dos numeros, pero ten encuenta que en ese orden se van a operar!")
# number1 = float(int(input("Escriba el primer numero aqui: ")))
# # ingresa un valor flotante para la variable b aquí
# number2 = float(int(input("Escriba el segundo numero aqui: ")))

# # mostrar el resultado de la suma aquí
# print("\n" + "La suma de los dos numeros, es:", number1 + number2, "\n")

# # mostrar el resultado de la resta aquí
# print("La resta de los dos numeros, es:", number1 - number2, "\n")

# # mostrar el resultado de la multiplicación aquí
# print("La multiplicacion de los dos numeros, es:", number1 * number2, "\n")

# # mostrar el resultado de la división aquí
# print("La division de los dos numeros, es:", number1 / number2)

# print("\n¡Eso es todo, amigos!")

##############################################################

# x = float(input("Ingresa el valor para x: "))
# # Escribe tu código aquí.
# y = 1/(x+1/(x+1/(x +(1/x))))

# print("y =", y)

# print(700%60)
# print(700//60)


# hour = int(input("Hora de inicio (horas): "))
# mins = int(input("Minuto de inicio (minutos): "))
# dura = int(input("Duración del evento (minutos): "))    
# # Escribe tu código aquí.
# minsTotal = mins + dura
# minsFinal = minsTotal % 60
# hourExtra = minsTotal // 60
# hourFinal = (hourExtra + hour) % 24
# print(hourFinal,minsFinal,sep=":")


##El programa hizo esto 

# hour = int(input("Hora de inicio (horas): "))
# mins = int(input("Minuto de inicio (minutos): "))
# dura = int(input("Duración del evento (minutos): "))
# mins = mins + dura # encuentra el número total de minutos
# hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
# mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
# hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
# print(hour, ":", mins, sep='')


# x = int(input("Ingresa un número: ")) # El usuario ingresa un 2
# print(x * "5")

# x = 1
# y = 2
# z = x
# x = y
# y = z
# print(x, y)

# x = input()
# y = input()
# print(type(x + y))

# x = int(input())
# y = int(input())

# x = x / y
# y = y / x

# print(y)

# x = int(input())
# y = int(input())

# x = x % y
# x = x % y
# y = y % x

# print(y)
# x = input()
# y = int(input())

# print(x * y)

# z = y = x = 1
# print(x, y, z, sep='*')

# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)

# x = int(input())
# y = int(input())

# print(x + y)

########################################################################

#18/03/2026

# El = es asignacion de valor

# El == es verficar si es igual, si lo es la respuesta es True, sino es, la respuesta es False

# Tambien existe otro que es !=, donde no es igual, si no lo es, la respuesta es True y si son iguales,
# la respuesta es False

# var = 0  # Asignando 0 a var
# print(var != 0)

# var = 1  # Asignando 1 a var
# print(var != 0)


#Tambien se utiliza el > Mayor que y < Menor que, que son estrictos, a diferencia del <= y >= que no 
#son estrictos como los anteriores

#Asi se puede hacer uso de las respuestas en una variable
#answer = number_of_lions >= number_of_lionesses

# n = int(input("Escribe un numero: "))
# print(n >= 100 )

#Formas de anidamiento

# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()

# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()

# Se debe prestar atención adicional a este caso:

# No debes usar else sin un if precedente;
# else siempre es la última rama de la cascada, independientemente de si has usado elif o no;
# else es una parte opcional de la cascada, y puede omitirse;
# Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas;
# Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.

# # Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
 
# # Elige el número más grande
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
 
# # Imprime el resultado
# print("El número más grande es:", larger_number)

# # Se leen tres números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))
 
# # Asumimos temporalmente que el primer número
# # es el más grande.
# # Lo verificaremos pronto.
# largest_number = number1
 
# # Comprobamos si el segundo número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number2 > largest_number:
#     largest_number = number2
 
# # Comprobamos si el tercer número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number3 > largest_number:
#     largest_number = number3
 
# # Imprime el resultado.
# print("El número más grande es:", largest_number)

# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))

# big_number = number1

# if number2 > big_number:
#     big_number = number2
    
# if number3 > big_number:
#     big_number = number3
    
# print("El numero mas grande es:", big_number)

# Hay una manera de llamar a los numero o buscar el mayor, con la funcion max() y para la funcion
#buscar el numero menor se elige el min()
# # Se leen tres números.
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))
 
# # Verifica cuál de los números es el mayor
# # y pásalo a la variable largest_number.
 
# largest_number = max(number1, number2, number3)
 
# # Imprime el resultado.
# print("El número más grande es:", largest_number)

# # Se leen tres números.
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))

# min_number = max(number1, number2, number3)
# print("El numero menor es:", min_number)
# #Ó
# print("El numero menor es:", min(number1, number2, number3))

###########################################################################

# LAB - Operadores de comparación y ejecución condicional
# word = input("Ingrese por favor una palabra: ")

# if word == "ESPATIFILIO": 
#     print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
# elif word == "espatifilo": 
#     print("No, ¡quiero un gran Espatifilo!")
# else: 
#     print("¡Espatifilo!, ¡No "+word+"!" )

###########################################################################

# LAB - Ejercicio de impuesto

# income = float(input("Introduce el ingreso anual: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# elif income >= 85528: 
# 	tax = 14839.02 + (income-85528)*0.32
# if tax < 0:
# 	tax = float(0)
	
# tax = round(tax, 0)

# print("El impuesto es:", tax, "pesos")

###########################################################################

#20/03/2026

#Lab - Año bisiesto y año comun
# year = int(input("Introduce un año: "))

# if year < 1582:
# 	print("No esta dentro del período del calendario Gregoriano")
# else:
#     #  Escribe el bloque if-elif-elif-else aquí.
# 	if year % 4 != 0:
# 		print("Año comun")
# 	elif year % 100 != 0:
# 		print("Año bisiesto")
# 	elif year % 400 != 0:
# 		print("Año comun")
# 	else:
# 		print("Año bisiesto")

###########################################################################

#25/03/2026
# La diferencia semántica es más importante: cuando se cumple la condición, 
# if realiza sus sentencias sólo una vez; 
# while repite la ejecución siempre que la condición se evalúe como True.

# # Almacena el actual número más grande aquí.
# largest_number = -999999999
 
# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))
 
# # Si el número no es igual a -1, continuaremos
# while number != -1:
#     # ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         # Sí si, se actualiza largest_number.
#         largest_number = number
#     # Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))
 
# # Imprime el número más grande.
# print("El número más grande es:", largest_number)

###########################################################################

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
# odd_numbers = 0
# even_numbers = 0
 
# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)

# counter = 5
# while counter:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)

# No te sientas obligado a codificar tus programas 
# de una manera que siempre sea la más corta y la más compacta.
# La legibilidad puede ser un factor más importante. 
# Manten tu código listo para un nuevo programador.

###########################################################################

#Juego del Mago
# print("¡Bienvenido al juego del mago, en donde debes encontrar el numero secreto!")

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)

# secret_number = int(input("Ingresa un numero: "))
# secret_number_mago= 777

# while secret_number != secret_number_mago:
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     secret_number = int(input("Ingresa un numero de nuevo: "))

# print("Bien hecho, muggle! Eres libre")

##############################################################
#Bucle For

# for i in range(10):
#     print("El valor de i es", i)

# for i in range(2, 10,2):
#     print("El valor de i es", i)

# for i in range(2, 8, 3):
#     print("El valor de i es", i)

# numero_inicial = 1
# for exponencial in range(16):
#     print("2 a la potencia de", exponencial,"es",numero_inicial)
#     numero_inicial = numero_inicial *2

# import time

# # Escribe un bucle for que cuente hasta cinco.
# for conteo in range(1,6):
#     # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi"
#     print(conteo,"Mississippi")
#     # Cuerpo del bucle, emplea : time.sleep(1)
#     time.sleep(1)
# # Escribe una función print con el mensaje final.
# print("¡Listos o no, ahí voy!") 

################################################################################
# # break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

################################################################################
# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")

################################################################################

# largest_number = -99999999
# counter = 0

# number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# if counter:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")

################################################################################
#3.2.9   LAB   La sentencia break - atrapado en un bucle

# while True:
#     word = input("Plese, Enter a word: ")
#     secret_word = "chupacabra"    
#     if secret_word == word:
#         break
#     # word = input("Please, try again!: ")
# print("Has dejado el bucle con éxito.")

################################################################################
#3.2.10   LAB   La sentencia continue – el Feo Devorador de Vocales

# user_word = input("Ingrese una palabra: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     print(letter)

################################################################################

# #3.2.11   LAB   La sentencia continue – el Lindo Devorador de Vocales
# user_word = input("Ingrese una palabra: ")
# user_word = user_word.upper()
# word_without_vowels = ""

# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     word_without_vowels = word_without_vowels + letter

# print(word_without_vowels)

################################################################################

# while con else
# i = 5
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

# # for con else
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)

################################################################################
# 3.2.14   LAB   Fundamentos del bucle while

# blocks = int(input("Ingresa el número de bloques: "))
# layer = 0
# height = 0

# # Escribe tu código aquí.
# while blocks > layer:
#     layer += 1
#     blocks = blocks - layer
#     height += 1

# print("La altura de la pirámide:", height)

################################################################################

# #3.2.15   LAB   La hipótesis de Collatz

# c0 = int(input("Coloca cualquier numero entero que no sea 0, ni negativo: "))
# step = 0

# while c0 > 1:
#     step = step + 1
#     if c0 % 2 == 0:
#         c0 = c0//2
#         print(c0)
#     elif c0 % 2 == 1:
#         c0 = 3 * c0 + 1
#         print(c0)

# print(c0)
# print("Pasos =",step)

################################################################################

# 1. Existen dos tipos de bucles en Python: while y for:

# El bucle while ejecuta una sentencia o un conjunto de sentencias 
# siempre que una condición booleana especificada sea verdadera

# El bucle for ejecuta un conjunto de sentencias muchas veces; se usa para 
# iterar sobre una secuencia (por ejemplo, una lista, un diccionario, una 
# tupla o un conjunto; pronto aprenderás sobre ellos) u otros objetos que 
# son iterables (por ejemplo, cadenas). Puedes usar el bucle for para iterar sobre una 
# secuencia de números usando la función incorporada range. Mira los ejemplos 
# a continuación:

# 2. Puedes usar las sentencias break y continue para cambiar el flujo de un bucle:

# Utiliza break para salir de un bucle, por ejemplo:

# text = "OpenEDG Python Institute
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end="")

# Utiliza continue para omitir la iteración actual, y continuar con la siguiente iteración, por ejemplo:

# text = "pyxpyxpyx
# for letter in text:
#     if letter == "x":
#         continue
#     print(letter, end="")
 
#  3. Los bucles while y for también pueden tener una cláusula 
# else en Python. La cláusula else se ejecuta después de que 
# el bucle finalice su ejecución siempre y cuando no haya 
# terminado con break, por ejemplo:

# n = 0
 
# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")
 
# print()
 
# for i in range(0, 3):
#     print(i)
# else:
#     print(i, "else")
 
# 4. La función range() genera una secuencia de números. 
# Acepta enteros y devuelve objetos de rango. La sintaxis 
# de range() tiene el siguiente aspecto: range(start, stop, step), donde:

# start es un parámetro opcional que especifica el número de 
# inicio de la secuencia (0 por defecto)
# stop es un parámetro opcional que especifica el final de 
# la secuencia generada (no está incluido).
# y step es un parámetro opcional que especifica la diferencia 
# entre los números en la secuencia es (1 por defecto.)
# Código de ejemplo:


# for i in range(3):
#     print(i, end=" ")  # output: 0 1 2
 
# for i in range(6, 1, -2):
#     print(i, end=" ")  # output: 6, 4, 2

################################################################################

# Pregunta 1: Crea un bucle for que cuente de 0 a 10, 
# e imprima números impares en la pantalla. 
# Usa el esqueleto de abajo:

# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)

# Pregunta 2: Crea un bucle while que cuente de 0 a 10, 
# e imprima números impares en la pantalla. 
# Usa el esqueleto de abajo:

# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# Pregunta 3: Crea un programa con un bucle for y una sentencia break.
# El programa debe iterar sobre los caracteres en una dirección de correo
# electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la 
# parte antes de @ en una línea. Usa el esqueleto de abajo:

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch)

# Pregunta 4: Crea un programa con un bucle for y una sentencia continue. 
# El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 
# con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

################################################################################

#Operadores de bit a bit, si es & es una conjucion y si es OR es una disyuncion, entonces a eso se refiere
# hay que tener mucho cuidado con eso

# Puedes estar familiarizado con las leyes de De Morgan. Dicen que:

# La negación de una conjunción es la separación de las negaciones.

# La negación de una disyunción es la conjunción de las negaciones.

# Escribamos lo mismo usando Python:

# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

# i = 1
# j = not not i

# print(i, j)

# La diferencia en el funcionamiento de los operadores lógicos y de bits es importante: los operadores lógicos
# no penetran en el nivel de bits de su argumento. Solo les interesa el valor entero final.

# La diferencia en una frase:

# Lógico → mira el número completo y pregunta ¿es cero o no?
# Bits → mira cada bit individualmente y opera sobre ellos

########################################################################################

# Operadores lógicos (and, or, not):
# No miran los bits individuales, solo ven si el número es cero o no cero.
# pythoni = 15  # En bits es: 0000 1111
# j = 22  # En bits es: 0001 0110

# print(i and j)  # Resultado: 22

########################################################################################

# Operadores de bits (&, |, ~, ^):
# Sí penetran hasta el nivel de cada bit individual y operan uno por uno.
# pythoni = 15  # En bits: 0000 1111
# j = 22  # En bits: 0001 0110

# print(i & j)  # Resultado: 6

####################################################################################

# flag_register = 0x1234  # valor del sistema
# the_mask = 8            # 8 en binario es 00001000, el bit 3

# if flag_register | the_mask:
#     print("Mi bit está en 1, función activa")
# else:
#     print("Mi bit está en 0, función inactiva")


##################################Permisos de usuarios en Linux##################################

# Número      Binario                 Permisos
# ✅7           111         lectura + escritura + ejecución 
# ✅6           110         lectura + escritura
# ✅5           101         lectura + ejecución
# ✅4           100         solo lectura
# ✅3           011         escritura + ejecución
# ✅2           010         solo escritura
# ✅1           001         solo ejecución0000sin permisos

####################################################################################

#05/04/2026 -> Dia del cumpleaños de laura

#Porque se necesitan las listas, es porque si se necesitan muchas variables, aqui entran las listas

# numbers = [10, 5, 7, 2, 1, 30, 5, 4, 2026]
# print("Imprimir los numeros de la lista:", numbers)

# numbers[4] = 7
# print("Imprimir los numeros de la lista:", numbers)

# numbers[1] = numbers[4]
# print("Imprimir los numeros de la lista:", numbers)

# del numbers[5]
# print(numbers)

# print("Longitud de la lista:", len(numbers)) 

# # numbers = [111, 7, 2, 1]
# print(numbers[-3])

#####3.4.6   LAB   Los fundamentos de las listas#####

# hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
# print(hat_list)

# # Paso 1: escribe una línea de código que solicite al usuario
# # reemplazar el número de en medio con un número entero ingresado por el usuario.
# hat_list[2] = int(input("Por favor cambia el tercer numero que vez en pantalla, escribe cualquier numero: "))

# # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
# del hat_list[-1]

# # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
# print("La lista tiene", len(hat_list),"numeros.")

# print(hat_list)


####################################################################
# Funciones vs metodos

# Los metodos son funciones, pero con la diferencia que los metodos se aplican a un objeto,
# mientras que las funciones no necesitan de un objeto para ser utilizadas, por ejemplo:

# Esta es una invocacion normal de una funcion: result = function(arg)

# Esta es una invocacion normal de un metodo: result = data.method(arg)

# append() es un metodo y este hace que un nuevo elemento se añada al final de la lista.

# insert() es un metodo y este hace que un nuevo elemento se añada a la lista en la posicion 
# que se le indique,
# por ejemplo: list.insert(0, "nuevo elemento") esto hace que el nuevo 
# elemento se añada al inicio de la lista, y si se le indica list.insert(2, "nuevo elemento")
# esto hace que el nuevo elemento se añada en la posicion 2 de la lista, y asi sucesivamente. 

# len() es una funcion y esta hace que se cuente el numero de elementos que hay en la lista.

# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###

# numbers.append(4)
# print(len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# numbers.insert(1, 333)
# print(len(numbers))
# print(numbers)


# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i+1)
# print(my_list)


# my_list = []  # Creando una lista vacía.
 
# for i in range(5):
#     my_list.insert(0, i + 1)
# print(my_list)

# 3.4.9 Haciendo uso de las listas

# my_list = [10, 1, 8, 3, 5]
# total = 0

# print(len(my_list))

# for i in range(len(my_list)): # -> La función len() devuelve el número de elementos en la lista,
                                #  y range() genera una secuencia de números desde
                                #  0 hasta len(my_list)-1, lo que nos permite acceder a cada    
                                #  elemento de la lista utilizando su índice.   
                                #  Pero para ser realistas, no es necesario usar len(mi_list) para recorrer la lista, 
                                #  se puede hacer de una manera mas sencilla, como se muestra a continuacion: 
#     total += my_list[i]
# print(total)

# my_list = [10, 1, 8, 3, 5]
# total = 0
# for i in my_list:
#     total += i
# print(total)

# Que son las listas en accion? -> Son una estructura de datos que nos permite almacenar una 
# colección de elementos,
# y estos elementos pueden ser de cualquier tipo de dato, como por ejemplo: enteros,

# variable_1 = 1
# variable_2 = 2
 
# variable_2 = variable_1
# variable_1 = variable_2

# print(variable_1, variable_2)

#Aqui se puede cambiar el valor de las variables sin necesidad de usar una variable temporal, 
#como se muestra a continuacion:
# variable_1 = 1
# variable_2 = 2
# variable_1, variable_2 = variable_2, variable_1

# my_list = [10, 1, 8, 3, 5]
 
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
 
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# print(my_list)


###3.4.11   LAB   Los fundamentos de las listas: los Beatles###

beatles = []  # Crea una lista vacía llamada beatles.
print("Paso 1:", beatles)  # Imprime la lista.

# Agrega los Beatles a la lista.
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)  # Imprime la lista.

for i in range(2):
    beatles.append(input("Ingrese el nombre de un miembro de los Beatles: "))
print("Paso 3:", beatles)  # Imprime la lista.

del beatles[-2]
del beatles[-1] 
print("Paso 4:", beatles)  # Imprime la lista.

beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)  # Imprime la lista.

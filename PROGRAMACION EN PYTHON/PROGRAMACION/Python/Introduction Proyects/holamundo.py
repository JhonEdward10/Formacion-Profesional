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

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

big_number = number1

if number2 > big_number:
    big_number = number2
    
if number3 > big_number:
    big_number = number3
    
print("El numero mas grande es:", big_number)





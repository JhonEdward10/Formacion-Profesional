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

# a = 6
# b = 3
# a /= 2 * b
 


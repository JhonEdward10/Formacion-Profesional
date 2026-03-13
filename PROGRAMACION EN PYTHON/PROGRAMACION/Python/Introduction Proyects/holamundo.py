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
# print("James Bond.")

# print(sep="&", "fish", "chips")
#Recuerda: Los argumentos de palabras clave deben pasarse después de cualquier argumento posicional requerido.
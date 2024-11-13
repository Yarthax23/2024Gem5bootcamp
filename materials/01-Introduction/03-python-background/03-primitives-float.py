
#!/usr/bin/env python3.12
"""
 Esta porción de código permite hacer este archivo un ejecutable para correrlo desde BASH
 Ver referencia: https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script

 $ chmod +x  03-primitives-float.py

Y luego puedo correrlo como ejecutable
 $ ./03-primitives-float.py

En vez de cada ver hacer
 $ python3.12 03-primitives-float.py



Otro método consiste en crear un archivo adicional job.sh (un shell script)
Que contenga

    #!/bin/bash
    python3.12 03-primitives-float.py

Al hacerlo ejecutable (chmod +x job.sh), lo corremos ./job.sh y se corre el script (con 03-primitives-float.py dentro)
Éste podría extenderse para correr varios python (o varias cosas) de una, tiene algo de similitud con MakeFiles de AyOC
"""



"""
This script demonstrates the use of floats as a primative data type in
Python.
"""

# Floats are a primative data type in Python. They are "real numbers" and are
# declared like so. Here we declare a variable `x` and assign it the literal
# value `1.5`.
x = 1.5
print(f"Value of x: {x}")

# Like integers floats can be set using arithmetic operations of literals or
# other float variables.

# Set variable `y`` to `10.5 + 5.5`.`
y = 10.5 + 5.5
print(f"Value of y: {y}")

# Set variable `z` to `y - x` (in this case, 16 - 1.5).
z = y - x
print(f"Value of z: {z}")

# Multiplication
multi_xy = x * y
print(f"Value of multi_xy: {multi_xy}")

# Division
div_xy = y / x
print(f"Value of div_xy: {div_xy}")


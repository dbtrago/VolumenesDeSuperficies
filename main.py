from sympy import sympify, symbols
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def evaluar_expresion(expresion, x, y):
    return eval(expresion)

def leerFuncion(mensaje):
    funcion = input(mensaje)
    return funcion


def leerDatos(mensaje):
    num = int(input(mensaje))
    return num


def calcularDeltaX(a, b, n):
    delta_x = (b - a) / n
    return delta_x


def calcularDeltaY(c, d, m):
    delta_y = (d - c) / m
    return delta_y


def evaluarFuncion(funcion, i, j):
    x, y = symbols('x y')
    try:
        expresion = sympify(funcion)
        x_value = i  # Punto x
        y_value = j  # Punto y
        resultado = expresion.subs([(x, x_value), (y, y_value)])
        return float(resultado)
    except Exception as e:
        print("Ha ocurrido un error al evaluar la expresión:", e)


def calcularV(funcion, a, b, c, d, n, m, delta_x, delta_y):
    # se calculan los puntos iniciales para evaluar funcion
    w = a+delta_x/2
    v = c+delta_y/2

    print("w: " + str(w), "v: " + str(v))
    # se calcula delta_a
    delta_a = (delta_x*delta_y)
    # se empieza la suma en 0
    suma = 0
    print("delta_x: "+str(delta_x))
    print("delta_y: "+str(delta_y))
    # va a operar hasta que w y v superen a b y d
    for i in range(int(n)): #for(int i=w, i==b,i++)
        #print("2 w: " + str(w), "v: " + str(v))
        for j in range(int(m)):
            #suma += delta_a * evaluarFuncion(funcion, w, v)
            suma = suma + (delta_a * evaluarFuncion(funcion, w, v))
            print("w: "+str(w), "v: "+str(v))
            #print("delta_a = "+str(delta_a)+" funcion:"+str(evaluarFuncion(funcion,float(w),float(v))))
            w = w + delta_x
            print("Sumatoria actual: " + str(suma))
        w = a + delta_x / 2
        v = v + delta_y
    return suma

# Definir la función a integrar
def f(x, y):
    return x**2 + y**2

# Definir los límites de integración
x_min, x_max = 0, 1
y_min, y_max = 0, 1


# Función que realiza la integración doble
def integrar_doble(func, x_min, x_max, y_min, y_max):
    result, error = integrate.dblquad(func, x_min, x_max, y_min, y_max)
    return result, error

def main():
    funcion = leerFuncion("Ingrese una funcion en terminos de x, y: ")
    # ----------------------------------------------------- #
    a = leerDatos("ingrese un valor para a: ")
    b = leerDatos("ingrese un valor para b: ")
    while a >= b:
        a = leerDatos("ingrese un valor para a: ")
        b = leerDatos("ingrese un valor para b: ")
        if a < b:
            break
    # ----------------------------------------------------- #
    n = leerDatos("ingrese un valor para n: ")
    delta_x = calcularDeltaX(a, b, n)

    c = leerDatos("Ingrese un valor para c: ")
    d = leerDatos("Ingrese un valor para d: ")
    while c >= d:
        c = leerDatos("Ingrese un valor para c: ")
        d = leerDatos("Ingrese un valor para d: ")

    m = leerDatos("Ingrese un valor para m: ")
    delta_y = calcularDeltaY(c, d, m)
    # ---------------------------------------------------- #
    volumen = calcularV(funcion, a, b, c, d, n, m, delta_x, delta_y)
    print("Para la funcion: " + str(funcion))
    print("El volumen aproximando con sumatorias es: " + str(volumen))

    print("----------------------------------------------------")

    # Convertir la cadena de texto a una función usando eval
    funcion_integral = eval(f"lambda x, y: {funcion}")

    # Llamar a la función con la función definida por el usuario
    resultado, error = integrar_doble(funcion_integral, a, b, c, d)

    # Imprimir el resultado
    print(f"El volumen con integral doble es: {resultado}")
    print(f"Error estimado: {error}")


    # --------------------GRAFICA------------------------ #
    # Valores de los ejes
    x_values = np.linspace(a, b, 100)
    y_values = np.linspace(c, d, 100)
    X, Y = np.meshgrid(x_values, y_values)

    # Calcular los valores de las funciones
    Z3 = evaluar_expresion(funcion, X, Y)

    # Crear la figura
    fig = plt.figure()

    # Crear el eje 3D
    ax = fig.add_subplot(111, projection='3d')

    # Graficar las funciones en el espacio 3D
    ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='b', label=funcion)

    # Graficar el plano XY (z=0)
    ax.plot_surface(X, Y, np.zeros_like(Z3), alpha=0.5, rstride=100, cstride=100, color='r', label='Plano XY')

    # Establecer el color de los ejes
    #ax.axhline(0, color="black")
    #ax.axvline(0, color="black")

    # Mostrar el gráfico
    ax.legend()
    plt.show()

main()
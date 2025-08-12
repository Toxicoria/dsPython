
def obtenerGrados():
    while True:
        try:
            return float(input("Ingrese la temperatura: "))
        except ValueError:
            print("Error: Ingrese solo números.")

def obtenerEscala():
    while True:
        escala = input("Ingrese la escala de origen [C / F]: ").lower()
        if escala in ('c', 'f'):
            return escala
        print("Error: Escala no válida. Ingrese 'C' para Celsius o 'F' para Fahrenheit.")

def convertirTemp(temp, escala_origen):
    if escala_origen == 'c':
        resultado = (temp * 9/5) + 32
        print(f"{temp}°C es igual a {resultado:.2f}°F")
    else:
        resultado = (temp - 32) * 5/9
        print(f"{temp}°F es igual a {resultado:.2f}°C")

if __name__ == "__main__":
    temperatura = obtenerGrados()
    escala = obtenerEscala()
    convertirTemp(temperatura, escala)

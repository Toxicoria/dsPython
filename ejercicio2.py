from sys import argv

if __name__ == "__main__":
    
    if len(argv) < 2:
        print("Error: Se necesita un argumento de operación.")
        print("Uso: python ejercicio2.py [-s | -r | -m | -d]")
    else:
        
        argumento = argv[1]

        try:
            x_str = input("Introduce el primer número: ")
            x = float(x_str)
            y_str = input("Introduce el segundo número: ")
            y = float(y_str)
        except ValueError:
            print("Error: Debes introducir valores numéricos.")
            exit() 

        match argumento:
            case "-s":
                print("SUMA")
                print(f"{x} + {y} = {x+y}")
            
            case "-r":
                print("RESTA")
                print(f"{x} - {y} = {x-y}")
            
            case "-m":
                print("MULTIPLICACIÓN")
                print(f"{x} * {y} = {x*y}")
            
            case "-d":
                print("DIVISIÓN")
                if y == 0:
                    print("Error: No se puede dividir por cero.")
                else:
                    print(f"{x} / {y} = {x/y}")
            case _:
                print(f"El argumento '{argumento}' no es válido.")
                print("Los argumentos válidos son: -s | -r | -m | -d")
        
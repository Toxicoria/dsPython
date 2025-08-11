from sys import argv

if __name__ == "__main__":
    if len(argv)>1:
        print("venis con argumentos:")
        print("----------------------")
        for i in argv:
            print(f"¡Hola {i}!")
    else:
        print("¡Hola Mundo!")
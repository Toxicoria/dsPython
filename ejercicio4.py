from datetime import datetime

class libro:
    def __init__(self, titulo: str, autor: str, anio: int, genero: str):
        if not isinstance(anio, int):
            raise TypeError("El parámetro 'anio' debe ser un número entero.")
        if anio <= 0:
            raise ValueError("El año debe ser un número positivo.") 
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.anio}) - Género: {self.genero}"

    def obtenerInfo(self):
        return self.__str__()
    
    def esClasico(self, anios_para_ser_clasico: int = 50) -> bool:

      año_actual = datetime.now().year
      return (año_actual - self.anio) > anios_para_ser_clasico

if __name__ == "__main__":
    print("--- Creación exitosa ---")
    l1 = libro("El Señor de los Anillos", "J.R.R. Tolkien", 1954, "Fantasía épica")
    l2 = libro("Los Anillos del Señor", "Random", 1398, "Católico")
    l3 = libro("Manija Colectiva", "Z.Z.Z. Juan", 2020, "Carreras(???)")

    libros = [l1,l2,l3]
    
    for l in libros:
        print(l)
        print(f"¿Es un clásico? -> {l.esClasico()}")
        print("\n" + "="*30 + "\n")

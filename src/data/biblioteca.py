"""Libros y categorias almacenadas"""
from models.libro import Libro

# Lista de libros (usa esta estructura)
libros: list[Libro] = [
    {"titulo": "Cien anos de soledad", "autor": "Garcia Marquez",
        "paginas": 471, "disponible": True},
    {"titulo": "Don Quijote", "autor": "Cervantes",
        "paginas": 863, "disponible": False},
    {"titulo": "El principito", "autor": "Saint-Exupery",
        "paginas": 96, "disponible": True},
    {"titulo": "1984", "autor": "George Orwell", "paginas": 328, "disponible": True}
]

# SET con las categorias disponibles
categorias = {"Ficcion", "Ciencia", "Historia", "Poesia"}

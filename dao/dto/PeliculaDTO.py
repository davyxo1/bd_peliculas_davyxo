class PeliculaDTO:
    def __init__(self, id_pelicula, titulo, duracion, fecha_estreno, genero, idioma, director):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.duracion = duracion
        self.fecha_estreno = fecha_estreno
        self.genero = genero
        self.idioma = idioma
        self.director = director

    def __str__(self):
        return f"{self.id_pelicula} - {self.titulo} ({self.duracion} min) - Dirigida por {self.director}"

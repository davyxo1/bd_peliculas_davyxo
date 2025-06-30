class PeliculaDTO:
    def __init__(self, id_pelicula=None, titulo="", duracion=0, fecha_de_estreno=None, genero=0, idioma=0, director=""):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.duracion = duracion
        self.fecha_de_estreno = fecha_de_estreno
        self.genero = genero
        self.idioma = idioma
        self.director = director

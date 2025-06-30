CREATE DATABASE bd_peliculas;

USE bd_peliculas;

CREATE TABLE pelicula (
    id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
    titulo_pelicula VARCHAR(45),
    duracion INT,
    fecha_de_estreno DATE,
    genero INT,
    idioma INT,
    director VARCHAR(45)
);

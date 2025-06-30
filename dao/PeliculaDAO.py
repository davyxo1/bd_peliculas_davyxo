class PeliculaDAO:
    def insertar(self, pelicula):
        print(f"[SIMULADO] Insertar: {pelicula}")

    def eliminar(self, id_pelicula):
        print(f"[SIMULADO] Eliminar película con ID: {id_pelicula}")

    def modificar(self, pelicula):
        print(f"[SIMULADO] Modificar película: {pelicula}")

    def consultar_todo(self):
        print("[SIMULADO] Mostrar todas las películas")
        return []

    def consultar_parcial(self, campo, valor):
        print(f"[SIMULADO] Consultar películas donde {campo} = {valor}")
        return []

    def consultar_particular(self, id_pelicula):
        print(f"[SIMULADO] Consultar película con ID: {id_pelicula}")
        return None

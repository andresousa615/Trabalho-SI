class Hospital:

    def __init__(self, listaRecetores: list, coordenada_x: float, coordenada_y: float, equipasMedicas: int, salas: int) -> object:
        self.listaRecetores = listaRecetores
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.equipasMedicas = equipasMedicas
        self.salas = salas

    def get_listaRecetores(self):
        return self.listaRecetores

    def set_listaRecetores(self, listaRecetores: list):
        self.listaRecetores = listaRecetores

    def get_coordenada_x(self):
        return self.coordenada_x

    def set_coordenada_x(self, coordenada_x: float):
        self.coordenada_x = coordenada_x

    def get_coordenada_y(self):
        return self.coordenada_y

    def set_coordenada_y(self, coordenada_y: float):
        self.coordenada_y = coordenada_y

    def get_equipasMedicas(self):
        return self.equipasMedicas

    def set_equipasMedicas(self, equipasMedicas: int):
        self.equipasMedicas = equipasMedicas

    def get_salas(self):
        return self.salas

    def set_salas(self, salas: int):
        self.salas = salas

    def __str__(self):
        listaRecetores_str = ', '.join([str(recetor) for recetor in self.listaRecetores])
        return (f"Hospital[listaRecetores=[{listaRecetores_str}], coordenada_x={self.coordenada_x}, "
                f"coordenada_y={self.coordenada_y}, equipasMedicas={self.equipasMedicas}, salas={self.salas}]")

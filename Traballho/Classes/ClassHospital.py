class Hospital:

    def __init__(self, listaPacientes: list, coordenada_x: float,coordenada_y: float, equipasMedicas: int, salas: int):
        self.listaPacientes = listaPacientes
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.equipasMedicas = equipasMedicas
        self.salas = salas

    def get_listaPacientes(self):
        return self.listaPacientes

    def set_listaPacientes(self, listaPacientes: list):
        self.listaPacientes = listaPacientes

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

    def toString(self):
        return (f"listaPacientes: {self.listaPacientes}, coordenada_x: {self.coordenada_x}, coordenada_y: {self.coordenada_y}, equipasMedicas: {self.equipasMedicas}")

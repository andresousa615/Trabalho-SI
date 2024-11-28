
class Transporte:

    def __init__(self, tipo_transporte: str, x: int, y: int, disponibilidade: bool):
        # Atributos relacionados ao transporte
        self.tipo_transporte = tipo_transporte  # Tipo do transporte (ex: Ambulância, Helicóptero, etc.)
        self.x = x  # Posição X do transporte (coordenada)
        self.y = y  # Posição Y do transporte (coordenada)
        self.disponibilidade = disponibilidade  # Se o transporte está disponível ou não

    def get_tipo_transporte(self):
        return self.tipo_transporte

    def set_tipo_transporte(self, tipo_transporte: str):
        self.tipo_transporte = tipo_transporte

    def get_x(self):
        return self.x

    def set_x(self, x: int):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y: int):
        self.y = y

    def get_disponibilidade(self):
        return self.disponibilidade

    def set_disponibilidade(self, disponibilidade: bool):
        self.disponibilidade = disponibilidade

    def __str__(self):
        return (f"Tipo de transporte: {self.tipo_transporte}, "
                f"Coordenada X: {self.x}, Coordenada Y: {self.y}, "
                f"Disponibilidade: {self.disponibilidade}")

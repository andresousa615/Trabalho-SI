class Orgao:

    def __init__(self, jid_orgao: str, sangue: str, nome_orgao: str, x: int, y: int, validade: int):
        self.jid_orgao = jid_orgao
        self.sangue = sangue
        self.nome_orgao = nome_orgao
        self.x = x  # Coordenada x
        self.y = y  # Coordenada y
        self.validade = validade  # Validade em dias

    # Getters e setters
    def get_jid_orgao(self):
        return self.jid_orgao

    def set_jid_orgao(self, jid_orgao: str):
        self.jid_orgao = jid_orgao

    def get_sangue(self):
        return self.sangue

    def set_sangue(self, sangue: str):
        self.sangue = sangue

    def get_nome_orgao(self):
        return self.nome_orgao

    def set_nome_orgao(self, nome_orgao: str):
        self.nome_orgao = nome_orgao

    def get_x(self):
        return self.x

    def set_x(self, x: int):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y: int):
        self.y = y

    def get_validade(self):
        return self.validade

    def set_validade(self, validade: int):
        self.validade = validade

    # Representação em string
    def __str__(self):
        return (f"jid_orgao: {self.jid_orgao}, sangue: {self.sangue}, nome_orgao: {self.nome_orgao}, "
                f"x: {self.x}, y: {self.y}, validade: {self.validade} dias")



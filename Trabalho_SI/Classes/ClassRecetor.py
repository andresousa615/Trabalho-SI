
class Recetor:

    def __init__(self, jid_recetor: str, urgencia: str, sangue: str, nome_orgao: str , orgao_atribuido: bool):
        self.urgencia = urgencia
        self.sangue = sangue
        self.jid_recetor = jid_recetor
        self.nome_orgao = nome_orgao
        self.orgao_atribuido = orgao_atribuido

    def get_urgencia(self):
        return self.urgencia

    def set_urgencia(self, urgencia: str):
        self.urgencia = urgencia

    def get_sangue(self):
        return self.sangue

    def set_sangue(self, sangue: str):
        self.sangue = sangue

    def get_jid_recetor(self):
        return self.jid_recetor

    def set_jid_recetor(self, jid_recetor: str):
        self.jid_recetor = jid_recetor

    def get_orgao_atribuido(self):
        return self.orgao_atribuido

    def set_orgao_atribuido(self, orgao_atribuido: bool):
        self.orgao_atribuido = orgao_atribuido

    def get_nome_orgao(self):
        return self.nome_orgao

    def set_nome_orgao(self, nome_orgao: str):
        self.nome_orgao = nome_orgao

    def __str__(self):
        return (f"jid_recetor: {self.jid_recetor}, urgencia: {self.urgencia}, sangue: {self.sangue},  orgao_atribuido: {self.orgao_atribuido}, nome_orgao: {self.nome_orgao}")

    def _repr_(self):
        return f"Recetor({repr(self.jid_recetor)}, {repr(self.urgencia)})"

class Recetor:

    def __init__(self, jid_recetor: str, urgencia: str, compatibilidade: str, nome_orgao: str , orgao_atribuido: bool):
        self.urgencia = urgencia
        self.compatibilidade = compatibilidade
        self.jid_recetor = jid_recetor
        self.orgao_atribuido = orgao_atribuido
        self.nome_orgao = nome_orgao

    def get_urgencia(self):
        return self.urgencia

    def set_urgencia(self, urgencia: str):
        self.urgencia = urgencia

    def get_compatibilidade(self):
        return self.compatibilidade

    def set_compatibilidade(self, compatibilidade: str):
        self.compatibilidade = compatibilidade

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

    def toString(self):
        return (f"jid_recetor: {self.jid_recetor}, urgencia: {self.urgencia}, compatibilidade: {self.compatibilidade},  orgao_atribuido: {self.orgao_atribuido}, nome_orgao: {self.nome_orgao}")
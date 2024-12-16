
class Recetor:

    def __init__(self, urgencia: str, compatibilidade: str, jid_paciente: str, orgao_atribuido: bool, nome_orgao: str ):
        self.urgencia = urgencia
        self.compatibilidade = compatibilidade
        self.jid_paciente = jid_paciente
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

    def get_jid_paciente(self):
        return self.jid_paciente

    def set_jid_paciente(self, jid_paciente: str):
        self.jid_paciente = jid_paciente

    def get_orgao_atribuido(self):
        return self.orgao_atribuido

    def set_orgao_atribuido(self, orgao_atribuido: bool):
        self.orgao_atribuido = orgao_atribuido

    def get_nome_orgao(self):
        return self.nome_orgao

    def set_nome_orgao(self, nome_orgao: str):
        self.nome_orgao = nome_orgao

    def toString(self):
        return (f"urgencia: {self.urgencia}, compatibilidade: {self.compatibilidade}, jid_paciente: {self.jid_paciente}, orgao_atribuido: {self.orgao_atribuido}, nome_orgao: {self.nome_orgao}")
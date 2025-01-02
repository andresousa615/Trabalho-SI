from Trabalho_SI.Classes.ClassHospital import Hospital
from Trabalho_SI.Classes.ClassOrgao import Orgao
from Trabalho_SI.Classes.ClassRecetor import *
from Trabalho_SI.Classes.ClassTransporte import Transporte


class PedidoTransporte:

    def __init__(self, recetor_selecionado: Recetor, orgao_recebido: Orgao, hospital_jid: str, hospital_obj: Hospital,
                 transporte: Transporte):
        self.recetor_selecionado = recetor_selecionado
        self.orgao_recebido = orgao_recebido
        self.hospital_jid = hospital_jid
        self.hospital_obj = hospital_obj
        self.transporte = transporte

    # Getters e setters

    def get_recetor_selecionado(self):
        return self.recetor_selecionado

    def get_orgao(self):
        return self.orgao_recebido

    def get_hospital_jid(self):
        return self.hospital_jid

    def get_hospital_obj(self):
        return self.hospital_obj

    def get_transporte(self):
        return self.transporte

    def set_recetor_selecionado(self, recetor_selecionado: Recetor):
        self.recetor_selecionado = recetor_selecionado

    def set_orgao_recebido(self, orgao_recebido: Orgao):
        self.orgao_recebido = orgao_recebido

    def set_hospital_jid(self, hospital_jid: str):
        self.hospital_jid = hospital_jid

    def set_hospital_obj(self, hospital_obj: Hospital):
        self.hospital_obj = hospital_obj

    def set_transporte(self, transporte: Transporte):
        self.transporte = transporte

        # Representação em string
    def __str__(self):
        return (f"recetor: {self.recetor_selecionado}, orgao: {self.orgao_recebido}, hospital_jid: {self.hospital_jid}, hospital_obj: {self.hospital_obj}, "
                f"transporte: {self.transporte}")

from spade import agent
from Trabalho_SI.Behaviours.Hospital_Behaviours import *

class AgentHospital(agent.Agent):

    def __init__(self, jid, password, x, y, nr_equipas, nr_salas):
        super().__init__(jid, password)
        # Atributos do hospital
        self.lista_recetores = []  # Lista de recetores inicialmente vazia
        self.x = x
        self.y = y
        self.nr_equipas = nr_equipas
        self.nr_salas = nr_salas


    async def setup(self):
        print(f"Hospital Agent {self.jid} está ativo")
        hospital_behaviour_registar = HospitalBehaviour_registo()
        hospital_behaviour_registarRecetor = HospitalReceiveRecetorBehaviour()
        self.add_behaviour(hospital_behaviour_registar)
        self.add_behaviour(hospital_behaviour_registarRecetor)

    def add_recetor(self, recetor):
        """Adiciona um recetor à lista do hospital."""
        self.lista_recetores.append(recetor)
        print(f"Recetor {recetor.jid_recetor} adicionado ao hospital {self.jid}. Total de recetores: {len(self.lista_recetores)}")


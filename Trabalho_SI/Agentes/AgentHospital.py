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
        self.lista_recetores_salvos = [] # Lista de recetores salvos/que sofreram transplantes inicialmente vazia


    async def setup(self):
        print(f"Hospital Agent {self.jid} está ativo")
        hospital_behaviour_registar = HospitalBehaviour_registo()
        hospital_behaviour_registarRecetor = HospitalReceiveRecetorBehaviour()
        hospital_behaviour_periodic = HospitalPeriodicBehaviour(period=30)
        self.add_behaviour(hospital_behaviour_registar)
        self.add_behaviour(hospital_behaviour_registarRecetor)
        self.add_behaviour(hospital_behaviour_periodic)

    def add_recetor(self, recetor):
        self.lista_recetores.append(recetor)
        print(f"Recetor {recetor.jid_recetor} adicionado ao hospital {self.jid}. Total de recetores: {len(self.lista_recetores)}")

    def add_recetor_salvos(self, recetor):
        self.lista_recetores_salvos.append(recetor)



import jsonpickle
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour
from spade.message import Message
import asyncio
import random
from random import randrange
import time as time

from Trabalho_SI.Classes.ClassRecetor import Recetor
from Trabalho_SI.Classes.ClassHospital import Hospital


class TransplanteBehaviour_cyclic(CyclicBehaviour):
    hospitais_dic = {}  # {"jid_hospital": Classe Hospital}
    recetores_dic = {}  # [ {jid_hospital: LISTA DE PACIENTES NESSE HOSPITAL},  ...]
    transportes_dic = {}  # {jid transporte: Classe Transporte}
    orgao_recebido=None

    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            performative = msg.get_metadata("performative")
            # receber os Hospitals
            if performative == "registarOrgao":  # adiciona o Hospital ao dicionário de Hospitals
                print("Recebida mensagem do tipo 'registarOrgao'")
                if msg.body:
                    self.orgao_recebido = jsonpickle.decode(msg.body)

                    #pedir a lista ao Gestor
                    manager_jid = self.agent.get("manager_jid")
                    msg = Message(to=manager_jid)
                    msg.set_metadata("performative", "pedirPacientes")  # Tipo da mensagem
                    msg.body = "pedir pacientes"
                    await self.send(msg)

            if performative == "informPacientes":  # adiciona o Hospital ao dicionário de Hospitals
                print("Recebida mensagem do tipo 'informPacientes'")
                if msg.body:
                    recetores_dic = jsonpickle.decode(msg.body)

                    #decidir quais pacientes são compatíveis

                    #informar o Gestor quais pacientes (TOP-3)
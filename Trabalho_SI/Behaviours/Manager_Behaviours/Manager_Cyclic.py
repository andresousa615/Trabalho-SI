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


class ManagerBehaviour_cyclic(CyclicBehaviour):
    hospitais_dic = {}  # {"jid_hospital": Classe Hospital}
    recetores_dic= {}  # [ {jid_hospital: LISTA DE PACIENTES NESSE HOSPITAL},  ...]
    transportes_dic = {} # {jid transporte: Classe Transporte}


 #   async def on_start(self):
#        manager_jid=self.agent.get("manager_jid")
        #print("manager_jid: ", manager_jid)

    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            #print("CHEGOU A MENSAGEM")
            performative = msg.get_metadata("performative")
            # receber os Hospitals
            if performative == "registarHospital":  # adicion o Hospital ao dicionario de Hospitals
                print("Recebida mensagem do tipo 'registerHospitals'")
                if msg.body:
                    hospital_recebido = jsonpickle.decode(msg.body)
                    hospital_jid = str(msg.sender)
                    #print("hosptial reecebido: ", hospital_recebido)
                    # Armazenar o objeto Hospital no dicionário, associado ao JID do agente
                    self.hospitais_dic[hospital_jid] = hospital_recebido

                    self.recetores_dic[hospital_jid] = hospital_recebido.get_listaRecetores()
                    print(f"Pacientes {self.recetores_dic[hospital_jid]} do hospital {hospital_jid}")


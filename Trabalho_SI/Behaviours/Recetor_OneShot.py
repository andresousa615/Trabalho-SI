import jsonpickle
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour, OneShotBehaviour
from Trabalho_SI.Classes.ClassRecetor import Recetor
from spade.message import Message
import asyncio
import random
from random import randrange
from Trabalho_SI.Classes.ClassHospital import Hospital


class RecetorBehaviour_registo(OneShotBehaviour): #envia uma mensagem para registar 1 Taxi no Manager
    async def run(self):
        lista_urgencia=['Pouco Urgente','Medio Urgente','Muito Urgente','Emergencia']
        lista_tipo_sangue = ['A', 'B', 'AB', 'O-', 'O+']
        lista_orgaos= ['coracao','figado','rim']
        #coordenadas de onde o Taxi vai spawnar
        x = randrange(0, 3)
        y = randrange(0, 2)
        z = randrange(0, 2)
        urgencia=lista_urgencia[x]
        sangue= lista_tipo_sangue[y]
        orgao = lista_orgaos[z]
        jid_recetor = str(self.agent.jid)
        recetor= Recetor(jid_recetor,urgencia,sangue,orgao,False)

        # Obter a lista de hospitais
        hospital_jids = self.get("hospital_jids")
        if not hospital_jids:
            print("Nenhum hospital disponível para registrar.")
            return

        # Escolher um hospital aleatoriamente
        hospital_jid = random.choice(hospital_jids)

        #print("Manager jid no hospital", manager_jid)
        msg = Message(to=hospital_jid)  # Definindo o JID do receptor (manager)
        msg.set_metadata("performative","registarRecetor")

        msg.body = jsonpickle.encode(recetor) # envia o objeto classe Taxi para o Manager
        await self.send(msg)
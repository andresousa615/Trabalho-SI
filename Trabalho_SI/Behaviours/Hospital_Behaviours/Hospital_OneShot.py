import jsonpickle
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour, OneShotBehaviour
from spade.message import Message
import asyncio
import random
from random import randrange
from Trabalho_SI.Classes.ClassHospital import Hospital


class HospitalBehaviour_registo(OneShotBehaviour): #envia uma mensagem para registar 1 Taxi no Manager

    async def run(self):

        #coordenadas de onde o Taxi vai spawnar
        x = randrange(1, 1000)
        y = randrange(1, 1000)
        listaRecetores=[]
        nr_equipas=randrange(1, 5)
        nr_salas= randrange(1, 5)
        hospital= Hospital(listaRecetores, x, y, nr_equipas, nr_salas)


        manager_jid= self.get("manager_jid")
        #print("Manager jid no hospital", manager_jid)
        msg = Message(to=manager_jid)  # Definindo o JID do receptor (manager)
        msg.set_metadata("performative","registarHospital")

        msg.body = jsonpickle.encode(hospital) # envia o objeto classe Taxi para o Manager
        await self.send(msg)

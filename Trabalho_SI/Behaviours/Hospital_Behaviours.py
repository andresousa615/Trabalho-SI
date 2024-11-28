import jsonpickle
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour, OneShotBehaviour
from spade.message import Message
import asyncio
import random
from random import randrange
from Trabalho_SI.Classes.ClassHospital import Hospital



class HospitalBehaviour_registo(OneShotBehaviour):
    async def run(self):
        # Obtem os atributos do hospital a partir do agente
        x = self.agent.x
        y = self.agent.y
        nr_equipas = self.agent.nr_equipas
        nr_salas = self.agent.nr_salas
        lista_recetores = self.agent.lista_recetores

        # Cria um objeto da classe Hospital
        hospital = Hospital(lista_recetores, x, y, nr_equipas, nr_salas)

        # Recupera o JID do gestor a partir do agente
        manager_jid = self.agent.get("manager_jid")

        # Cria a mensagem para o gestor
        msg = Message(to=manager_jid)
        msg.set_metadata("performative", "registarHospital")  # Tipo da mensagem
        msg.body = jsonpickle.encode(hospital)  # Envia o objeto hospital serializado

        # Envia a mensagem
        await self.send(msg)
        #print(f"Hospital {self.agent.jid} registado com o gestor. Detalhes: Coordenadas ({x}, {y}), Equipas: {nr_equipas}, Salas: {nr_salas}")




class HospitalReceiveRecetorBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)  # Aguarda mensagens
        if msg:
            performative = msg.get_metadata("performative")
            if performative == "registarRecetor":
                print(f"Mensagem recebida para registar recetor no hospital {self.agent.jid}")
                if msg.body:
                    recetor_recebido = jsonpickle.decode(msg.body)  # Decodifica o objeto Recetor
                    self.agent.add_recetor(recetor_recebido)


                    #Atualizar as informações no Manager
                    manager_jid = self.agent.get("manager_jid")
                    x = self.agent.x
                    y = self.agent.y
                    nr_equipas = self.agent.nr_equipas
                    nr_salas = self.agent.nr_salas
                    lista_recetores = self.agent.lista_recetores
                    hospital = Hospital(lista_recetores, x, y, nr_equipas, nr_salas)

                    # Cria a mensagem para o gestor
                    msg = Message(to=manager_jid)
                    msg.set_metadata("performative", "atualizarHospital")  # Tipo da mensagem
                    msg.body = jsonpickle.encode(hospital)  # Envia o objeto hospital serializado

                    # Envia a mensagem
                    await self.send(msg)




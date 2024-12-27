import asyncio
from asyncio import sleep
from datetime import time
from random import randrange
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
import jsonpickle
import random
from Trabalho_SI.Classes.ClassTransporte import *
from Trabalho_SI.Functions.transporte_functions import *


class TransporteBehaviour_registo(OneShotBehaviour):  # Envia uma mensagem para registar um transporte no Manager
    async def run(self):

        criar_heli = self.agent.get("helicopetro")

        if criar_heli==1:
            tipo_transporte = 'Helicóptero'
            coordenada_x = random.randint(0, 1000)  # Coordenada X aleatória
            coordenada_y = random.randint(0, 1000)  # Coordenada Y aleatória
            disponibilidade = True

            transporte = Transporte(tipo_transporte, coordenada_x, coordenada_y, disponibilidade)

            transplante_jid = self.agent.get("transplante_jid")
            msg = Message(to=transplante_jid)  # Definindo o JID do manager
            msg.set_metadata("performative", "registarTransporte")

            # Serializar o objeto transporte para enviar
            msg.body = jsonpickle.encode(transporte)
            await self.send(msg)
            print(f"Mensagem enviada para registrar transporte: {transporte}")

        else:
            lista_tipo_transporte = ['Ambulância', 'Carro INEM', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Carro INEM','Carro INEM','Carro INEM','Carro INEM','Carro INEM']
            # Coordenadas de onde o transporte vai spawnar
            i = randrange(0, 14)
            disponibilidade = True  # O transporte pode estar disponível ou não

            tipo_transporte = lista_tipo_transporte[i]
            coordenada_x = random.randint(0, 1000)  # Coordenada X aleatória
            coordenada_y = random.randint(0, 1000)  # Coordenada Y aleatória

            transporte = Transporte(tipo_transporte, coordenada_x, coordenada_y, disponibilidade)

            transplante_jid = self.agent.get("transplante_jid")
            msg = Message(to=transplante_jid)  # Definindo o JID do manager
            msg.set_metadata("performative", "registarTransporte")

            # Serializar o objeto transporte para enviar
            msg.body = jsonpickle.encode(transporte)
            await self.send(msg)

            print(f"Mensagem enviada para registrar transporte: {transporte}")

class TransporteBehaviour_cyclic(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            performative = msg.get_metadata("performative")

            if performative == "iniciarViagem":  # adiciona o Hospital ao dicionário de Hospitals
                print("Recebida mensagem do tipo 'iniciarViagem'")
                if msg.body:
                    transplante_jid = str(msg.sender)

                    dic_transplante = jsonpickle.decode(msg.body)
                    recetor=dic_transplante["recetor"]
                    orgao=dic_transplante["orgao"]
                    hospital_jid = dic_transplante["hospital"][0]
                    hospital = dic_transplante["hospital"][1]
                    transporte=dic_transplante["transporte"]

                    distancia_orgao_transporte=calcular_distancia(orgao.get_x(), orgao.get_y(), transporte.get_x(), transporte.get_y())
                    distancia_orgao_hospital = calcular_distancia(orgao.get_x(), orgao.get_y(), hospital.get_coordenada_x(), hospital.get_coordenada_y())
                    distancia_total= distancia_orgao_transporte+distancia_orgao_hospital

                    tipo_transporte= transporte.get_tipo_transporte()
                    if tipo_transporte=="Ambulância":
                        time = distancia_total / 300
                        print(f'Tempo de viagem: {time}')
                        await asyncio.sleep(time)
                    elif tipo_transporte=="Carro INEM":
                        time=distancia_total / 400
                        print(f'Tempo de viagem: {time}')
                        await asyncio.sleep(time)
                    elif tipo_transporte=="Helicóptero":
                        time=distancia_total / 800
                        print(f'Tempo de viagem: {time}')
                        await asyncio.sleep(time)

                    hospital_msg = Message(to=hospital_jid)
                    hospital_msg.set_metadata("performative", "orgaoEntregue")
                    hospital_msg.body = jsonpickle.encode(recetor)
                    await self.send(hospital_msg)

                    transplante_msg = Message(to=transplante_jid)
                    transplante_msg.set_metadata("performative", "viagemConcluida")
                    transplante_msg.body = jsonpickle.encode(hospital)
                    await self.send(transplante_msg)



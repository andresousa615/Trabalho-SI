from random import randrange
from spade.behaviour import OneShotBehaviour
from spade.message import Message
import jsonpickle
import random
from Trabalho_SI.Classes.ClassTransporte import *

class TransporteBehaviour_registo(OneShotBehaviour):  # Envia uma mensagem para registar um transporte no Manager
    async def run(self):
        lista_tipo_transporte = ['Ambulância', 'Helicóptero', 'Carro INEM', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Ambulância', 'Carro INEM','Carro INEM','Carro INEM','Carro INEM','Carro INEM']
        # Coordenadas de onde o transporte vai spawnar
        i = randrange(0, 15)
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

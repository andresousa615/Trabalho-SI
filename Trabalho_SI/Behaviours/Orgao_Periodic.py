import jsonpickle
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour, OneShotBehaviour
from Trabalho_SI.Classes.ClassOrgao import *
from spade.message import Message
import asyncio
import random
from random import randrange
from Trabalho_SI.Classes.ClassHospital import Hospital


class OrgaoBehaviour_gerarOrgao(PeriodicBehaviour): #envia uma mensagem para registar 1 Orgao no Transplante
    async def run(self):

        lista_tipo_sangue = ['A+','A-', 'B+','B-', 'AB+','AB-', 'O-', 'O+']
        lista_orgaos= ['coracao','figado','rim']

        #coordenadas de onde o Taxi vai spawnar
        coordenada_x = random.randint(0, 1000)  # Coordenada X aleatória
        coordenada_y = random.randint(0, 1000)

        sangue_index = randrange(0, 8)
        orgao_index = randrange(0, 3)

        sangue= lista_tipo_sangue[sangue_index]
        orgao = lista_orgaos[orgao_index]

        validade_orgao=random.randint(500, 1000)


        jid_orgao = str(self.agent.jid)

        objeto_orgao = Orgao(jid_orgao, sangue, orgao,  coordenada_x, coordenada_y, validade_orgao)

        #Registar no AgentTransplante
        transplante_jid = self.agent.get("transplante_jid")
        msg = Message(to=transplante_jid)

        msg.set_metadata("performative","registarOrgao")

        msg.body = jsonpickle.encode(objeto_orgao) # envia o objeto classe Taxi para o Manager
        await self.send(msg)

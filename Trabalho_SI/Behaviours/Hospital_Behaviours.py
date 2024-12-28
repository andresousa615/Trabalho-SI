import jsonpickle
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour, OneShotBehaviour
from spade.message import Message
import asyncio
import random
from random import randrange
from Trabalho_SI.Classes.ClassHospital import Hospital

from colorama import Fore, Back, Style, init
init(autoreset=True)

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
        transplante_jid = self.agent.get("transplante_jid")

        # Cria a mensagem para o gestor
        msg = Message(to=transplante_jid)
        msg.set_metadata("performative", "registarHospital")  # Tipo da mensagem
        msg.body = jsonpickle.encode(hospital)  # Envia o objeto hospital serializado

        # Envia a mensagem
        await self.send(msg)
        #print(f"Hospital {self.agent.jid} registado com o gestor. Detalhes: Coordenadas ({x}, {y}), Equipas: {nr_equipas}, Salas: {nr_salas}")

class HospitalPeriodicBehaviour(PeriodicBehaviour): #envia uma mensagem para registar 1 Orgao no Transplante
    async def run(self):
        print(f"Lista de Recetores que já sofreram transplante no Hospital {self.agent.jid}:")
        for recetor in self.agent.lista_recetores_salvos:
            print(recetor)
        print("\n")



class HospitalReceiveBehaviour(CyclicBehaviour):
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
                    transplante_jid = self.agent.get("transplante_jid")
                    x = self.agent.x
                    y = self.agent.y
                    nr_equipas = self.agent.nr_equipas
                    nr_salas = self.agent.nr_salas
                    lista_recetores = self.agent.lista_recetores
                    hospital = Hospital(lista_recetores, x, y, nr_equipas, nr_salas)

                    # Cria a mensagem para o gestor
                    msg = Message(to=transplante_jid)
                    msg.set_metadata("performative", "atualizarHospital")  # Tipo da mensagem
                    msg.body = jsonpickle.encode(hospital)  # Envia o objeto hospital serializado

                    # Envia a mensagem
                    await self.send(msg)

            if performative == "orgaoAtribuido":
                #print(f"Mensagem recebida para atualizar recetor no hospital - orgaoAtribuido")
                if msg.body:

                    recetor_recebido = jsonpickle.decode(msg.body)  # Decodifica o objeto Recetor
                    #print(f'recetor_Recebido {recetor_recebido}.')
                    lista_recetores = self.agent.lista_recetores
                    recetor_encontrado=False
                    for recetor in lista_recetores:
                        if recetor.get_jid_recetor()==recetor_recebido.get_jid_recetor():
                            recetor.set_orgao_atribuido(True)
                            #print(f'Recetor atualizado: {recetor}')
                            recetor_encontrado=True
                    if not recetor_encontrado:
                            print("NÃO ENCONTROU O RECETOR NESTE HOSPITAL")


                    '''for recetor in self.agent.lista_recetores:
                        print(f'Recetor HOSP: {recetor}')'''

            if performative == "orgaoEntregue":
                #print(f"Orgao Recebido para um Recetor - orgaoEntregue")
                if msg.body:

                    recetor_recebido = jsonpickle.decode(msg.body)  # Decodifica o objeto Recetor

                    print(f'Orgão entregue ao Recetor {recetor_recebido.get_jid_recetor()} que vai realizar o transplante, no Hospital {self.agent.jid}.')

                    self.agent.nr_equipas-=1
                    self.agent.nr_salas-=1

                    lista_recetores = self.agent.lista_recetores
                    recetor_encontrado=False
                    for recetor in lista_recetores:
                        if recetor.get_jid_recetor()==recetor_recebido.get_jid_recetor():
                            self.agent.lista_recetores.remove(recetor)
                            recetor_encontrado=True

                    if not recetor_encontrado:
                        print("Não encontrou o recetor")

                    transplante_jid = self.agent.get("transplante_jid")
                    x = self.agent.x
                    y = self.agent.y
                    nr_equipas = self.agent.nr_equipas
                    nr_salas = self.agent.nr_salas
                    lista_recetores = self.agent.lista_recetores
                    hospital = Hospital(lista_recetores, x, y, nr_equipas, nr_salas)

                    # Cria a mensagem para o agente transplante
                    msg = Message(to=transplante_jid)
                    msg.set_metadata("performative", "atualizarHospital")
                    msg.body = jsonpickle.encode(hospital)  # Envia o objeto hospital serializado

                    # Envia a mensagem
                    await self.send(msg)

                    print(Fore.BLUE +f"Operação de transplante ao Recetor {recetor_recebido.get_jid_recetor()} iniciada.")
                    await asyncio.sleep(5) #tempo até as equipas/salas voltarem a estar disponíveis
                    #mata-se o agente recetor e o orgão(?)




                    print(Fore.BLUE +f"Operação de transplante ao Recetor {recetor_recebido.get_jid_recetor()} Concluída com Sucesso.")
                    self.agent.add_recetor_salvos(recetor_recebido) #adiciona o recetor à lista do dos agentes Recetor salvos

                    self.agent.nr_equipas += 1
                    self.agent.nr_salas += 1

                    x = self.agent.x
                    y = self.agent.y
                    nr_equipas = self.agent.nr_equipas
                    nr_salas = self.agent.nr_salas
                    lista_recetores = self.agent.lista_recetores
                    hospital = Hospital(lista_recetores, x, y, nr_equipas, nr_salas)

                    # Cria a mensagem para o agente transplante
                    msg = Message(to=transplante_jid)
                    msg.set_metadata("performative", "atualizarHospital")
                    msg.body = jsonpickle.encode(hospital)  # Envia o objeto hospital serializado

                    # Envia a mensagem
                    await self.send(msg)






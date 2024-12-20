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
from Trabalho_SI.Functions.transplante_functions import *

class TransplanteBehaviour_cyclic(CyclicBehaviour):
    hospitais_dic = {}  # {"jid_hospital": Classe Hospital}
    recetores_dic = {}  # [ {jid_hospital: LISTA DE PACIENTES NESSE HOSPITAL},  ...]
    transportes_dic = {}  # {jid transporte: Classe Transporte}
    orgao_recebido = None

    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            performative = msg.get_metadata("performative")
            # receber os Hospitals
            if performative == "registarHospital":  # adiciona o Hospital ao dicionário de Hospitals
                print("Recebida mensagem do tipo 'registarHospital'")
                if msg.body:
                    hospital_recebido = jsonpickle.decode(msg.body)
                    hospital_jid = str(msg.sender)
                    # Armazenar o objeto Hospital no dicionário, associado ao JID do agente
                    self.hospitais_dic[hospital_jid] = hospital_recebido
                    self.recetores_dic[hospital_jid] = hospital_recebido.get_listaRecetores()
                    #print(f"JID: {hospital_jid}, objeto Hospital: {hospital_recebido}")  # Aqui imprime o Hospital de forma legível

            if performative == "atualizarHospital":  # Atualiza o Hospital no dicionário
                #print("Recebida mensagem do tipo 'atualizarHospital'")
                if msg.body:
                    hospital_recebido = jsonpickle.decode(msg.body)
                    hospital_jid = str(msg.sender)
                    self.hospitais_dic[hospital_jid] = hospital_recebido
                    self.recetores_dic[hospital_jid] = hospital_recebido.get_listaRecetores()
                    #print(f"JID: {hospital_jid}, objeto Hospital: {hospital_recebido}")  # Aqui imprime o Hospital de forma legível

            if performative == "registarTransporte":  # adiciona o Hospital ao dicionário de Hospitals
                #print("Recebida mensagem do tipo 'registarTransporte'")
                if msg.body:
                    transporte_recebido = jsonpickle.decode(msg.body)
                    transporte_jid = str(msg.sender)
                    # Armazenar o objeto Hospital no dicionário, associado ao JID do agente
                    self.transportes_dic[transporte_jid] = transporte_recebido
                    #print(f"JID: {transporte_jid}, objeto Hospital: {transporte_recebido}")  # Aqui imprime o Hospital de forma legível

            if performative == "registarOrgao":  # adiciona o Hospital ao dicionário de Hospitals
                print("Recebida mensagem do tipo 'registarOrgao'")
                if msg.body:
                    self.orgao_recebido = jsonpickle.decode(msg.body)
                    print(f"Orgão recebido: {self.orgao_recebido}")

                    #ir ver à lista de recetores que pacientes são compatíveis com o orgão e ordenar por ordem de prioridade

                    # Lista para armazenar recetores compatíveis
                    todos_recetores = []
                    for recetores in self.recetores_dic.values():
                        todos_recetores.extend(recetores)

                    # Determinar recetores compatíveis
                    recetores_compatíveis = determinar_recetores_compativeis(self.orgao_recebido, todos_recetores)

                    # Exibir recetores compatíveis
                    if recetores_compatíveis:
                        print("Recetores compatíveis (ordenados por prioridade):")
                        for recetor in recetores_compatíveis:
                            print(f"- {recetor}")
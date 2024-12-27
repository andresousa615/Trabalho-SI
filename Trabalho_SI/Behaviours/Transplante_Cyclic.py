import jsonpickle
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour
from spade.message import Message
import asyncio
import random
from random import randrange
import time as time

from colorama import Fore, Back, Style, init
init(autoreset=True)

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
                #print("Recebida mensagem do tipo 'registarHospital'")
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
                    recetores_compativeis = determinar_recetores_compativeis(self.orgao_recebido, todos_recetores) #dá print dos recetores possíveis, e determina os compatíveis
                    print('\n')
                    # Exibir recetores compatíveis
                    if recetores_compativeis:
                        print(Fore.GREEN + "Recetores compatíveis (ordenados por prioridade):")
                        for recetor in recetores_compativeis:
                            print(f"- {recetor}")
                        print('\n')

                        selecao = determinar_recetor_transporte(recetores_compativeis, self.orgao_recebido, self.recetores_dic, self.hospitais_dic, self.transportes_dic)
                        #selecao = {'recetor_selecionado': recetor_em_causa, 'transporte': transporte_selecionado_jid}
                        if selecao:
                            recetor_selecionado=selecao['recetor_selecionado']

                            hospital_jid = None
                            for jid_hospital, recetores in self.recetores_dic.items():
                                if recetor_selecionado in recetores:
                                    hospital_jid = jid_hospital
                                    for recetor in self.recetores_dic[hospital_jid]:
                                        if recetor_selecionado == recetor:
                                            recetor.set_orgao_atribuido(True)
                                            print(Fore.GREEN + f"Orgão {self.orgao_recebido.get_jid_orgao()} - {self.orgao_recebido.get_nome_orgao()}, atribuído ao Recetor {recetor.get_jid_recetor()}")
                                            break

                            hospital_msg = Message(to=hospital_jid)
                            hospital_msg.set_metadata("performative", "orgaoAtribuido")
                            hospital_msg.body = jsonpickle.encode(recetor_selecionado)
                            await self.send(hospital_msg)

                            '''for recetor in self.recetores_dic[hospital_jid]:
                                print(f'Recetor TRANS: {recetor}')'''

                            #PASSO SEGUINTE INFORMAR O TRANSPORTE
                            jid_transporte_selecionado = selecao['transporte']

                            self.transportes_dic[jid_transporte_selecionado].set_disponibilidade(False) #coloca a disponibilidade do transporte a falso

                            transporte_msg = Message(to=jid_transporte_selecionado)
                            transporte_msg.set_metadata("performative", "iniciarViagem")

                            dic_transplante={"recetor": recetor_selecionado, "orgao": self.orgao_recebido, "hospital": (hospital_jid,self.hospitais_dic[hospital_jid]), "transporte": self.transportes_dic[jid_transporte_selecionado] }

                            transporte_msg.body = jsonpickle.encode(dic_transplante)

                            await self.send(transporte_msg)

                    else:
                        print("Não existe nenhum recetor compatível com este orgão.")

                            #depois inf hospital, e hospital informar o transplante, timer no hopsital e cenas

            if performative == "viagemConcluida":  # adiciona o Hospital ao dicionário de Hospitals
                # print("Recebida mensagem do tipo 'registarTransporte'")
                if msg.body:
                    transporte_jid = str(msg.sender)
                    hospital_recebido = jsonpickle.decode(msg.body)

                    #torna o veículo novamente disponível
                    self.transportes_dic[transporte_jid].set_disponibilidade(True)

                    #atualiza as coordenadas do veículo
                    self.transportes_dic[transporte_jid].set_x(hospital_recebido.get_coordenada_x())
                    self.transportes_dic[transporte_jid].set_y(hospital_recebido.get_coordenada_y())

                    #print(f'Hospital aonde foi o veículo: {hospital_recebido}')
                    print(Fore.GREEN + f'Veículo novamente disponível: {self.transportes_dic[transporte_jid]}')







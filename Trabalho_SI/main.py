from Agentes.AgentHospital import AgentHospital
from Agentes.AgentRecetor import AgentRecetor
from Agentes.AgentTransporte import AgentTransporte
from Agentes.AgentOrgao import AgentOrgao
from spade import quit_spade
import asyncio
from random import randrange

from Trabalho_SI.Agentes.AgentTransplante import AgentTransplante

if __name__ == "__main__":

    transplante_jid = "manager@laptop-hjqmpgkj"  #laptop-hjqmpgkj
    transplante_password = "NOPASSWORD"

    # Inicializando o agente Gestor
    transplante_agent = AgentTransplante(transplante_jid, transplante_password)
    future = transplante_agent.start()
    future.result()

    hospital_jids = []

    # Inicializando o agente Hospital
    for i in range(5): #ele cria 5 instÂncias diferentes, mas tem todas o mesmo jid, o que vai ser chato para depois tentar conversar com um taxi em específico

        hospital_jid = f"hospital{i}@laptop-hjqmpgkj"
        hospital_jids.append(hospital_jid)
        hospital_password = "NOPASSWORD"
        x, y = randrange(1, 1000), randrange(1, 1000)
        nr_equipas = randrange(1, 5)
        nr_salas = randrange(1, 5)

        hospital_agent = AgentHospital(hospital_jid, hospital_password, x, y, nr_equipas, nr_salas)
        hospital_agent.set("transplante_jid", transplante_jid)
        future = hospital_agent.start()
        future.result()

    # Inicializando os agentes Transportes
    for i in range(10):  # ele cria 5 instÂncias diferentes, mas tem todas o mesmo jid, o que vai ser chato para depois tentar conversar com um taxi em específico

        transporte_jid = f"transporte{i}@laptop-hjqmpgkj"
        transporte_password = "NOPASSWORD"
        transporte_agent = AgentTransporte(transporte_jid, transporte_password)
        transporte_agent.set("transplante_jid", transplante_jid)
        future = transporte_agent.start()
        future.result()

    orgao_jid = "orgao@laptop-hjqmpgkj"  #
    orgao_password = "NOPASSWORD"

    # Inicializando o agente Orgao
    orgao_agent = AgentOrgao(orgao_jid, orgao_password)
    orgao_agent.set("transplante_jid", transplante_jid)
    future = orgao_agent.start()
    future.result()

    async def create_recetor_agents(hospital_jids):
        a=0
        while a < 50:
            for i in range(a,a+5):
                recetor_jid = "recetor" + str(i) + "@laptop-hjqmpgkj"
                recetor_password = "NOPASSWORD"
                recetor_agent = AgentRecetor(recetor_jid, recetor_password)
                recetor_agent.set("transplante_jid", transplante_jid)
                recetor_agent.set("hospital_jids", hospital_jids)
                future = recetor_agent.start()
                future.result()

            # Espera 5 segundos antes de criar os próximos clientes
            await asyncio.sleep(10)
            a += 10

    try:
        asyncio.run(create_recetor_agents(hospital_jids))
        asyncio.run(asyncio.sleep(1000))  # Tempo suficiente para interagir
    finally:
        # Parar os agentes de forma segura
        transplante_agent.stop()
        hospital_agent.stop()
        #recetor_agent.stop()


    # Finalizar SPADE
    quit_spade()
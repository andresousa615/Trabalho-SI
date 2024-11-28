from Agentes.AgentManager import AgentManager
from Agentes.AgentHospital import AgentHospital
from spade import quit_spade
import asyncio
from random import randrange

from Trabalho_SI.Agentes.AgentManager import AgentManager

if __name__ == "__main__":

    manager_jid = "manager@laptop-hjqmpgkj.mshome.net"  #
    manager_password = "NOPASSWORD"

    # Inicializando o agente Gestor
    manager_agent = AgentManager(manager_jid, manager_password)
    future = manager_agent.start()
    future.result()

    # Inicializando o agente Taxi
    for i in range(5): #ele cria 5 instÂncias diferentes, mas tem todas o mesmo jid, o que vai ser chato para depois tentar conversar com um taxi em específico

        hospital_jid = "hospital"+str(i)+"@laptop-hjqmpgkj.mshome.net"
        hospital_password = "NOPASSWORD"

        hospital_agent = AgentHospital(hospital_jid, hospital_password)
        hospital_agent.set("manager_jid", manager_jid)
        future = hospital_agent.start()
        future.result()


    try:
        asyncio.run(asyncio.sleep(1000))  # Tempo suficiente para interagir
    finally:
        # Parar os agentes de forma segura
        manager_agent.stop()
        hospital_agent.stop()


    # Finalizar SPADE
    quit_spade()
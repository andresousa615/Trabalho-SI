import time

from Trabalho_SI.Behaviours.Orgao_Periodic import *


# Receiver Agent: Recebe mensagens e as imprime
class AgentOrgao(agent.Agent):

    def __init__(self, jid, password):
        super().__init__(jid, password)

    async def setup(self):
        time.sleep(3) #dá tempo de serem criados recetores
        print(f"Agente Orgao {self.jid} inicializado.")
        orgao_behaviour_periodic = OrgaoBehaviour_gerarOrgao(period=5)
        self.add_behaviour(orgao_behaviour_periodic)

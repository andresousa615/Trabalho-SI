from spade.agent import Agent
from spade import agent
from Trabalho_SI.Behaviours.Manager_Behaviours import *
from Trabalho_SI.Behaviours.Manager_Behaviours.Manager_Cyclic import ManagerBehaviour_cyclic


# Receiver Agent: Recebe mensagens e as imprime
class AgentManager(agent.Agent):

    def __init__(self, jid, password):
        super().__init__(jid, password)

    async def setup(self):
        print(f"Manager Agent {self.jid} está ativo")
        manager_behaviour_cyclic = ManagerBehaviour_cyclic()
        self.add_behaviour(manager_behaviour_cyclic)
   
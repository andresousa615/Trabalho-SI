from spade import agent
from Trabalho_SI.Behaviours.Manager_Cyclic import ManagerBehaviour_cyclic


# Receiver Agent: Recebe mensagens e as imprime
class AgentTransplante(agent.Agent):

    def __init__(self, jid, password):
        super().__init__(jid, password)

    async def setup(self):
        print(f"Agente Transplante {self.jid} está ativo")
        transplante_behaviour_cyclic = ()
        self.add_behaviour(transplante_behaviour_cyclic)

from Trabalho_SI.Behaviours.Transporte_Behaviours import *
from spade import agent


class AgentTransporte(agent.Agent):

    def __init__(self, jid, password):
        super().__init__(jid, password)

    async def setup(self):
        print(f"Agente Transporte {self.jid} inicializado.")
        transporte_behaviour_oneshot = TransporteBehaviour_registo()
        transporte_behaviour_cyclic = TransporteBehaviour_cyclic()
        self.add_behaviour(transporte_behaviour_oneshot)
        self.add_behaviour(transporte_behaviour_cyclic)

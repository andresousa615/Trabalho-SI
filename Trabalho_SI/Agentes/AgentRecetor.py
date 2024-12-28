from Trabalho_SI.Behaviours.Recetor_OneShot import *

class AgentRecetor(agent.Agent):

    def __init__(self, jid, password):
        super().__init__(jid, password)

    async def setup(self):
        recetor_behaviour_oneshot = RecetorBehaviour_registo()
        self.add_behaviour(recetor_behaviour_oneshot)



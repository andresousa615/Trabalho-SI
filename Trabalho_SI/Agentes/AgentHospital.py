from spade.agent import Agent
from spade import agent

from Trabalho_SI.Behaviours.Hospital_Behaviours.Hospital_OneShot import HospitalBehaviour_registo


class AgentHospital(agent.Agent):

    def __init__(self, jid, password):
        super().__init__(jid, password)


    async def setup(self):
        print(f"Hospital Agent {self.jid} está ativo")
        hospital_behaviour_registar = HospitalBehaviour_registo()
        self.add_behaviour(hospital_behaviour_registar)



class BaseAgent:
    def __init__(self, aid, name, agent_type):
        self.aid = aid
        self.name = name
        self.type = agent_type
        self.busy = False

    def work(self, task):
        raise NotImplementedError
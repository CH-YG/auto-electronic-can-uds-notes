import time
from .task import TaskStatus

class AgentScheduler:
    def __init__(self):
        self.agents = []
        self.tasks = []

    def register(self, agent):
        self.agents.append(agent)

    def add_task(self, task):
        self.tasks.append(task)

    def get_free_agent(self, agent_type):
        for a in self.agents:
            if a.type == agent_type and not a.busy:
                return a
        return None

    def run_once(self):
        pending = [t for t in self.tasks if t.status == TaskStatus.PENDING]
        for task in pending:
            agent = self.get_free_agent(task.agent_type)
            if agent:
                agent.busy = True
                task.status = TaskStatus.RUNNING
                agent.work(task)
                agent.busy = False
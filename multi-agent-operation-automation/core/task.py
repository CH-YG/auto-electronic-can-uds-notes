from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    PENDING = "待分配"
    RUNNING = "执行中"
    DONE = "已完成"

class Task:
    def __init__(self, tid, title, agent_type):
        self.tid = tid
        self.title = title
        self.agent_type = agent_type
        self.status = TaskStatus.PENDING
        self.result = ""
        self.create_time = datetime.now().strftime("%H:%M:%S")

    def finish(self):
        self.status = TaskStatus.DONE
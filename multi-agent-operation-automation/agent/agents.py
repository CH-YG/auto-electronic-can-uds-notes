from .base_agent import BaseAgent
import time

class DataAgent(BaseAgent):
    def work(self, task):
        time.sleep(0.5)
        task.result = "数据清洗完成"
        task.finish()

class OpAgent(BaseAgent):
    def work(self, task):
        time.sleep(0.5)
        task.result = "运营分析完成"
        task.finish()

class AutoAgent(BaseAgent):
    def work(self, task):
        time.sleep(0.5)
        task.result = "自动化流程执行完成"
        task.finish()

class NotifyAgent(BaseAgent):
    def work(self, task):
        time.sleep(0.5)
        task.result = "通知发送完成"
        task.finish()
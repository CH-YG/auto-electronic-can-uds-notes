from flask import Flask, render_template
from core.scheduler import AgentScheduler
from agent.agents import DataAgent, OpAgent, AutoAgent, NotifyAgent
from core.task import Task

app = Flask(__name__)

scheduler = AgentScheduler()
scheduler.register(DataAgent("D01", "数据处理员", "data"))
scheduler.register(OpAgent("O01", "运营分析师", "op"))
scheduler.register(AutoAgent("A01", "流程机器人", "auto"))
scheduler.register(NotifyAgent("N01", "消息推送员", "notify"))

scheduler.add_task(Task("T01", "用户行为数据清洗", "data"))
scheduler.add_task(Task("T02", "流量转化分析", "op"))
scheduler.add_task(Task("T03", "自动生成运营报表", "auto"))
scheduler.add_task(Task("T04", "推送日报给管理员", "notify"))

scheduler.run_once()

@app.route('/')
def index():
    return render_template('index.html', tasks=scheduler.tasks, agents=scheduler.agents)

if __name__ == '__main__':
    app.run(debug=True)
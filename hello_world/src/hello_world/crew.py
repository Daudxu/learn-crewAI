from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

# 如果你想在团队启动前或启动后运行一段代码，
# 你可以使用 @before_kickoff 和 @after_kickoff 装饰器
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@CrewBase
class HelloWorld():
    """你好世界团队"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # 了解更多关于YAML配置文件的信息：
    # 智能体: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # 任务: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # 如果你想为你的智能体添加工具，可以在这里了解更多：
    # https://docs.crewai.com/concepts/agents#agent-tools
    llm = LLM(
        model="gemini/gemini-1.5-pro-latest",
        api_key=GOOGLE_API_KEY,
        temperature=0.1,
    )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            llm=self.llm,
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
             llm=self.llm,
            verbose=True
        )

    # 要了解更多关于结构化任务输出、
    # 任务依赖关系和任务回调的信息，请查看文档：
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """创建你好世界团队"""
        # 要了解如何为你的团队添加知识源，请查看文档：
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # 由 @agent 装饰器自动创建
            tasks=self.tasks, # 由 @task 装饰器自动创建
            process=Process.sequential,
            chat_llm=self.llm,
            verbose=True,
            # process=Process.hierarchical, # 如果你想使用层级处理方式 https://docs.crewai.com/how-to/Hierarchical/
        )

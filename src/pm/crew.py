from crewai import Agent, LLM, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0
)

@CrewBase
class ProjectManagementCrew():
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config = self.agents_config["product_manager"],
            verbose = False,
            llm = llm,
            allow_delegation = False,
            tools = []
        )
    @agent
    def engineer(self) -> Agent:
        return Agent(
            config = self.agents_config["engineer"],
            verbose = False,
            llm = llm,
            allow_delegation = False,
            tools = []
        )
    @agent
    def designer(self) -> Agent:
        return Agent(
            config = self.agents_config["designer"],
            verbose = False,
            llm = llm,
            allow_delegation = False,
            tools = []
        )
    @agent
    def cpo(self) -> Agent:
        return Agent(
            config = self.agents_config["cpo"],
            verbose = False,
            llm = llm,
            allow_delegation = True,
            tools = []
        )
    
    @task
    def product_manager_task(self) -> Task:
        return Task(
            config=self.tasks_config["product_manager_task"],
            verbose=False,
        )
    @task
    def engineer_task(self) -> Task:
        return Task(
            config=self.tasks_config["engineer_task"],
            verbose=False,
        )
    @task
    def designer_task(self) -> Task:
        return Task(
            config=self.tasks_config["designer_task"],
            verbose=False,
        )
    @task
    def cpo_task(self) -> Task:
        return Task(
            config=self.tasks_config["cpo_task"],
            verbose=True,
        )
        
    @crew
    def crew(self) -> Crew:
     return Crew(
         agents=self.agents,
         tasks=self.tasks,
        # agents=[self.product_manager, self.engineer,
        #         self.designer, self.cpo],
        # tasks=[self.product_manager_task, self.engineer_task,
        #        self.designer_task, self.cpo_task],
        process=Process.sequential,
        verbose=True,
        memory= False, 
    )

import os
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI


os.environ["OPENAI_API_KEY"] = "sk-proj-111"

llm = ChatOpenAI(
    model= "ollama/deepseek-r1:7b",
    base_url= "http://localhost:11434/v1",
)


info_agent = Agent(
    role = "Information Agent",
    goal = "To provide information about a certain topic.",
    backstory = """
        You love to know information.  You win most of the quizzes at your local pub.
    """,
    llm = llm
)

task1 = Task(
    description = "Tell me all about Srinagar, Jammu and Kashmir",
    expected_output = "give me a quick summary and seven bullet points about Srinagar, Jammu and Kashmir",
    agent = info_agent,
    # crew = Crew(info_agent),
    # goal = "To provide information about the history of the United States.",
    # backstory = """
    #     You are tasked with providing information about the history of the United States.
    # """
)

crew = Crew(
    agents = [info_agent],
    tasks = [task1],
    verbose = True
)

result = crew.kickoff()

print("###############")
print(result)




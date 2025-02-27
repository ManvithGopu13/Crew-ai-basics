import os
from crewai import Agent, Task, Crew

info_agent = Agent(
    role = "Information Agent",
    goal = "To provide information about a certain topic.",
    backstory = """
        You love to know information.  You win most of the quizzes at your local pub.
    """
)

task1 = Task(
    description = "Tell me all about blue-ringed octopus",
    expected_output = "give me a quick summary and seven bullet points about the blue-ringed octopus",
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




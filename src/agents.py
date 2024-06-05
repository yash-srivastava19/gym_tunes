from langchain_cohere import ChatCohere
from composio_crewai import ComposioToolset, Action, App
 
class SchedulingTool:
    #@tool("schedule an event")
    def schedule_event(query):
        """ schedule things at your convenience """
        return ComposioToolset(apps=[App.GOOGLECALENDAR])

class SchedulingAgents():
    def __init__(self) -> None:
        pass 

    def schedule_event_agent(self, cohere_api_key):
        llm = ChatCohere(cohere_api_key= cohere_api_key, max_tokens=3000)
        tool_thing = SchedulingTool()
        return Agent(
            role="Google Calendar Agent",
            goal="You take action on Google Calendar using Google Calendar APIs",
            backstory="You are AI agent that is responsible for taking actions on Google Calendar on users behalf. You need to take action on Google Calendar using Google Calendar APIs",
            tools = tool_thing.schedule_event(),
            verbose=True,
            llm = llm
        )

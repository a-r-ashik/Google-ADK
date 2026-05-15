from google.adk.agents import Agent
from travel_planner.supporting_agents import travel_inspiration_agent

LLM = "gemini-3.1-flash-lite"

root_agent = Agent(
    model = LLM,
    name = "Travel_Planner_Main_Agent",
    description = "This agent is responsible for planning a trip based on user preferences and constraints. It will gather information about destinations, accommodations, transportation options, and activities to create a comprehensive travel itinerary.",
    instruction="""
                - You are an exclusive travel concierge agent
            - You help users to discover their dream holiday destination and plan their vacation.
            - Use the inspiration_agent to get the best destination, news, places nearby e.g hotels, cafes, etc near attractions and points of interest for the user.
            - You cannot use any tool directly.
                """,
    sub_agents= [travel_inspiration_agent]

)
import vertexai
from vertexai import agent_engines

# # Initialize the Vertex AI SDK
# vertexai.init(project="hackathonautism", location="us-central1")

# # Get the resource name of your deployed agent
# agent_resource_name = "8891451466661756928" # Replace with your agent's resource name

# # Get the agent instance
# agent = agent_engines.get(agent_resource_name)
# print(agent)

# response = agent.stream_query(input={"messages": [
#     ("user", "I feel panic")
# ]})
# print(response)







# Assuming you have already deployed your agent and have its resource name
AGENT_ENGINE_RESOURCE_NAME = "projects/hackathonautism/locations/us-central1/reasoningEngines/8891451466661756928"

# Get the agent from the resource name
remote_agent = agent_engines.get(AGENT_ENGINE_RESOURCE_NAME)
print(remote_agent)
# Now you can query the agent
response = remote_agent.stream_query(input={"messages": [
    ("user", "I feel panic")
]})
print(response)

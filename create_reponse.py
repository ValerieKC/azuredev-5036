# Before running the sample:
#    pip install --pre azure-ai-projects>=2.0.0b1
#    pip install azure-identity
import datetime
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

# https://learn.microsoft.com/en-us/azure/ai-foundry/reference/foundry-project-rest-preview?view=foundry&preserve-view=true
user_endpoint = "https://foundry-dev-isd-eus2.services.ai.azure.com/api/projects/default"

credential = DefaultAzureCredential()

project_client = AIProjectClient(
    endpoint=user_endpoint,
    credential=credential,
)

# agent_name = "button-component-test-agent"
# model_deployment_name = "gpt-4o"

# # Creates an agent version with require_approval set to never
# agent = project_client.agents.create_version(  
#     agent_name=agent_name,
#     definition=PromptAgentDefinition(
#         model=model_deployment_name,
#         instructions="Use only my knowledge to answer questions, don't use answers from your own knowledge. Don't hallucinate and never use your own knowledge to answer questions. Always use the knowledge I have added (button-kb).",
#         tools=[
#             {
#                 "type": "mcp",
#                 "server_label": "kb_kb_button_embedding_uabr3",
#                 "server_url": "https://asus-aocc-search-service.search.windows.net/knowledgebases/kb-button-embedding-002/mcp?api-version=2025-11-01-Preview",
#                 "project_connection_id": "kb-kb-button-embedding-uabr3",
#                 "require_approval": "never"
#             }
#         ]
#     ),
# )

print(f"Agent: {agent.name}")
print(f"Version: {agent.version}\n")

openai_client = project_client.get_openai_client()

# Reference the agent to get a response
response = openai_client.responses.create(
    input=[{"role": "user", "content": "How do I import the Button component in my React project?"}],
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")



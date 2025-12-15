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

# Get and log the access token
token = credential.get_token("https://ai.azure.com/.default")
print(f"Access Token: {token.token}")
print(f"Token expires on: {datetime.datetime.fromtimestamp(token.expires_on)}\n")

project_client = AIProjectClient(
    endpoint=user_endpoint,
    credential=credential,
)

agent_name = "test-agent"

openai_client = project_client.get_openai_client()

# Reference the agent to get a response
response = openai_client.responses.create(
    input=[{"role": "user", "content": "What is the cms api url?"}],
    extra_body={"agent": {"name": agent_name, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")



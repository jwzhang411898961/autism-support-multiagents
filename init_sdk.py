import vertexai
from vertexai import agent_engines

vertexai.init(
    project="gcpxmlb25",
    location="us-central1",
    staging_bucket="gs://speakease-agent",
)

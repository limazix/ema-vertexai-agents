"""This module is used to perform the agent deployment to the VertexAI platform.

Variables:
    remote_app (agent_engines.AgentEngine): The agent engine object.
"""

import os

import vertexai
from vertexai import agent_engines
from vertexai.agent_engines import AdkApp

from .agent import root_agent

app = AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

vertexai.init(
    project=os.getenv("PROJECT_ID"),
    location=os.getenv("PROJECT_LOCATION"),
    staging_bucket=os.getenv("GOOGLE_STORAGE_BUCKET"),
)

remote_app = agent_engines.create(
    display_name="electric-magnitudes-analyzer",
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]>=1.103.0",
        "google-generativeai>=0.8.5",
    ],
)

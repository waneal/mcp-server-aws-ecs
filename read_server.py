#\!/usr/bin/env python3
"""
AWS ECS MCP Server (Read-only version)
"""

import boto3
import os
from mcp.server.fastmcp import FastMCP

# Get AWS authentication credentials
aws_profile = os.environ.get("AWS_PROFILE")
aws_region = os.environ.get("AWS_REGION", "ap-northeast-1")  # Default is Tokyo region

# Create MCP server
mcp = FastMCP("AWS ECS Read-Only Server")

# Initialize ECS client
def get_ecs_client():
    session = boto3.Session(
        profile_name=aws_profile,
        region_name=aws_region
    )
    return session.client('ecs')

# Import tools from helpers
from src.read_tools import register_read_tools

# Register read-only tools
register_read_tools(mcp, get_ecs_client)

if __name__ == "__main__":
    mcp.run()

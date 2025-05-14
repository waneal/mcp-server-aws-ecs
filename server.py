#\!/usr/bin/env python3
"""
AWS ECS MCP Server (Full version with both read and write operations)
"""

import boto3
import os
from mcp.server.fastmcp import FastMCP

# Get AWS authentication credentials
aws_profile = os.environ.get("AWS_PROFILE")
aws_region = os.environ.get("AWS_REGION", "ap-northeast-1")  # Default is Tokyo region

# Create MCP server
mcp = FastMCP("AWS ECS Server")

# Initialize ECS client
def get_ecs_client():
    session = boto3.Session(
        profile_name=aws_profile,
        region_name=aws_region
    )
    return session.client('ecs')

# Import tools from helpers
from src.read_tools import register_read_tools
from src.write_tools import register_write_tools

# Register both read and write tools
register_read_tools(mcp, get_ecs_client)
register_write_tools(mcp, get_ecs_client)

if __name__ == "__main__":
    mcp.run()

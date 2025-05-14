#\!/usr/bin/env python3
"""
Start the AWS ECS Read-only MCP Server.
"""

from src.mcp_server_aws_ecs.servers.read_server import read_server

if __name__ == "__main__":
    read_server.run()

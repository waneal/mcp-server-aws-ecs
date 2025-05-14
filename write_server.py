#\!/usr/bin/env python3
"""
Start the AWS ECS Write MCP Server.
"""

from src.mcp_server_aws_ecs.servers.write_server import write_server

if __name__ == "__main__":
    write_server.run()

#\!/usr/bin/env python3
"""
Main entry point for the AWS ECS MCP Server.
This script runs the full server with both read and write capabilities.

For a read-only or write-only server, use the respective modules:
- src/mcp_server_aws_ecs/servers/read_server.py
- src/mcp_server_aws_ecs/servers/write_server.py
"""

from src.mcp_server_aws_ecs.servers.full_server import full_server

if __name__ == "__main__":
    # Run the full server (read + write operations)
    full_server.run()

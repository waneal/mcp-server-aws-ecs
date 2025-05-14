from mcp.server.fastmcp import FastMCP, Context
import os
from src.mcp_server_aws_ecs.read import register_read_tools
from src.mcp_server_aws_ecs.write import register_write_tools

# Create MCP server
mcp = FastMCP("AWS ECS MCP Server")

# Register read-only tools
register_read_tools(mcp)

# Register write tools
register_write_tools(mcp)

# Launch server
if __name__ == "__main__":
    mcp.run()

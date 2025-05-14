"""
Read-only MCP Server for AWS ECS operations.
"""

from mcp.server.fastmcp import FastMCP
from ..read import register_read_tools

def create_read_server(server_name: str = "AWS ECS Read-Only Server") -> FastMCP:
    """
    Create an MCP server for read-only AWS ECS operations.
    
    Args:
        server_name: Name of the MCP server (optional)
        
    Returns:
        FastMCP: Configured MCP server instance with read-only tools
    """
    # Create MCP server
    mcp = FastMCP(server_name)
    
    # Register read-only tools
    register_read_tools(mcp)
    
    return mcp

# Create default read-only server instance
read_server = create_read_server()

# Launch server when this script is run directly
if __name__ == "__main__":
    read_server.run()

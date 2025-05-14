"""
Full-featured MCP Server for AWS ECS operations (both read and write).
"""

from mcp.server.fastmcp import FastMCP
from ..read import register_read_tools
from ..write import register_write_tools

def create_full_server(server_name: str = "AWS ECS Full Server") -> FastMCP:
    """
    Create an MCP server with all AWS ECS operations (both read and write).
    
    Args:
        server_name: Name of the MCP server (optional)
        
    Returns:
        FastMCP: Configured MCP server instance with all tools
    """
    # Create MCP server
    mcp = FastMCP(server_name)
    
    # Register both read and write tools
    register_read_tools(mcp)
    register_write_tools(mcp)
    
    return mcp

# Create default full server instance
full_server = create_full_server()

# Launch server when this script is run directly
if __name__ == "__main__":
    full_server.run()

"""
Write-enabled MCP Server for AWS ECS operations.
"""

from mcp.server.fastmcp import FastMCP
from ..write import register_write_tools

def create_write_server(server_name: str = "AWS ECS Write Server") -> FastMCP:
    """
    Create an MCP server for write operations on AWS ECS.
    
    Args:
        server_name: Name of the MCP server (optional)
        
    Returns:
        FastMCP: Configured MCP server instance with write tools
    """
    # Create MCP server
    mcp = FastMCP(server_name)
    
    # Register write tools
    register_write_tools(mcp)
    
    return mcp

# Create default write server instance
write_server = create_write_server()

# Launch server when this script is run directly
if __name__ == "__main__":
    write_server.run()

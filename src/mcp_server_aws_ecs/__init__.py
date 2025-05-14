"""
MCP Server for AWS ECS operations.

This package provides MCP tools for interacting with AWS ECS services
through Claude Desktop, allowing both read-only and write operations.

Available server types:
- read_server: Read-only ECS operations
- write_server: Write operations (create, update, delete)
- full_server: Complete set of ECS operations
"""

from .read import register_read_tools
from .write import register_write_tools
from .servers.read_server import create_read_server, read_server
from .servers.write_server import create_write_server, write_server
from .servers.full_server import create_full_server, full_server

__all__ = [
    "register_read_tools", 
    "register_write_tools", 
    "create_read_server", 
    "read_server", 
    "create_write_server", 
    "write_server", 
    "create_full_server", 
    "full_server"
]

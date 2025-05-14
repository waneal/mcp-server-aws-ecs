"""
MCP Server for AWS ECS operations.

This package provides MCP tools for interacting with AWS ECS services
through Claude Desktop, allowing both read-only and write operations.
"""

from .read import register_read_tools
from .write import register_write_tools

__all__ = ["register_read_tools", "register_write_tools"]

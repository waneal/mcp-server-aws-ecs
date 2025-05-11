# AWS ECS MCP Server

<div align="center">

[![Python Version][python-badge]][python-url]
[![MCP SDK Version][mcp-badge]][mcp-url]

</div>

A Model Context Protocol (MCP) server for interacting with Amazon ECS (Elastic Container Service). This MCP server provides a set of tools that allow LLMs to list, describe, and manage ECS clusters, services, and tasks.

## Table of Contents

- [AWS ECS MCP Server](#aws-ecs-mcp-server)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Step 1: Clone the repository](#step-1-clone-the-repository)
    - [Step 2: Install uv (Python package manager)](#step-2-install-uv-python-package-manager)
    - [Step 3: Configure AWS credentials](#step-3-configure-aws-credentials)
  - [Usage](#usage)
    - [Running the server](#running-the-server)
    - [Using with Claude for Desktop](#using-with-claude-for-desktop)
      - [Troubleshooting](#troubleshooting)
  - [Available Tools](#available-tools)
  - [Configuration](#configuration)
  - [License](#license)

[python-badge]: https://img.shields.io/badge/python-3.11%2B-blue.svg
[python-url]: https://www.python.org/downloads/
[mcp-badge]: https://img.shields.io/badge/MCP%20SDK-1.8%2B-blue.svg
[mcp-url]: https://github.com/modelcontextprotocol/python-sdk

## Overview

This MCP server provides a bridge between Large Language Models (LLMs) and AWS ECS resources. It enables LLMs to query and interact with ECS clusters, services, tasks, and related resources using MCP tools. The server wraps the AWS boto3 ECS client API and exposes it through the MCP protocol.

## Prerequisites

- Python 3.11 or higher
- AWS account with ECS access
- AWS credentials configured locally
- Claude for Desktop (for integration with Claude)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/waneal/mcp-server-aws-ecs.git
cd mcp-server-aws-ecs
```

### Step 2: Install uv (Python package manager)

We recommend using [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver.

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

## Usage

### Running the server

You can run the server directly with uv:

```bash
export AWS_PROFILE=your-profile-name
export AWS_REGION=ap-northeast-1  # Optional, defaults to ap-northeast-1
uv run server.py
```

### Using with Claude for Desktop

To use this server with Claude for Desktop:

1. Manually configure Claude Desktop by editing your configuration file:

   - On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - On Windows: `%APPDATA%\Claude\claude_desktop_config.json`

   Create or edit the file to include the following:

   ```json
   {
     "mcpServers": {
       "aws-ecs": {
         "command": "uv",
         "args": [
           "--directory",
           "/ABSOLUTE/PATH/TO/mcp-server-aws-ecs",
           "run",
           "server.py"
         ],
         "env": {
           "AWS_PROFILE": "your-profile-name",
           "AWS_REGION": "ap-northeast-1"
         }
       }
     }
   }
   ```

   For Windows, use a path format like:
   ```json
   {
     "mcpServers": {
       "aws-ecs": {
         "command": "uv",
         "args": [
           "--directory",
           "C:\\ABSOLUTE\\PATH\\TO\\mcp-server-aws-ecs",
           "run",
           "server.py"
         ],
         "env": {
           "AWS_PROFILE": "your-profile-name",
           "AWS_REGION": "ap-northeast-1"
         }
       }
     }
   }
   ```

2. Restart Claude Desktop after saving the configuration file.

3. Verify the server is connected:
   - Look for the hammer icon 🔨 in the bottom right corner of the input box
   - Click on it to see the available AWS ECS tools
   - If tools are not showing up, check the troubleshooting section below

4. Start a new conversation in Claude Desktop, and the ECS tools will be available to Claude.

#### Troubleshooting

If your MCP server doesn't connect properly:

1. Restart Claude Desktop completely
2. Check your `claude_desktop_config.json` file syntax
3. Make sure the file paths are valid and absolute (not relative)
4. Check Claude's logs:
   - macOS: `~/Library/Logs/Claude/mcp*.log`
   - Windows: `%APPDATA%\Claude\logs\mcp*.log`
5. Try running the server manually to check for errors:
   ```bash
   cd /path/to/mcp-server-aws-ecs
   python server.py
   ```

## Available Tools

This server provides the following ECS tools:

- Cluster operations: `list_clusters`, `describe_clusters`
- Service operations: `list_services`, `describe_services`, `list_services_with_details`
- Task operations: `list_tasks`, `describe_tasks`, `get_task_protection`
- Container instance operations: `list_container_instances`, `describe_container_instances`
- Task definition operations: `list_task_definitions`, `list_task_definition_families`
- Capacity provider operations: `list_capacity_providers`, `describe_capacity_providers`, `get_cluster_capacity_providers`
- Deployment operations: `list_service_deployments`, `describe_service_deployments`, `describe_service_revisions`
- Miscellaneous: `list_account_settings`, `list_attributes`, `list_tags_for_resource`, `list_services_by_namespace`, `discover_poll_endpoint`

## Configuration

The server uses these environment variables that can be configured in the `env` section of the `claude_desktop_config.json` file:

- `AWS_PROFILE`: AWS profile name from your AWS credentials file
- `AWS_REGION`: AWS region (defaults to ap-northeast-1)
- `AWS_ACCESS_KEY_ID`: AWS access key (alternative to profile)
- `AWS_SECRET_ACCESS_KEY`: AWS secret key (alternative to profile)
- `AWS_SESSION_TOKEN`: AWS session token (if using temporary credentials)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

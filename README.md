# MCP Server Example

## Quick Start

### Prerequisites

- Python 3.11+
- [uvx](https://github.com/astral-sh/uv) installed on your system

### Installation with MCP Clients

#### Claude Desktop

Add this configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "demo": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/pree-dew/mcp-server-example.git",
        "mcp-server"
      ]
    }
  }
}
```

#### VS Code with GitHub Copilot

Add to your MCP settings:

```json
{
  "servers": {
    "demo": {
      "command": "uvx",
      "args": [
        "--from", 
        "git+https://github.com/pree-dew/mcp-server-example.git",
        "mcp-server"
      ]
    }
  }
}
```

#### Other MCP Clients

For any MCP-compatible client, use this server configuration:

```json
{
  "command": "uvx",
  "args": [
    "--from",
    "git+https://github.com/pree-dew/mcp-server-example.git", 
    "mcp-server"
  ]
}
```

### Using with uvx directly

You can also run the server directly for testing:

```bash
uvx --from git+https://github.com/pree-dew/mcp-server-example.git mcp-server
```


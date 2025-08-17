from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

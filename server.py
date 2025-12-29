from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MyFirstMCP")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def sumar(a: int, b: int) -> int:
    """Sumar dos numeros"""
    return a + b

@mcp.tool()
def restar(a: int, b: int) -> int:
    """Restar dos numeros"""
    return a - b

@mcp.tool()
def multiplicar(a: int, b: int) -> int:
    """Multiplicar dos numeros"""
    return a * b

@mcp.tool()
def dividir(a: int, b: int) -> int:
    """Dividir dos numeros"""
    return a / b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
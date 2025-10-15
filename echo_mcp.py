from fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("My Demo Server")

# Define a tool using the @mcp.tool decorator
@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

@mcp.tool
def echo(message: str) -> str:
    """Echoes the same message back."""
    return message

@mcp.tool
def uppercase(message: str) -> str:
    """Converts the message to uppercase."""
    return message.upper()

# Define a resource using the @mcp.resource decorator
@mcp.resource("greetings://{name}")
def personalized_greeting(name: str) -> str:
    """Generates a personalized greeting for the given name."""
    return f"Hello, {name}! Welcome to the MCP server."

# Run the server (e.g., using STDIO transport for local execution)
if __name__ == "__main__":
    print("FastMCP server starting... (Press Ctrl+C to stop)")
    mcp.run(transport="http", host="0.0.0.0", port=8000)

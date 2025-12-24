from typing import List
import random
import json
from fastmcp import FastMCP


mcp = FastMCP(name="Simple calculator server")


@mcp.tool
def add(a : int = 1 , b: int = 1    ) -> int :
    """Add two integers."""
    return a + b

@mcp.tool
def random(min:int =0, max:int =100) -> int:
    """Generate a random integer between min and max."""
    return random.randint(min, max)

@mcp.resource("info://server")
def info():
    """Return server information."""
    info= {
        "name": mcp.name,
        "version": "1.0.0",
        "description": "A test FastMCP server with basic tools."
    }
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)


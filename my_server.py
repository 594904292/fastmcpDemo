from fastmcp import FastMCP
from fastmcp import Context  

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool  
def add(a: int, b: int) -> int:  
    """Add two numbers and return the result"""  
    return a + b  

@mcp.tool  
def multiply(a: float, b: float) ->float:  
    """Multiply two numbers"""  
    return a*b


@mcp.resource("config://version")  
def get_version():  
     return "1.0.0"  
   
@mcp.resource("user://{user_id}/profile")  
def get_profile(user_id: int):  
     return {"name": f"User {user_id}", "status": "active"}


@mcp.tool  
async def summarize(uri: str, ctx: Context):  
    await ctx.info(f"Reading resource from {uri}")  
    data = await ctx.read_resource(uri)  
    summary = await ctx.sample(f"Summarize this: {data.content[:500]}")  
    return summary.text


if __name__ == "__main__":
    mcp.run()

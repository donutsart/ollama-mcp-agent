from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with configuration
mcp = FastMCP(
    "resource rate manager",  # Name of the MCP server
#    instructions="You are resource usage rate manager, can answer questions server resource usage rate of the requested app.",  # Instructions for the LLM on how to use this tool
    instructions="",
    host="0.0.0.0",  # Host address (0.0.0.0 allows connections from any IP)
    port=8007, # Port number for the server
)


@mcp.tool()
async def get_resource(service_name: str) -> str:
    """
    Get resource usage rate for specified app.

    Args:
        service_name (str): The name of the app  to get resource usage rate for

    Returns:
        str: A string containing the resource usage for the specified app
    """
    print(f"\n[DEBUG] MCP: service name called: {service_name}\n")
#    return f"{service_name} 의 자원 사용률은 50% 입니다."
    return f"{service_name} 앱 의 자원 사용률은 50% 이다."


if __name__ == "__main__":
    # Start the MCP server with stdio transport
    # stdio transport allows the server to communicate with clients
    # through standard input/output streams, making it suitable for
    # local development and testing
    mcp.run(transport="stdio")

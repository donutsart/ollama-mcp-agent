from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with configuration
mcp = FastMCP(
    "hadoop manager",  # Name of the MCP server
    instructions="You are a Hadoop system administrator and can stop the requested service and respond with its status.",  # Instructions for the LLM on how to use this tool
    host="0.0.0.0",  # Host address (0.0.0.0 allows connections from any IP)
    port=8008,  # Port number for the server
)


@mcp.tool()
async def status_hadoop_service(service_name: str ) -> tuple[str, str] :
    """
    get the status of a specified service in a Hadoop system.

    Args:
        service_name (str): Service name to check status

    Returns:
        tuple[str, str]: (service name, status)
    """
    print(f"\n[DEBUG] MCP: service name called: {service_name}\n")

    return service_name, "중지됨"


if __name__ == "__main__":
    # Start the MCP server with stdio transport
    # stdio transport allows the server to communicate with clients
    # through standard input/output streams, making it suitable for
    # local development and testing
    mcp.run(transport="stdio")

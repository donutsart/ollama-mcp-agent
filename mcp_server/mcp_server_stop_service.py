from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with configuration
mcp = FastMCP(
    "hadoop manager",  # Name of the MCP server
    instructions="You are a Hadoop system administrator and can stop the requested service and respond with its status.",  # Instructions for the LLM on how to use this tool
    host="0.0.0.0",  # Host address (0.0.0.0 allows connections from any IP)
    port=8009,  # Port number for the server
)


@mcp.tool()
async def stop_hadoop_service(service_name: str,  action: str) -> str:
    """
    Starts or stops a service on the Hadoop system.

    Args:
        service_name (str): Name of the service on the hadoop system to start or stop
        action (str): 'start' or 'stop'
    Returns:
        tuple[str, str]: (hadoop system name, service status)
    """
    print(f"\n[DEBUG] MCP: service name called: {service_name}\n")

    if action == "start":
        status_message = f"{service_name} is started"
    elif action == "stop":
        status_message = f"{service_name} is stopped"
    else:
        status_message = f"알 수 없는 동작: {action}. 'start' 또는 'stop'만 허용됩니다."

    return "hadoop", status_message


if __name__ == "__main__":
    # Start the MCP server with stdio transport
    # stdio transport allows the server to communicate with clients
    # through standard input/output streams, making it suitable for
    # local development and testing
    mcp.run(transport="stdio")

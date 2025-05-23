from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with configuration
mcp = FastMCP(
    "bdp manager",  # Name of the MCP server
    instructions="You are a BDP system administrator and can stop the requested service and respond with its status.",  # Instructions for the LLM on how to use this tool
    host="0.0.0.0",  # Host address (0.0.0.0 allows connections from any IP)
    port=8005,  # Port number for the server
)


@mcp.tool()
async def stop_service(service_name: str) -> tuple[str, str]:
    """
    Starts or stops a service on the bdp system.

    Args:
        service_name (str): Name of the service to start or stop

    Returns:
        tuple[str, str]: (bdp system name, service status)
    """
    print(f"\n[DEBUG] MCP: service name called: {service_name}\n\n\n\n")
    # return f"bdp 시스템에서 {service_name} 서비스를 중지 합니다.  중지된 상태가 되었습니다. "
    return "BDP", service_name


if __name__ == "__main__":
    # Start the MCP server with stdio transport
    # stdio transport allows the server to communicate with clients
    # through standard input/output streams, making it suitable for
    # local development and testing
    mcp.run(transport="stdio")

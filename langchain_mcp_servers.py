import asyncio
import os, sys, json
from contextlib import AsyncExitStack
from typing import Optional, List

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'content'):
            return {"type": o.__class__.__name__, "content": o.content}
        return super().default(o)


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_retries=2,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

#----------------------------------------------
# MCP Server Script Argument
#----------------------------------------------
if len(sys.argv) < 2:
    print("usage: python client.py <path_to_server>")
    sys.exit(1)

server_script = sys.argv[1]

#----------------------------------------------
# MCP Server Parameters
#----------------------------------------------
server_params = StdioServerParameters(
    command="python" if server_script.endswith(".py") else "node",
    args=[server_script],
)

MCP_Client = None


async def run_agent():
    global MCP_Client

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Store globally
            MCP_Client = type("MCPClientHolder", (), {"session": session})()

            tools = await load_mcp_tools(session)
            agent = create_agent(llm, tools)

            print("🚀 MCP CLIENT STARTED! Type 'quit' to exit.")

            while True:
                query = input("\nQuery: ").strip()
                if query.lower() == "quit":
                    break

                response = await agent.invoke({
                 "messages": [{"role": "user", "content": query}]
                })

                try:
                    formatted = json.dumps(response, indent=2, cls=CustomEncoder)
                except Exception:
                    formatted = str(response)

                print("\nResponse:")
                print(formatted)


if __name__ == "__main__":
    asyncio.run(run_agent())
    # add a text file in the same directory of the client "faa" in it
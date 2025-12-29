# Model-Context-Protocol
Model Context Protocol Repository for Zhu's research team

# Setting Up MCP server with uv

Need Claude Desktop and uv installed

Reference: https://www.youtube.com/watch?v=-8k9lGpGQ6g

curl -LsSf https://astral.sh/uv/install.sh | sh

mkdir mcp-server

uv init mcp-server

cd mcp-server

uv add "mcp[cli]"

You should see virtual environment, README, configuration, and server.py files in the mcp-server. The server.py file is where you programed mcp tools and resources that the LLM agent can use.

uv run mcp install server.py -> If you already have Claude Desktop, your mcp server will be added to Claude Config


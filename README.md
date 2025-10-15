# Echo MCP Service

A simple echo service implemented using the fastmcp framework.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/hackathon_mcp_demo.git
cd hackathon_mcp_demo
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Echo MCP service:
```bash
python echo_mcp.py
```

2. The service will be available at:
   - Echo endpoint: `http://localhost:8000/echo`
   - Uppercase echo endpoint: `http://localhost:8000/echo/uppercase`

3. Send requests to the service:

```python
from fastmcp import MCPClient

# Create an MCP client
client = MCPClient("http://localhost:8000")

# Send a message to the echo endpoint
response = client.call("/echo", {"message": "Hello, MCP!"})
print(response)  # {"message": "Hello, MCP!"}

# Send a message to the uppercase echo endpoint
response = client.call("/echo/uppercase", {"message": "Hello, MCP!"})
print(response)  # {"message": "HELLO, MCP!"}
```

## API Endpoints

### /echo

Returns the exact same message that was sent.

### /echo/uppercase

Returns the message with all string values converted to uppercase.

## Examples

### Example with curl

```bash
# Echo endpoint
curl -X POST http://localhost:8000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, MCP!"}'

# Uppercase echo endpoint
curl -X POST http://localhost:8000/echo/uppercase \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, MCP!"}'
```

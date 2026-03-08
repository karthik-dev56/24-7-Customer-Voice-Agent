# 24/7  Customer Support voice Agent

An intelligent conversational AI agent named "Anisha" built with LiveKit for providing multilingual customer support for Adidas. The agent supports real-time voice and text interactions with advanced speech processing, product search capabilities, and customer service tools.

## Features

### 🗣️ Multilingual Support
- **Default Language**: Hindi/Hinglish (Roman script)
- **Supported Languages**: Hindi, English, Telugu, Tamil, and more
- Automatic language detection and switching based on user preference

### 🎯 Core Capabilities
- **Product Search & Information**: Search Adidas products, check prices, find deals
- **Order Management**: Track orders and order status
- **Customer Support**: Handle complaints, create support tickets, escalate issues
- **General Queries**: Return policy, shipping information, store hours

### 🔧 Technical Features
- **Real-time Voice Processing**: Speech-to-text with Deepgram Nova-3 model
- **Natural Voice Synthesis**: Text-to-speech with Murf AI (Hindi voice: Sunaina)
- **AI-Powered Responses**: DeepSeek Chat model for intelligent conversations
- **Memory Integration**: Persistent conversation memory with Mem0AI
- **Web Search**: DuckDuckGo integration for general queries
- **Custom Product Database**: Direct integration with Adidas product API

## Tech Stack

- **Framework**: LiveKit Agents
- **LLM**: DeepSeek Chat via OpenAI API
- **STT**: Deepgram Nova-3 (Hindi language support)
- **TTS**: Murf AI (Hindi conversational voice)
- **Memory**: Mem0AI for conversation persistence
- **Search**: DuckDuckGo, Custom Adidas API
- **Additional Plugins**: Google, Noise Cancellation, Silero

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd livekit-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   # OR
   pip install -e .
   ```

3. **Set up environment variables**:
   ```bash
   cp demo_env_sample .env
   # Edit .env file with your API keys
   ```

## Environment Setup

Create a `.env` file with the following variables:

```env
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_secret

DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
MURF_API_KEY=your_murf_api_key

MEM0_API_KEY=your_mem0_api_key

# Other service API keys as needed
```

## Usage

### Running the Agent

1. **Start the agent**:
   ```bash
   python main.py
   ```

2. **For development with auto-reload**:
   ```bash
   python agent.py
   ```

### Conversation Examples

**English Greeting**:
- User: "Hello!"
- Anisha: "Namaste Boss, Anisha from Adidas here. Order check karna hai ya koi quick question hai?"

**Product Search**:
- User: "Show me cheapest Adidas shoes"
- Anisha: *Uses adidas_search_engine tool to fetch and display products*

**Order Tracking**:
- User: "Track my order"
- Anisha: *Accesses order system through Adidas API integration*

## Project Structure

```
├── agent.py              # Main agent implementation
├── main.py               # Entry point
├── tools.py              # Search and API integration tools
├── prompts.py            # Agent instructions and prompts
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project configuration
├── .env                  # Environment variables (create from demo_env_sample)
├── mcp_client/           # Model Context Protocol client
│   ├── __init__.py
│   ├── agent_tools.py
│   ├── server.py
│   └── util.py
└── KMS/                  # Knowledge Management System
    └── logs/
```

## Available Tools

### 1. General Web Search (`search_engine`)
- Uses DuckDuckGo for general web queries
- Handles non-Adidas specific questions

### 2. Adidas Product Search (`adidas_search_engine`)
- Product search and details
- Price checking and comparisons
- Order tracking
- Customer support ticket creation
- Issue logging and escalation

## Configuration

The agent can be customized through various parameters in [agent.py](agent.py):

- **LLM Settings**: Model, temperature, max tokens
- **Voice Settings**: STT language, TTS voice and style
- **Tools**: Enable/disable specific functionalities

## Development

### Adding New Tools
1. Create tool functions in [tools.py](tools.py)
2. Use the `@function_tool` decorator
3. Add to the tools list in the Assistant class

### Modifying Prompts
- Edit system instructions in [prompts.py](prompts.py)
- Adjust language preferences and response styles

### MCP Integration
The project includes Model Context Protocol support for advanced integrations. See the `mcp_client/` directory for implementation details.

## Logging

Logs are stored in the `KMS/logs/` directory. The agent provides detailed logging for:
- Search operations
- API interactions
- Error handling
- User conversations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request



---

**Note**: This agent is designed specifically for Adidas customer support scenarios for Demonstration and includes specialized tools for product search, order management, and customer service workflows.


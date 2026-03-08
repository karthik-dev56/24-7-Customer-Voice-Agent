from dotenv import load_dotenv
from livekit import agents, rtc
from livekit.agents import AgentSession, Agent, RoomInputOptions,ChatContext
from livekit.plugins.google.beta import realtime
from livekit.plugins import (
    openai,
    murf,
    noise_cancellation,
    google,
    deepgram
    
)
# from mcp_client import MCPServerSse
# from mcp_client.agent_tools import MCPToolsIntegration
from tools import search_engine,adidas_search_engine
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from mem0 import AsyncMemoryClient
import json
import logging
import os

load_dotenv()

class Assistant(Agent):
    def __init__(self, chat_ctx=None) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            llm=openai.LLM(
                model="deepseek-chat",
                # voice="Aoede",
                base_url="https://api.deepseek.com/",
                temperature=0.2,
                # max_output_tokens=200
            ),
            stt=deepgram.STT(
                model="nova-3",
                language="hi",
            ),
            tts=murf.TTS(
                voice="hi-IN-Sunaina",
                style="Conversational",
                speed=0.7,
                pitch=0
            ),
            tools=[search_engine,adidas_search_engine],
            chat_ctx=chat_ctx
        )    
        

async def entrypoint(ctx:agents.JobContext):

    async def shutdown_hook(chat_ctx:ChatContext,mem0:AsyncMemoryClient,memory_str:str):
        logging.info("Shutting down, saving chat context to memory...")

        messages_formatted = [

        ]
        logging.info(f"Chat context messages: {chat_ctx.items}")
        for item in chat_ctx.items:
            if item.type != 'message':
                continue
            content_str = ''.join(item.content) if isinstance(item.content,list) else str(item.content)

            if memory_str and memory_str in content_str:
                continue
            if item.role in ['user','assistant']:
                messages_formatted.append({
                    "role":item.role,
                    "content":content_str.strip()
                })
        logging.info(f"Formatted messages to add to memory: {messages_formatted}")
        await mem0.add(messages_formatted,user_id="karthik_123")
        logging.info("Chat context saved to memory.")




    session = AgentSession()


    mem0 = AsyncMemoryClient()
    user_name = "karthik_123"
    results = (await mem0.get_all(filters={"user_id": user_name})).get("results", [])

    initial_ctx = ChatContext()
    memory_str = ''

    if results:
        memories = [
            {
                "memory": result["memory"],
                "updated_at": result["updated_at"]
            }
            for result in results
        ]
        memory_str = json.dumps(memories)
        logging.info(f"Memories: {memory_str}")
        initial_ctx.add_message(
            role="assistant",
            content=f"The user's name is {user_name}, and this is relvant context about him: {memory_str}."
        )


    # mcp_server = MCPServerSse(
    #     params={"url": os.environ.get("N8N_MCP_SERVER_URL")},
    #     cache_tools_list=True,
    #     name="SSE MCP Server"
    # )

    # agent = await MCPToolsIntegration.create_agent_with_tools(
    #     agent_class=Assistant, agent_kwargs={"chat_ctx": initial_ctx},
    #     mcp_servers=[mcp_server]
    # )


    await session.start(
        room = ctx.room,
        agent = Assistant(chat_ctx=initial_ctx),
        room_input_options = RoomInputOptions(
            # video_enabled = True,
            noise_cancellation =  noise_cancellation.BVC()
        )
    )

    await ctx.connect()

    

    await session.generate_reply(
        instructions = SESSION_INSTRUCTION
    )

    ctx.add_shutdown_callback(lambda:shutdown_hook(session._agent.chat_ctx,mem0,memory_str))

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

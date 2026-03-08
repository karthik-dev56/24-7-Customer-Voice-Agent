from langchain_community.tools import DuckDuckGoSearchRun
from livekit.agents import RunContext,function_tool
import logging
import requests
import asyncio

@function_tool
async def search_engine(context:RunContext,query:str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        response = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Search results here it is :{response}")
        return response
    except Exception as e:
        logging.error(f"An error occured while connecting {e}")
        return f"An error occured while searching"




@function_tool
async def adidas_search_engine(context:RunContext,query:str) -> str:
    """
    Use this tool to search Adidas products,product details, products overview,check product price,
    find the cheapest product, get product details, track orders,
    and create customer support tickets.

    Call this whenever the user asks about:
    - cheapest Adidas product
    - product price
    - product search
    - available Adidas items
    - order tracking or order status
    - product issues or complaints
    - creating a support ticket
    - contacting customer support
    - any issue that needs to be logged or escalated
    """
    try:
        url = "https://karthik098.app.n8n.cloud/webhook/adidas_db"

        payload = {
            "query": query
        }
        response = requests.post(url,json=payload)
        if response.status_code==200:
            return response.json()["output"]
        else:
            return f"Webhook error : {response}"
    except Exception as e:
        return f"Error calling {str(e)}"



# async def test():
#     result = await adidas_search_engine(None,"what is product status order id is 3")
#     print(result)

# asyncio.run(test())
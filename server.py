import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/interzoid/api/get-email-information'

mcp = FastMCP('get-email-information')

@mcp.tool()
def get_email_information(email: Annotated[str, Field(description='Sample email address')]) -> dict: 
    '''Validates, categorizes, and enriches an email address with B2B demographics.'''
    url = 'https://get-email-information.p.rapidapi.com/getemailinfo'
    headers = {'x-rapidapi-host': 'get-email-information.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'email': email,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")

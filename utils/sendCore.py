import ssl
import os
import aiohttp
import urllib.parse

os.environ['no_proxy'] = '*'

cafeUrl = 'https://cafemaker.wakingsands.com/'
sourceUrl = 'https://universalis.app/api/v2/'
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False

async def searchItem(item):
    extPath = 'search'
    type = 'item'
    headers = {
        'Connection' : 'keep-alive',
        'Content-Type': 'application/json',
    }

    conn = aiohttp.TCPConnector(ssl=ssl_context)
    url = cafeUrl + extPath.replace(" ", "")
    url += "?indexes=" + type + "&limit=5&string=" + item
    
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            async with session.get(url=url, headers=headers) as response:
                data = await response.json()
                return data["Results"]
        except Exception as e:
            print(f"Error searching for {item}: {e}")



async def doSend(extPath, ifHQ):
    headers = {
        'Connection' : 'keep-alive',
        'Content-Type': 'application/json',
    }

    conn = aiohttp.TCPConnector(ssl=ssl_context)
    url = sourceUrl + extPath.replace(" ", "")
    url += "?listings=9&HQ=" + ifHQ
    
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            async with session.get(url=url, headers=headers) as response:
                data = await response.json()
                return data["listings"]
        except Exception as e:
            print(f"Error searching : {e}")


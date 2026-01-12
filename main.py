
import os
import httpx
import logging
from fastmcp import FastMCP


mcp = FastMCP("bindayagent")


@mcp.tool(name="find_council",
          description="Finds the council for a given postcode")
def find_council(postcode: str) -> str:
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['result']['admin_district']
    else:
        return "Unknown Council"
    

@mcp.tool(name="get_bin_collection_day", 
          description="Fetches bin collection day for a given council")
def get_bin_collection_day(council: str) -> str:

    if council.lower() != "brent":
        return "This tool only supports Brent council."

    file_path = os.path.join(os.path.dirname(__file__), "brent_collection_text.txt")
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read().rstrip()
    except FileNotFoundError:
        logging.warning("brent_collection_text.txt not found at %s", file_path)
    except Exception:
        logging.exception("failed to load 'brent_collection_text.txt' from %s", file_path)
    
    return data

def main():
    # Initialise and run the server
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
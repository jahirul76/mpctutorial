
import httpx
# from fastmcp import FastMCP
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

    with open('brent_collection_text.txt', 'r') as file:
        data = file.read().rstrip()

    return data

def main():
    # Initialise and run the server
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
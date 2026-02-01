from newsapi import NewsAPI
from fastmcp import FastMCP

NewsAPI = NewsAPI()
my_mcp = FastMCP("My server")

json_response = NewsAPI.get_top_headlines("bitcoin")
print(f"json_response={json_response}")
print(f"num_articles={len(json_response["articles"])}")

@my_mcp.tool
def top_headlines():
    return NewsAPI.get_top_headlines("bitcoin")

if __name__ == "__main__":
    my_mcp.run(transport="http", port=8000)
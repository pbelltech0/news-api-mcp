from newsapi import NewsAPI
from fastmcp import FastMCP

news_api = NewsAPI()
mcp = FastMCP("news-mcp-server")


@mcp.tool
def top_headlines(
    query=None, country=None, category=None, sources=None, page_size=None, page=None
):
    return news_api.get_top_headlines(
        query, country, category, sources, page_size, page
    )


@mcp.tool
def everything(
    query=None,
    search_in=None,
    sources=None,
    domains=None,
    exclude_domains=None,
    from_date=None,
    to_date=None,
    language=None,
    sortBy=None,
    pageSize=None,
    page=None,
):
    return news_api.get_everything(
        query,
        search_in,
        sources,
        domains,
        exclude_domains,
        from_date,
        to_date,
        language,
        sortBy,
        pageSize,
        page,
    )


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

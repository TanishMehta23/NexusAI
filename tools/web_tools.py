from tavily import TavilyClient
from config.settings import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query: str) -> str:
    """
    Search the internet using Tavily.
    """

    response = client.search(
        query=query,
        max_results=5
    )

    results = response.get("results", [])

    if not results:
        return "No search results found."

    output = ""

    for result in results:
        output += (
            f"Title: {result['title']}\n"
            f"Content: {result['content']}\n"
            f"URL: {result['url']}\n\n"
        )

    return output
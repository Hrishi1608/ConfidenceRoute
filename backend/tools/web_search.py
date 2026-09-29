from ddgs import DDGS


def web_search(query, max_results=5):
    """
    Search the web using DuckDuckGo.

    Args:
        query: Search query.
        max_results: Maximum number of results.

    Returns:
        A list of search results.
    """

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in search_results:
            results.append({
                "title": result.get("title", ""),
                "url": result.get("href", ""),
                "snippet": result.get("body", "")
            })

    return results
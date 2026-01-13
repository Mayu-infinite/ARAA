from ddgs import DDGS
    
def web_search(query: str, max_results: int = 5)->str:
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            if "body" in r:
                results.append(r["body"])

    return "SEARCH - " + "\n".join(results)


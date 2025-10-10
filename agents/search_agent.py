from langchain_ollama import OllamaLLM
from langchain.tools import DuckDuckGoSearchRun
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def search_and_summarize(query):
    print("\n🔎 Searching the web for:", query)
    search = DuckDuckGoSearchRun()
    results = search.run(query)

    llm = OllamaLLM(model="llama3")
    prompt = PromptTemplate.from_template("""
Summarize the following search results into 5 concise bullet points.

Query: {query}
Results: {results}

Summary:
""")
    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.invoke({"query": query, "results": results})
    return summary["text"]

if __name__ == "__main__":
    query = input("Enter your search topic: ")
    print(search_and_summarize(query))

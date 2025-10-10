from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def plan_goal(goal):
    llm = OllamaLLM(model="llama3")
    prompt = PromptTemplate.from_template("""
You are ARAA, an autonomous research planner.
Break down the following goal into clear, step-by-step subtasks.

Goal: {goal}

Output a numbered list of tasks.
""")
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.invoke({"goal": goal})
    return result["text"]

if __name__ == "__main__":
    goal = input("Enter your research goal: ")
    plan = plan_goal(goal)
    print("\n🧩 PLAN:\n", plan)

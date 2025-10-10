from agents.planner_agent import plan_goal
from agents.searcher_agent import search_and_summarize

def main():
    goal = input("🎯 Enter your overall research goal: ")
    plan = plan_goal(goal)

    print("\n🧭 PLANNED TASKS:\n", plan)

    # Ask user which step to execute
    step = input("\nWhich step do you want ARAA to execute? (e.g. 1): ")

    # Extract relevant line
    lines = [l.strip() for l in plan.splitlines() if l.strip()]
    if lines:
        chosen_task = lines[int(step)-1]
        print(f"\n🚀 Executing task: {chosen_task}\n")
        summary = search_and_summarize(chosen_task)
        print("\n✅ Task Result:\n", summary)
    else:
        print("⚠️ No tasks found.")

if __name__ == "__main__":
    main()

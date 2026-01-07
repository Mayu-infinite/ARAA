<<<<<<< HEAD
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
=======
from core.loop import AgentLoop

def main():
    goal = input("Enter your goal: ")
    loop = AgentLoop()
    state = loop.run(goal)

    print("\nRun finished.")

    print("\nFinal Memory:")
    for item in state.memory:
        print(f"- {item['task']}")
        print(f"  {item['result']}")

    print(f"\nCompleted tasks: {len(state.completed_tasks)}")
    print(f"Remaining tasks: {len(state.pending_tasks)}")
    print(f"Iterations: {state.iteration}")
>>>>>>> 2994e7a (updated project)

if __name__ == "__main__":
    main()

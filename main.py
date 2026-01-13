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

if __name__ == "__main__":
    main()

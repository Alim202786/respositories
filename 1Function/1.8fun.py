def spy_game(Agent):
    agent_code = [0, 0, 7]
    index = 0
    for code in Agent:
        if code == agent_code[index]:
            index += 1
        if index == len(agent_code):
            print("Welcome Jason Bond")
            return True
    return False

Agent = list(map(int, input("Enter the code: ").split()))
print(spy_game(Agent))
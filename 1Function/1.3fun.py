def solve(head, legs):
    for chickens in range(head + 1):
        rabbits = head - chickens
        if ((chickens * 2 + rabbits * 4) == legs):
            return chickens, rabbits

head = 35
legs = 94
chickens, rabbits = solve(head, legs)
print(f"chickens: {chickens}, rabbits: {rabbits}")
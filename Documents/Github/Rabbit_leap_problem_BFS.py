from collections import deque
def initial_config():
    return ('W', 'W', 'W', '_', 'E', 'E', 'E')


def is_goal_state(configuration):
    return configuration == ('E', 'E', 'E', '_', 'W', 'W', 'W')

def generate_possible_moves(config):
    config = list(config)  
    next_steps = []

    for i in range(len(config)):
        token = config[i]

        
        if token == 'W':
   
            if i + 1 < len(config) and config[i + 1] == '_':
                new_config = config[:]
                new_config[i], new_config[i + 1] = new_config[i + 1], new_config[i]
                next_steps.append(tuple(new_config))

  
            elif i + 2 < len(config) and config[i + 2] == '_' and config[i + 1] in ['W', 'E']:
                new_config = config[:]
                new_config[i], new_config[i + 2] = new_config[i + 2], new_config[i]
                next_steps.append(tuple(new_config))

        elif token == 'E':
           
            if i - 1 >= 0 and config[i - 1] == '_':
                new_config = config[:]
                new_config[i], new_config[i - 1] = new_config[i - 1], new_config[i]
                next_steps.append(tuple(new_config))

        
            elif i - 2 >= 0 and config[i - 2] == '_' and config[i - 1] in ['W', 'E']:
                new_config = config[:]
                new_config[i], new_config[i - 2] = new_config[i - 2], new_config[i]
                next_steps.append(tuple(new_config))

    return next_steps
def solve_with_bfs():
    queue = deque([(initial_config(), [])])
    visited = set()

    while queue:
        current_config, path = queue.popleft()

        if is_goal_state(current_config):
            return path + [current_config]

        if current_config in visited:
            continue

        visited.add(current_config)

        for next_config in generate_possible_moves(current_config):
            queue.append((next_config, path + [current_config]))

    return None
solution = solve_with_bfs()

print("Sequence of Moves to Solve the Rabbit Leap Puzzle:\n")
if solution:
    for step_num, state in enumerate(solution):
        print(f"Step {step_num + 1}: {state}")
else:
    print("No solution found.")


from collections import deque

class BridgeCrossing:
    def __init__(self):
        self.people = {
            'Amogh': 5,
            'Ameya': 10,
            'Grandmother': 20,
            'Grandfather': 25
        }
        self.all = set(self.people)

    def start_state(self):
        return (frozenset(self.all), frozenset(), 'L', 0)

    def is_goal(self, state):
        left, right, torch, time = state
        return len(left) == 0 and time <= 60

    def get_next_states(self, state):
        left, right, torch, time = state
        next_states = []

        if torch == 'L':
            for p1 in left:
                for p2 in left:
                    if p1 <= p2:
                        new_left = left - {p1, p2}
                        new_right = right | {p1, p2}
                        extra_time = max(self.people[p1], self.people[p2])
                        total_time = time + extra_time
                        if total_time <= 60:
                            next_states.append((new_left, new_right, 'R', total_time))
        else:
            for person in right:
                new_left = left | {person}
                new_right = right - {person}
                extra_time = self.people[person]
                total_time = time + extra_time
                if total_time <= 60:
                    next_states.append((new_left, new_right, 'L', total_time))

        return next_states


def solve_bfs(puzzle):
    q = deque([(puzzle.start_state(), [])])
    visited = set()

    while q:
        state, path = q.popleft()
        if puzzle.is_goal(state):
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for next_state in puzzle.get_next_states(state):
            q.append((next_state, path + [state]))

    return None


puzzle = BridgeCrossing()
solution = solve_bfs(puzzle)

print("\nBridge Crossing using BFS:\n")
if solution:
    for i, step in enumerate(solution):
        left, right, torch, time = step
        print(f"Step {i + 1}:")
        print(f"  Left side:  {set(left)}")
        print(f"  Right side: {set(right)}")
        print(f"  Torch side: {torch}")
        print(f"  Time used:  {time} minutes\n")
else:
    print("No valid solution found within the time limit.")

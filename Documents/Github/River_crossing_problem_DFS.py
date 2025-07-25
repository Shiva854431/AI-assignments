class BridgeCrossing:
    def __init__(self):
        self.times = {
            'Amogh': 5,
            'Ameya': 10,
            'Grandmother': 20,
            'Grandfather': 25
        }
        self.people = set(self.times.keys())

    def start_state(self):
        return (frozenset(self.people), frozenset(), 'L', 0)

    def is_done(self, state):
        left, right, lamp, time = state
        return len(left) == 0 and time <= 60

    def next_states(self, state):
        left, right, lamp, time = state
        states = []

        if lamp == 'L':
            for p1 in left:
                for p2 in left:
                    if p1 <= p2:
                        new_left = left - {p1, p2}
                        new_right = right | {p1, p2}
                        extra_time = max(self.times[p1], self.times[p2])
                        total = time + extra_time
                        if total <= 60:
                            states.append((new_left, new_right, 'R', total))
        else:
            for p in right:
                new_left = left | {p}
                new_right = right - {p}
                back_time = self.times[p]
                total = time + back_time
                if total <= 60:
                    states.append((new_left, new_right, 'L', total))

        return states


def dfs_solver(puzzle):
    stack = [(puzzle.start_state(), [])]
    seen = set()

    while stack:
        current, path = stack.pop()
        if puzzle.is_done(current):
            return path + [current]
        if current in seen:
            continue
        seen.add(current)

        for nxt in puzzle.next_states(current):
            stack.append((nxt, path + [current]))

    return None


puzzle = BridgeCrossing()
result = dfs_solver(puzzle)

print("\nBridge Crossing (DFS):\n")
if result:
    for i, step in enumerate(result):
        l, r, lamp, t = step
        print(f"Step {i + 1}:")
        print(f"  Left:  {set(l)}")
        print(f"  Right: {set(r)}")
        print(f"  Lamp:  {lamp}")
        print(f"  Time:  {t} mins\n")
else:
    print("No valid solution found.")

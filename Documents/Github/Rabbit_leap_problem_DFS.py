from collections import deque

class RabbitGame:
    def get_start(self):
        return ('W', 'W', 'W', '_', 'E', 'E', 'E')

    def is_finished(self, state):
        return state == ('E', 'E', 'E', '_', 'W', 'W', 'W')

    def possible_moves(self, state):
        state = list(state)
        moves = []

        for i in range(len(state)):
            if state[i] == 'W':
                if i + 1 < len(state) and state[i + 1] == '_':
                    new_state = state[:]
                    new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                    moves.append(tuple(new_state))
                elif i + 2 < len(state) and state[i + 2] == '_' and state[i + 1] in ['W', 'E']:
                    new_state = state[:]
                    new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                    moves.append(tuple(new_state))
            elif state[i] == 'E':
                if i - 1 >= 0 and state[i - 1] == '_':
                    new_state = state[:]
                    new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                    moves.append(tuple(new_state))
                elif i - 2 >= 0 and state[i - 2] == '_' and state[i - 1] in ['W', 'E']:
                    new_state = state[:]
                    new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                    moves.append(tuple(new_state))

        return moves


def solve_with_dfs(game: RabbitGame):
    stack = [(game.get_start(), [])]
    seen = set()

    while stack:
        current_state, path = stack.pop()

        if game.is_finished(current_state):
            return path + [current_state]

        if current_state in seen:
            continue

        seen.add(current_state)

        for next_state in game.possible_moves(current_state):
            stack.append((next_state, path + [current_state]))

    return None


if __name__ == "__main__":
    game = RabbitGame()
    solution = solve_with_dfs(game)

    print("🧩 Path to Goal:\n")
    if solution:
        for idx, step in enumerate(solution):
            print(f"Step {idx + 1}: {step}")
    else:
        print("No solution found.")

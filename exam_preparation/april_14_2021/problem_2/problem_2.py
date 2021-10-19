from collections import deque


def corresponding_numbers(board: list,row: int, col: int, size=7):
    total = board[row][0] + board[row][size-1] + board[0][col] + board[size-1][col]
    return total


def deduction(players_data, current_player, points_to_subtract):
    players_data[current_player]["points"] -= points_to_subtract


players = deque(input().split(","))
first_player, second_player = players[0], players[1]
players_data = {
    first_player: {
        "throws": 0, "points": 501
    },
    second_player: {
        "throws": 0, "points": 501
    }
}
size = 7
board = []
for row in range(size):
    board.append([x if x.isalpha() else int(x) for x in input().split()])


current_player = None
while True:
    data = input()

    if not data:
        break

    row_col_list = [int(x) for x in data if x.isnumeric()]
    row, col = int(row_col_list[0]), int(row_col_list[1])
    current_player = players[0]
    players_data[current_player]["throws"] += 1

    if row not in range(size) or col not in range(size):
        players.append(players.popleft())
        continue

    position = board[row][col]
    if position == "D":
        total_corresponding_nums = corresponding_numbers(board, row, col) * 2
        deduction(players_data, current_player, total_corresponding_nums)

    elif position == "T":
        total_corresponding_nums = corresponding_numbers(board, row, col) * 3
        deduction(players_data, current_player, total_corresponding_nums)

    elif position == "B":
        break

    else:
        deduction(players_data, current_player, position)

    if players_data[current_player]["points"] <= 0:
        break

    players.append(players.popleft())

print(f"{current_player} won the game with {players_data[current_player]['throws']} throws!")
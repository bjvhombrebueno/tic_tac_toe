# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board(player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    game[row][column] = player
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board(just_display=True)
game_board(player=1, row=2, column=1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os

# 先画棋盘
board = {
    1: "   ", 2: "   ", 3: "   ",
    4: "   ", 5: "   ", 6: "   ",
    7: "   ", 8: "   ", 9: "   ",
}

# 定义两个玩家
player1 = "x"
player2 = "o"


def drawBoard():
    os.system("cls")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("---+---+---")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("---+---+---")
    print(board[7] + "|" + board[8] + "|" + board[9])


def playGame():
    i = 0
    turn = ""
    while True:
        if (i % 2) == 0:
            turn = player1
        else:
            turn = player2
        while True:
            drawBoard()
            pos = int(input("%s, 请输入你要下的位置（0~9）：" % turn))
            if board[pos] == "   ":
                board[pos] = f" {turn} "
                break
            else:
                print("不能在这个位置下棋！请点击回车键重新下棋！")
                os.system("pause")
                # drawBoard()
        if i > 3:
            if justify() != "0":
                drawBoard()
                print(justify())
                os.system("pause")
                break
        i += 1
        if i == 9:
            drawBoard()
            print("游戏结束，平局！")
            os.system("pause")
            break


def justify():
    x_list = []
    o_list = []
    for key, value in board.items():
        if value == " x ":
            x_list.append(key)
        elif value == " o ":
            o_list.append(key)
    if isWin(x_list):
        return "x赢了"
    elif isWin(o_list):
        return "o赢了"
    else:
        return "0"


def isWin(lst):
    if 1 in lst:
        if 2 in lst and 3 in lst:
            return True
        elif 4 in lst and 7 in lst:
            return True
    if 9 in lst:
        if 7 in lst and 8 in lst:
            return True
        elif 3 in lst and 6 in lst:
            return True
    if 5 in lst:
        if 2 in lst and 8 in lst:
            return True
        elif 4 in lst and 6 in lst:
            return True
        elif 3 in lst and 7 in lst:
            return True
        elif 1 in lst and 9 in lst:
            return True
    return False

if __name__ == "__main__":
    playGame()

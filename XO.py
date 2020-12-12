matrix = [[".", 1, 2, 3],
    [1, " ", " ", " "],
    [2, " ", " ", " "],
    [3, " ", " ", " "]]

def show():
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(matrix[x][y], end=' ')
        print()

def ask(player):
    x, y = 0, 0
    print('Ходит '+player)
    while True:
        x = int(input('Введите ось Y: '))
        y = int(input('Введите ось X: '))
        if (x < 1 or x > 3 or y < 1 or y > 3 or matrix[x][y] == 'X' or matrix[x][y] == 'O'):
            print("Вы ввели недопустимое значение")
        else:
            matrix[x][y] = player
            break
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(matrix[x][y], end=' ')
        print()
    return

def chek_win(player):
    if matrix[1][1] == matrix[1][2] == matrix[1][3] == player\
            or matrix[2][1] == matrix[2][2] == matrix[2][3] == player\
            or matrix[3][1] == matrix[3][2] == matrix[3][3] == player\
            or matrix[1][1] == matrix[2][1] == matrix[3][1] == player\
            or matrix[1][2] == matrix[2][2] == matrix[3][2] == player\
            or matrix[1][3] == matrix[2][3] == matrix[3][3] == player\
            or matrix[1][1] == matrix[2][2] == matrix[3][3] == player\
            or matrix[1][3] == matrix[2][2] == matrix[3][1] == player:
        print(player + ' выиграл')
        return True
    if not(any([" " in row for row in matrix])):
        print("ничья")
        return True
show()
while True:
    ask('X')
    if chek_win('X'):
        break
    ask('O')
    if chek_win("O"):
        break
# Shift+F10 を押して実行する
import sys
import random

def display_map(map_list):
    for list in map_list:
        for item in list:
            print(str(item), end=' ')
        print("") # 改行追加

def check_current_num(sudoku_map, num):
    for list in sudoku_map:
        for item in list:
            if item == num:
                return True
    return False

def make_sudoku_map(sudoku_map):
    for i in range(1,10):

        flag = check_current_num(sudoku_map, i)

        if flag:
            continue

        while 1:
            try:

                x_poss = random.randint(0, 2)
                y_poss = random.randint(0, 2)

                if sudoku_map[x_poss][y_poss] == -1:
                    sudoku_map[x_poss][y_poss] = i
                    break
            except:
                print('x_poss' + str(x_poss))
                print('y_poss' + str(y_poss))
                return

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    args = sys.argv
    map_size = int(args[1])
    sudoku_map = [[-1] * map_size for i in range(map_size)]

    sudoku_map[0][0] = 3

    make_sudoku_map(sudoku_map)

    display_map(sudoku_map)

   # args[2] は固定数字のファイルパスを渡す

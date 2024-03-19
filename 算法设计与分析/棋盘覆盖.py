# 初始化棋盘和标记号
num = 0
Matrix = [[0]*100 for _ in range(100)]

# 棋盘覆盖函数
"""
chessBoard函数的五个参数分别表示:
tr:当前棋盘左上角的行号
tc:当前棋盘左上角的列号
dr:特殊方格的行号
dc:特殊方格的列号
size:当前棋盘的大小
这个函数的目标是将一个大小为size的棋盘,以(tr, tc)为左上角，以(dr, dc)为特殊方格，进行覆盖。
"""
def chessBoard(tr, tc, dr, dc, size):
    global num
    # 当棋盘大小为1时，无需覆盖
    if size == 1:
        return
    # 分割棋盘
    s = size // 2
    # 增加标记号
    t = num = num + 1

    # 覆盖左上角子棋盘
    if dr < tr + s and dc < tc + s:
        chessBoard(tr, tc, dr, dc, s)
    else:
        Matrix[tr+s-1][tc+s-1] = t
        chessBoard(tr, tc, tr+s-1, tc+s-1, s)

    # 覆盖右上角子棋盘
    if dr < tr + s and dc >= tc + s:
        chessBoard(tr, tc+s, dr, dc, s)
    else:
        Matrix[tr+s-1][tc+s] = t
        chessBoard(tr, tc+s, tr+s-1, tc+s, s)

    # 覆盖左下角子棋盘
    if dr >= tr + s and dc < tc + s:
        chessBoard(tr+s, tc, dr, dc, s)
    else:
        Matrix[tr+s][tc+s-1] = t
        chessBoard(tr+s, tc, tr+s, tc+s-1, s)

    # 覆盖右下角子棋盘
    if dr >= tr + s and dc >= tc + s:
        chessBoard(tr+s, tc+s, dr, dc, s)
    else:
        Matrix[tr+s][tc+s] = t
        chessBoard(tr+s, tc+s, tr+s, tc+s, s)

# 输入棋盘大小和特殊方格位置
size = int(input("请输入棋盘的行列号: "))
row, col = map(int, input("请输入特殊方格的行列号: ").split())
# 调用棋盘覆盖函数
chessBoard(0, 0, row, col, size)

# 打印覆盖后的棋盘
for r in range(size):
    for c in range(size):
        print(f"{Matrix[r][c]:2d} ", end='')
    print()
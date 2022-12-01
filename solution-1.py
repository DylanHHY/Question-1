import numpy as np
def Solution(N, R, C, SR, SC, INS):
    # 取得目前位置
    # grid
    TheGrid = boxMatrix(C, R)

    # 獲得初始位置
    present_posR = SR - 1
    present_posC = SC - 1

    # 紀錄當前位置，確保不會走到這格
    TheGrid[present_posR][present_posC] = 1

    # 依照指示並移動機器人
    for i in range(0, N):
        if INS[i] == "N":
            present_posR -= 1
        elif INS[i] == "S":
            present_posR += 1
        elif INS[i] == "W":
            present_posC -= 1
        else:
            present_posC += 1

        actualPos = TheGrid[present_posR][present_posC]

        # 如果有走過就繼續前進
        while(actualPos == 1):
            if INS[i] == "N":
                present_posR -= 1
            elif INS[i] == "S":
                present_posR += 1
            elif INS[i] == "W":
                present_posC -= 1
            else:
                present_posC += 1

            actualPos = TheGrid[present_posR][present_posC]

        # 紀錄當前位置，確保不會走到這格
        TheGrid[present_posR][present_posC] = 1

    return "{} {}".format(present_posR + 1, present_posC + 1)

# 定義矩陣行列
def boxMatrix(R, C):
    npMax = np.zeros((C, R))
    return npMax

# 根據說明給輸入
T = int(input())
for i in range(1, T+1):
    NRCSRSRINS = list(map(int, input().split(" ")))
    INS = input()

    print('Case #{}: {}'.format(i, Solution(
        NRCSRSRINS[0], NRCSRSRINS[1], NRCSRSRINS[2], NRCSRSRINS[3], NRCSRSRINS[4], INS)))

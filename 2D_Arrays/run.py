import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

if __name__ == '__main__':
    arr = []
    r = list()
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            # 00 01 02 11 20 21 22
            top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            middle = arr[i + 1][j + 1]
            low = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            r.append(top + middle + low)
    print(max(r))

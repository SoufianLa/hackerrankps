import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

l = [1, 4, 2, 10, 2, 3, 1, 0, 20]
w_len = 4
w_sum = sum(l[:w_len])
max_sum = -sys.maxsize -1

print(max_sum)

for i in range(len(l) - w_len):
    w_sum = w_sum - l[i] + l[i + w_len]
    m = max(w_sum, max_sum)


print(m)

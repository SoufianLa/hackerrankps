import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def resolve_dp(arr, total, start_index, mem):
    key = str(total) + ":" + str(start_index)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif start_index < 0:
        return 0
    elif arr[start_index] > total:
        to_return = resolve_dp(arr, total, start_index - 1, mem)
    else:
        to_return = resolve_dp(arr, total - arr[start_index], start_index - 1, mem) + resolve_dp(arr, total, start_index-1, mem)

    mem[key] = to_return
    return to_return


def count_number_of_subsets(arr, n):
    mem = {}
    return resolve_dp(arr, n, len(arr) - 1, mem)


if __name__ == '__main__':
    arr = [2, 4, 6, 10]
    n = 16
    print(count_number_of_subsets(arr, n))

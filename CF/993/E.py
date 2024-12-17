import math


def count_valid_pairs(k, l1, r1, l2, r2):
    count = 0
    power = 1
    while power <= r2:
        min_x = max(l1, math.ceil(l2 / power))
        max_x = min(r1, r2 // power)
        if min_x <= max_x:
            count += (max_x - min_x + 1)
        if power > r2 // k:
            break
        power *= k

    return count

def main():
    t = int(input())

    for _ in range(t):
        k, l1, r1, l2, r2 = map(int, input().split())
        result = count_valid_pairs(k, l1, r1, l2, r2)
        print(result)


if __name__ == "__main__":
    main()

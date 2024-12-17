def solve():
    t = int(input())
    results = []
    for _ in range(t):
        m, a, b, c = map(int, input().split())
        row1 = min(m, a)
        remaining_row1 = m - row1
        row1 += min(remaining_row1, c)
        c -= min(remaining_row1, c)
        row2 = min(m, b)
        remaining_row2 = m - row2
        row2 += min(remaining_row2, c)
        results.append(row1 + row2)
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()

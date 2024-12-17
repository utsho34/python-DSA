def solve_case(a):
    mirror_map = {'p': 'q', 'q': 'p', 'w': 'w'}
    b = ''.join(mirror_map[char] for char in reversed(a))
    return b

def main():
    t = int(input())
    for _ in range(t):
        a = input().strip()
        print(solve_case(a))


if __name__ == "__main__":
    main()

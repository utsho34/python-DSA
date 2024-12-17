def main():
    h, l = map(float, input().split())
    print("{:.7f}".format((l * l - h * h) / (2 * h)))

if __name__ == "__main__":
    main()
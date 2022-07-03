#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 0
    count = len(sys.argv) - 1
    for i in range(count):
        j = j + int(sys.argv[i + 1])
    print(f"{j}")

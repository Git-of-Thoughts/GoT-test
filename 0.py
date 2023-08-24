t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    start_with_0 = [w for w in words if w[0] == '0']
    end_with_1 = [w for w in words if w[-1] == '1']
    if len(start_with_0) == 0 or len(end_with_1) == 0:
        print(-1)
        continue
    if len(start_with_0) > len(end_with_1):
        to_reverse = start_with_0[:len(start_with_0) - len(end_with_1)]
    else:
        to_reverse = end_with_1[:len(end_with_1) - len(start_with_0)]
    print(len(to_reverse))
    for w in to_reverse:
        print(words.index(w) + 1, end=' ')
    print()
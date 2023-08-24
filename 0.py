t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    start_with_0_end_with_1 = [word for word in words if word[0] == '0' and word[-1] == '1']
    start_with_1_end_with_0 = [word for word in words if word[0] == '1' and word[-1] == '0']
    if len(start_with_0_end_with_1) == 0 or len(start_with_1_end_with_0) == 0:
        print(0)
        continue
    if len(start_with_0_end_with_1) > len(start_with_1_end_with_0):
        to_reverse = start_with_0_end_with_1
    else:
        to_reverse = start_with_1_end_with_0
    to_reverse.sort(key=len)
    reversals = max(0, abs(len(start_with_0_end_with_1) - len(start_with_1_end_with_0)) - 1)
    print(reversals)
    for i in range(reversals):
        print(words.index(to_reverse[i]) + 1, end=' ')
    print()
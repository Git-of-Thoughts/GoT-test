t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    start = [0]*2
    end = [0]*2
    both = [0]*2
    for word in words:
        start[word[0] == '1'] += 1
        end[word[-1] == '1'] += 1
        both[word[0] == word[-1]] += 1
    if both[0] > 0 and both[1] > 0 and start[0] == end[0]:
        print(-1)
    else:
        print(max(abs(start[0] - end[0]) - min(both), 0))
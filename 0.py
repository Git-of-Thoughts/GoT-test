def solve(test_cases):
    results = []
    for test_case in test_cases:
        n, words = test_case
        start_with_0 = [word for word in words if word[0] == '0']
        start_with_1 = [word for word in words if word[0] == '1']
        if len(start_with_0) == 0 or len(start_with_1) == 0:
            results.append((0, []))
            continue
        start_with_0.sort(key=lambda x: x[-1])
        start_with_1.sort(key=lambda x: x[-1])
        if start_with_0[-1][-1] == '0' and start_with_1[-1][-1] == '1':
            results.append((0, []))
        elif start_with_0[-1][-1] == '1' and start_with_1[-1][-1] == '0':
            if len(start_with_0) > len(start_with_1):
                results.append((1, [words.index(start_with_0[-1]) + 1]))
            else:
                results.append((1, [words.index(start_with_1[-1]) + 1]))
        else:
            results.append((-1, []))
    return results

print(solve([(4, ['0001', '1000', '0011', '0111']), (3, ['010', '101', '0']), (2, ['00000', '00001']), (4, ['01', '001', '0001', '00001'])]))
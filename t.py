def solution(data, n):
    # Your code here
    common_dict = {}
    for d in data:
        if d in common_dict.keys():
            common_dict[d] += 1
        else:
            common_dict[d] = 1

    result = []

    for key in common_dict.keys():
        if common_dict[key] <= n:
            result.append(key)

    final = []
    for i in range(len(data)):
        if data[i] in result:
            final.append(data[i])

    return final


print(solution([5 , 10 , 15, 10 , 7], 0))

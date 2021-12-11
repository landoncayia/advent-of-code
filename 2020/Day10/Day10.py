def part1(jolts):
    curr_rating = 0  # charging outlet jolt rating = 0
    diffs = {1: 0, 2: 0, 3: 1}  # diff of 3 initialized to 1 since device joltage will produce a diff of 3
    while curr_rating < max(jolts):
        compatible_js = [curr_rating+1, curr_rating+2, curr_rating+3]
        for j in compatible_js:
            if j in jolts:
                d = j - curr_rating
                diffs[d] += 1
                curr_rating = j
                break
    ans = diffs[1] * diffs[3]
    return ans


def part2(jolts):
    jolts = sorted(jolts)
    jolts.append(max(jolts)+3)  # for your device
    combos = {0: 1}  # 1 combo for the outlet
    for jolt in jolts:
        combos[jolt] = combos.get(jolt-1, 0) + combos.get(jolt-2, 0) + combos.get(jolt-3, 0)
    return combos[jolts[-1]]


with open('input.txt', 'r') as f:
    data = f.readlines()

jolt_list = [int(jolt) for jolt in data]
ans1 = part1(jolt_list)
print(ans1)
ans2 = part2(jolt_list)
print(ans2)

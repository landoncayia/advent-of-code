import string

with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')


# Part One: Questions to which anyone answered "Yes"
# passports = [{key: value for word in passport.split() for key, value in [word.split(':')]} for passport in passports]
responses = [d.replace('\n', '') for d in data]
counts = [[c for c in string.ascii_lowercase if c in question] for question in responses]
print(sum([len(count) for count in counts]))

# Part Two: Questions to which EVERYONE answered "Yes"
responses_2 = [d.replace('\n', ' ') for d in data]
counts_2 = [[c for c in string.ascii_lowercase if all([c in s for s in question_2.split()])] for question_2 in
            responses_2]
print(sum([len(count) for count in counts_2]))

brackets = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>',
}

scores = {
    ')' : 3,
    ']' : 57,
    '}' : 1_197,
    '>' : 25_137,
}

lines = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        lines.append(list(line.strip('\n')))

error_scores = []
for i, line in enumerate(lines):
    stack = []
    for bracket in line:
        if (bracket in brackets):
            stack.append(bracket)
        elif (bracket in brackets.values()):
            if (brackets[stack[-1]] == bracket):
                stack.pop()
            else:
                print(f'Error on line {i+1}, expected {brackets[stack[-1]]} but found {bracket}')
                error_scores.append(scores[bracket])
                break

print(f'Score is: {sum(error_scores)}')

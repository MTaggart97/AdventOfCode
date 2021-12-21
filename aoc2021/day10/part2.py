brackets = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>',
}

scores = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4,
}

lines = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        lines.append(list(line.strip('\n')))

# Remove all incomplete lines
corrupted_lines = []
for i, line in enumerate(lines):
    stack = []
    incomplete = False
    for bracket in line:
        if (bracket in brackets):
            stack.append(bracket)
        elif (bracket in brackets.values()):
            if (brackets[stack[-1]] == bracket):
                stack.pop()
            else:
                print(f'Error on line {i+1}, expected {brackets[stack[-1]]} but found {bracket}')
                incomplete = True
                break
    if (not incomplete):
        corrupted_lines.append(line)

final_scores = []
for line in corrupted_lines:
    stack = []
    for bracket in line:
        if (bracket in brackets):
            stack.append(bracket)
        elif (brackets[stack[-1]] == bracket):
                stack.pop()
    charaters_to_complete = []
    while stack:
        charaters_to_complete.append(brackets[stack.pop()])
    completion_string = ''.join(charaters_to_complete)
    print(f'Completion string: {completion_string}')
    # Calculate score
    score = 0
    for c in charaters_to_complete:
        score *= 5
        score += scores[c]
    final_scores.append(score)

final_scores.sort()
print(final_scores[int(len(final_scores)/2)])

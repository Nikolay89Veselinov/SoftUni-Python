# Given a sequence consisting of parentheses, determine whether the expression is balanced. A sequence of
# parentheses is balanced if every open parenthesis can be paired uniquely with a closed parenthesis that occurs
# after the former. Also, the interval between them must be balanced. You will be given three types of parentheses:
# (, {, and [.

parantheses = input()
stack = []
pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}
valid = True

for el in parantheses:
    if el in '([{':
        stack.append(el)
    elif el in ')]}':
        if stack:
            current = stack[-1]
        if pairs[current] == el:
            if stack:
                stack.pop()
        else:
            valid = False
            break

if valid:
    print('yes')
else:
    print('no')

# input

# {[(])}

# {{[[(())]]}}
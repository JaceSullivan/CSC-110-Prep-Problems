###Jason Sullivan
###CSC 110
###This program will check to make sure that for every open parenthesis ,(, there will be a closed parenthesis, ).  Will determine if parenthesis are even by taking a string input.
string_expression = input('Enter string:\n')

parenthesis1 = 0
parenthesis2 = 0
i = 0

while i < len(string_expression):
    if string_expression [i] == '(':
        parenthesis1 +=1
    elif string_expression [i] == ')':
        parenthesis2 +=1
    i += 1

if parenthesis1 == parenthesis2:
    print('Parenthesis balanced')
else:
    print('Parenthesis unbalanced')


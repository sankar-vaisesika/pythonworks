def paranthesis(s):

    stack=[]

    mapping={
        ']':'[',
        '}':'{',
        ')':'('
    }

    for c in s:

        if c in mapping:

            if stack and stack[-1]==mapping[c]:

                stack.pop()

            else:

                return False
            
        else:

            stack.append(c)

    return not stack

        
print(paranthesis('{[]}'))

print(paranthesis('()[]{}'))

print(paranthesis('([)'))

print(paranthesis("}{[]}"))

print(paranthesis("}{}"))


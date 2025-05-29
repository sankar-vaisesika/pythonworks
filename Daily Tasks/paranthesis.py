# def paranthesis(s):

#     stack=[]

#     mapping={
#         ']':'[',
#         '}':'{',
#         ')':'('
#     }

#     for c in s:

#         if c in mapping:

#             if stack and stack[-1]==mapping[c]:

#                 stack.pop()

#             else:

#                 False
            
#         else:

#             stack.append(c)

#     return not stack

        


# print(paranthesis('{[]}'))

# print(paranthesis('()[]{}'))

# print(paranthesis('([)'))


def paranthesis(s):

        mapping={
        ']':'[',
        '}':'{',
        ')':'('
    }
        
        stack=[]

        for c in s:
                
            if c in mapping:
                  
                  if stack and stack[-1]==mapping[c]:
                        
                        stack.pop()

                  else:
                        
                        False
            else:
                  stack.append(c)
        
        return not stack

print(paranthesis('{[]}'))

print(paranthesis('()[]{}'))

print(paranthesis('([)'))
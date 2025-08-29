a=0
b=1

print(a)
print(b)

for c in range(18):

    c=a+b

    print(c)

    a=b
    b=c

# implementation using recursion

print(0)

print(1)

count=2

def fibanocci(a,b):

    global count

    if count<=19:

        c=a+b

        print(c)

        a=b

        b=c

        count+=1

        fibanocci(a,b)

    else:

        return 

fibanocci(0,1)



# Finding The nth Fibonacci Number Using Recursion

def F(n):

    if n<=1:

        return n
    
    else:

        return F(n-1)+F(n-2)
    
print(F(18))
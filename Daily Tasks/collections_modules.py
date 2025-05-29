from collections import Counter

c=Counter("banana")

print(c)

#_______________________________

from collections import OrderedDict

od=OrderedDict()

od['a']=1

od['b']=2

print(od)

#__________________________________

from collections import defaultdict

dd = defaultdict(int)
dd['a'] = 1
print(dd)  

#_______________________________

from collections import ChainMap

dict1 = {'a': 1}
dict2 = {'b': 2}
cm = ChainMap(dict1, dict2)
print(cm)

#_________________________________

from collections import namedtuple

Student=namedtuple('Student',['fname','lname','dob'])

s=Student("mani","kandan","2002-04-19")

print(s.fname)

#_________________________________


from collections import deque

dq=deque([1,2,3])

dq.append(4)

dq.appendleft(3)

print(dq)   #output:-deque([3, 1, 2, 3, 4])

#__________________________________

def greet(name:str):

    print("Hello",name)

greet("saji")
#1: Convert a List of Strings to Lowercase

countries=["USA","India","Chine","Russia","Japan"]

lowercase_countries=list(map(lambda x:x.lower(),countries))
print(lowercase_countries)

#Calculate the Length of Each Word

words = ['python', 'is', 'awesome', 'and', 'fun']

lenth_of_words=list(map(lambda x:len(x),words))

print(lenth_of_words)

#Add a Prefix to Each String
usernames = ['alice', 'bob', 'charlie', 'david']

prefixed_usernames=list(map(lambda x:"user_"+x, usernames))

print(prefixed_usernames)
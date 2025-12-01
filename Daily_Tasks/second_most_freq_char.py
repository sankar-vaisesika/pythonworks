# Find the second most frequent character in a string

def second_most_frequent_character(s):

    cleaned_s=s.replace(" ","").lower()

    count={}

    for ch in cleaned_s:
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1

    sorted_count=sorted(count.items(),key=lambda x:x[1],reverse= True)
    return sorted_count [1][0]
print(second_most_frequent_character("Programming is fun"))
print(second_most_frequent_character("successs"))
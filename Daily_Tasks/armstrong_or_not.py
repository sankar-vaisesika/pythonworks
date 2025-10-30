num=1531

digit_count=len(str(num))
org_num=num
total=0

while num!=0:
    digit=num%10
    exp=digit**digit_count
    total+=exp
    num=num//10
print("Armstrong" if org_num==total else "Not armstrong")
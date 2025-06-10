
def intToRoman(num):

    roman_mapping=[
        (1000,"M"),(900,"CM"),(500,"D"),(100,"C"),(90,'XC'),(50,"L"),(40,"XL"),(10,"X"),(9,'IX'),(5,"V"),(4,"IV"),(1,"I")
    ]

    res=""

    for value,symbol in roman_mapping:

        while num>=value:

            res+=symbol

            num=num-value

    return res


print(intToRoman(3749))
print(intToRoman(1994))
print(intToRoman(58))

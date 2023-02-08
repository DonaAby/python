ch=input("enter the character")
v=["a","e","i","o","u","A","E","I","O","U"]
if ch in v:
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")

str1=input("enter string")
for i in str1:
    if i in v:
        print(f'{i}is a vowel')
    else:
        print(f'{i} is a consonant')
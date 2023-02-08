# Capitalize the 1st character of a string
str="good morning"
print(str.capitalize())

# Count the number of a specific character in a string
str1="Welcome to python django angular full stack development"
print(str1.count('e'))

#Find the index of the first occurence of a substring in a string

str="I am Dona Aby"
index=str.find('D')
print(index)

#check if a string contains only numbers
str="My DOB is 18 march"
print(str.isdigit())
str1="12345678"
print(str1.isdigit())

#check if each word in a string begins with a capital letter
str="My name is Dona Aby"
print(str.istitle())

#count the total number of characters in a string
str="My name is Dona Aby"
print(len(str))

#replace special symbol with #
str1='/*Jon is @developer & musician!!'
nstr=str1.replace('/','#')
#print(nstr)
nstr1=nstr.replace('*','#')
#print(nstr1)
nstr2=nstr1.replace('@','#')
#print(nstr2)
nstr3=nstr2.replace('&','#')
#print(nstr3)
nstr4=nstr3.replace('!','#')
print(nstr4)


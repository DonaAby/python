"""WAP to print integer values i n a list using list comprehension"""
ls=[12,33,44,55,6,7,814,"dfdh"]
result=[x for x in ls if type(x)==int]
print(result)
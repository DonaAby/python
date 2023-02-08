import random
print(dir(random))
a=random.random()
print(a)
b=random.randint(1,100)
print(b)
c=random.randrange(1,10,2)
print(c)
d=random.choice([1,2,3,4,5,6])
print(d)
n=[1,2,3,4,5]
random.shuffle(n)
print(n)
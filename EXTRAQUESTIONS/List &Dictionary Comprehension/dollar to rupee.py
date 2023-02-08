"""DICTIONARY COMPREHENSION"""
def dollar():
    price={'laptop':10,'mobile':5,'watch':3,'keyboard':1}
    conversion=81.38
    n_price={i:j*conversion for (i,j)in price.items()}
    return n_price
rc=dollar()
print(rc)
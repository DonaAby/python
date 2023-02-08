#JSON -JAVASCRIPT OBJECT NOTATION
#Storing and exchange data(python to java , java to python)
#json => python : json.loads
#python=>json : json.dumps
#json always string type

import json
import os
print(dir(json)) #dir-says all the function names in it
#json
x='{"name":"dona","age":12}'
print(type(x))

#parsing json to python
# y=json.loads(x)
# print(type(y)

#parsing python to json
d={"name":"saliha","age":20,"place":"mvpa"}
y=json.dumps(d)
print(type(y))
print(os.getcwd())
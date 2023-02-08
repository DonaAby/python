f=open("test1","r")
# print(f.read())
# print(f.read(14))
# print(f.readline())
# print(f.readline())

"""we can use for loop for printing new line"""
# for i in f:
#     print(i)
# f.close()

"""APPEND"""
# f=open("test1","a")
#
# f.write("python is a oop")
# f=open("test1","r")
# print(f.read())
# f.close()

"""WRITE"""
# f=open("test1","w")
# f.write("python is simple")
# f=open("test1","r")
# print(f.read())
# f.close()

"""SEEK"""
# f=open("test1","r")
# f.seek(10)
# print(f.readline())
# f.close()

"""TELL"""
# f=open("test1","r")
# f.readline()
# pos=f.tell()
#
# f.close()
# print("position is :",pos)

"""WAP TO READ A FILE LINE BY LINE AND STORE INTO A LIST"""
# def file_read(fna):
#     with open(fna) as f:
#         output_list=f.readlines()
#     print(output_list)
# file_read("test1")

"""COPY"""
# from shutil import copyfile
# copyfile("test1","test2")


"""WAP to cal the occurence of each element as a dictionary """
str1="cat rat mat cat pat rat cat sat cat "
words=str1.split()
print(words)
d={}
for i in words:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

"using file"
f=open('test1','r')
dict={}
for i in f: ## i is the first line of the file
    var=i.split(" ")
    for j in var:
        if j not in dict:
            dict[j]=1
        else:
            dict[j]+=1
print(dict)
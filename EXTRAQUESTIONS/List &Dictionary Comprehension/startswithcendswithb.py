"""WAP to print the string that starts with c and ends with b"""
names=["chb","ydb","thd","hgt","cghb","cfdsrtb"]
newname=[x for x in names if x.startswith("c") & x.endswith("b")]
print(newname)
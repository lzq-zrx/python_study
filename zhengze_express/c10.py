# 提取life和python之间的所有数据
import re
s = 'life is short,i use python,i love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group(0))
#关于group这个组的概念
print(r.group(1))
print(r.group(2))
print(r.group(0,1,2))
print(r.groups())

 
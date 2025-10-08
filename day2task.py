#list
m=[22,44,67,88,88,2]
print (m)
m.append(99)
print (m)
m.copy()
print (m)
print(m.count(88))
m.insert(1,8)
print(m)
print(m.index(2))
m.pop()
print(m)
m.sort()
print(m)

#Tuple
Tuple =('abarna','dharani','ragavi','priya','dharani')
print(Tuple.count('dharani'))
print(Tuple.index('dharani'))

#set
set={1,2,3,4,5}
set1={6,4,7,8,3,9}
set1.add(10)
print(set1)
set1.discard(9)
print(set1)
print ("The length is:",len(set))
print(set1.pop())
print("The union is:",set|set1)
print("The intersection is:",set&set1)

#Dictionary

mypython={'Empno':'1','Name':'Bala','department':'IT'}
mypython1={'designation':'developer'}
print("The items are:",mypython.items())
print("The keys are:",mypython.keys())
print("Values using keys: ",mypython.get('Name'))
mypython.update(mypython1)
print("after update:",mypython)
mypython.pop('department')
print("after pop:",mypython)
import monkdata as m
import dtree as d

t = d.buildTree(m.monk1, m.attributes)
print('monk1')
print(d.check(t, m.monk1test))
print(d.check(t, m.monk1))
print()

print('monk2')
t = d.buildTree(m.monk2, m.attributes)
print(d.check(t, m.monk2test))
print(d.check(t, m.monk2))
print()

print('monk3')
t = d.buildTree(m.monk3, m.attributes)
print(d.check(t, m.monk3test))
print(d.check(t, m.monk3))


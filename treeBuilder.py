import monkdata as m
import dtree as dt
import drawtree as draw

entropy = dt.entropy(m.monk1)
best_gain = 0
for attribute in m.attributes:
    gain = dt.averageGain(m.monk1, attribute)
    if gain > best_gain:
        best_gain = gain
        best_attribute = attribute


for v in best_attribute.values:
    subset = dt.select(m.monk1, best_attribute, v)
    majority_class = dt.mostCommon(subset)

values = {v: dt.mostCommon(dt.select(m.monk1, best_attribute, v)) for v in best_attribute.values}
print(best_attribute, values)
draw.drawTree(dt.buildTree(m.monk1, m.attributes, 2))

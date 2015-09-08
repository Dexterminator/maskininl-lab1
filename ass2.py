import monkdata as m
import dtree as dt


def printAverageGain(s, dataset):
    for x in range(0, 6):
        s = s + str(dt.averageGain(dataset, m.attributes[x])) + " "
        pass
    print(s)
    pass

    print("Average gain\n")


printAverageGain("Monk1: ", m.monk1)
printAverageGain("Monk2: ", m.monk2)
printAverageGain("Monk3: ", m.monk3)

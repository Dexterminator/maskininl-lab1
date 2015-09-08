import monkdata as m
import dtree as dt
import random


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def main():
    dataset = m.monk1
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    for fraction in fractions:
        average_performance = pruned_tree_performance(dataset, fraction)
        print(fraction, average_performance)


def pruned_tree_performance(dataset, fraction):
    total_performance = 0
    AGGREGATE_TIMES = 1000
    for i in range(AGGREGATE_TIMES):
        tree = best_pruned_tree(dataset, fraction)
        total_performance += dt.check(tree, m.monk1test)
    average_performance = total_performance / AGGREGATE_TIMES
    return average_performance


def best_pruned_tree(dataset, fraction):
    monk1train, monk1val = partition(dataset, fraction)
    tree = dt.buildTree(monk1train, m.attributes)
    improved = True
    while improved:
        improved = False
        best_performance = dt.check(tree, monk1val)
        for pruned_tree in dt.allPruned(tree):
            performance = dt.check(pruned_tree, monk1val)
            if performance > best_performance:
                best_performance = performance
                tree = pruned_tree
                improved = True
    return tree


if __name__ == '__main__':
    main()

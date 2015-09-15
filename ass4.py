import monkdata as m
import dtree as dt
import random

FRACTIONS = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
AGGREGATE_TIMES = 10000


def main():
    datasets = [('monk1', m.monk1, m.monk1test), ('monk3', m.monk3, m.monk3test)]
    for name, training_set, test_set in datasets:
        print(name)
        print_non_pruned_performance(training_set, test_set)
        print_pruned_performances(training_set, test_set)
        print()


def print_non_pruned_performance(training_set, test_set):
    non_pruned_tree = dt.buildTree(training_set, m.attributes)
    performance_without_pruning = dt.check(non_pruned_tree, test_set)
    print('Performance without pruning: {}'.format(performance_without_pruning))


def print_pruned_performances(training_set, test_set):
    best_performance = 0
    for fraction in FRACTIONS:
        average_performance = pruned_tree_performance(training_set, test_set, fraction)
        if average_performance > best_performance:
            best_performance = average_performance
            best_fraction = fraction
        print('Pruning performance with fraction {}: {}'.format(fraction, average_performance))
    print('Best fraction: {}: {}'.format(best_fraction, best_performance))


def pruned_tree_performance(training_set, test_set, fraction):
    total_performance = 0
    for i in range(AGGREGATE_TIMES):
        tree = best_pruned_tree(training_set, fraction)
        total_performance += dt.check(tree, test_set)
    average_performance = total_performance / AGGREGATE_TIMES
    return average_performance


def best_pruned_tree(dataset, fraction):
    train, val = partition(dataset, fraction)
    tree = dt.buildTree(train, m.attributes)
    improved = True
    while improved:
        improved = False
        best_performance = dt.check(tree, val)
        for pruned_tree in dt.allPruned(tree):
            performance = dt.check(pruned_tree, val)
            if performance > best_performance:
                best_performance = performance
                tree = pruned_tree
                improved = True
    return tree


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


if __name__ == '__main__':
    main()

import math


def get_proportion(classification, dataset):
    return  1-(len(dataset) - len(list(filter(lambda x: x[1] == classification, dataset)))) / len(dataset)
    


def misclassification(dataset):
    ks = list(set(x[1] for x in dataset))
    classifications = [(x, get_proportion(x,dataset)) for x in ks]
    return 1-max([x[1] for x in classifications])



def gini(dataset):
    ks = list(set(x[1] for x in dataset))
    classifications = [(x, get_proportion(x,dataset)) for x in ks]
    return sum([x[1] * ( 1-x[1]) for x in classifications])



def entropy(dataset):
    ks = list(set(x[1] for x in dataset))
    classifications = [(x, get_proportion(x,dataset)) for x in ks]
    return -1*sum([x[1] * (math.log2(x[1])) for x in classifications])



print("COMICALLY INEFFICIENT")
data = [
    ((False, False), False),
    ((False, True), True),
    ((True, False), True),
    ((True, True), False)
]
print("{:.4f}".format(misclassification(data)))
print("{:.4f}".format(gini(data)))
print("{:.4f}".format(entropy(data)))


# print(get_proportion(True, data))
# print("{:.4f}".format(misclassification(data)))


print("COMICALLY INEFFICIENT")
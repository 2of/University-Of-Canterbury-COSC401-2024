class DTNode(): 
    def __init__(self, decision):
        self.children = []
        self.decision = decision
    def leaves(self):
        if len(self.children) == 0:
            return 1
        return sum([self.children[x].leaves() for x in range(0,len(self.children))])
    def predict(self, x): 
        # print(self.__class__.__name__)
        # print("PREDICT GOT", x)
        if len(self.children) == 0:
            #is leaf
            return self.decision
        if callable(self.decision):
            m = self.decision(x)
            return self.children[m].predict(x)
            pass
        else:
            return self.decision

def get_proportion(classification, dataset):
    return  1-(len(dataset) - len(list(filter(lambda x: x[1] == classification, dataset)))) / len(dataset)
def misclassification(dataset):
    ks = list(set(x[1] for x in dataset))
    classifications = [(x, get_proportion(x,dataset)) for x in ks]
    return 1-max([x[1] for x in classifications])

def partition_by_feature_value(dataset,feature_index):



    keys = set([x[0][feature_index] for x in dataset])
    partitions = {key: [] for key in keys}
    for row in dataset:
        partitions[row[0][feature_index]].append(row)
    partitions_list = [key for key in partitions.values()]
    def create_function(feauture_index):
            def sepfunc(feature_vector):
                for feature_n in range(len(partitions_list)):
                    feature = partitions_list[feature_n]
                    if feature[0][0][feature_index] == feature_vector[feature_index]:
                        # print("returning index ", feature_n)
                        return feature_n      
                return 0
            return sepfunc
    return (create_function(feature_index), partitions_list)



def tree_helper(dataset,criterion,features_set):
    def most_common_labe2l():
        a = max(set(dataset[1]), key=dataset[1].count)
        if isinstance(a, tuple):
            return a[0]
        return a
    
    def most_common_label():
        labels = [x[1] for x in dataset]
        label_counts = {label: labels.count(label) for label in set(labels)}
        max_count = max(label_counts.values())
        for label in labels:  # iterate in original order
            if label_counts[label] == max_count:
                return label

    labels = [x[1] for x in dataset]
    if all(x == labels[0] for x in labels):
        return DTNode(labels[0])
    if len(features_set) == 0:
        return DTNode(most_common_label())

    impurity = float('inf')
    best_fi, best_part, best_dec = None, None, None
    for f_i in features_set:
        decision, datalabels_split = partition_by_feature_value(dataset, f_i)
        col_impurity = sum([criterion(x) * len(x) / len(dataset) for x in datalabels_split])
        if col_impurity < impurity:
            impurity = col_impurity
            partitions = datalabels_split
            decision_for_node = decision   
            best_fi = f_i 
    # hopefully ? 
    if best_fi is None:  
        return DTNode(most_common_label())


    # NOW THIS IS A THING! AHH
    feat_set_2 = features_set.copy()
    feat_set_2.difference_update({best_fi})

    Node = DTNode(decision_for_node)
    for partition in partitions:
        Node.children.append(tree_helper(partition, criterion, feat_set_2))
    return Node


def train_tree(dataset,criterion): 
    

    features_set = set([i for i in range(len(dataset[0][0]))])
    return (tree_helper(dataset, criterion,features_set))


dataset = [
    (("Sunny",    "Hot",  "High",   "Weak"),   False),
    (("Sunny",    "Hot",  "High",   "Strong"), False),
    (("Overcast", "Hot",  "High",   "Weak"),   True),
    (("Rain",     "Mild", "High",   "Weak"),   True),
    (("Rain",     "Cool", "Normal", "Weak"),   True),
    (("Rain",     "Cool", "Normal", "Strong"), False),
    (("Overcast", "Cool", "Normal", "Strong"), True),
    (("Sunny",    "Mild", "High",   "Weak"),   False),
    (("Sunny",    "Cool", "Normal", "Weak"),   True),
    (("Rain",     "Mild", "Normal", "Weak"),   True),
    (("Sunny",    "Mild", "Normal", "Strong"), True),
    (("Overcast", "Mild", "High",   "Strong"), True),
    (("Overcast", "Hot",  "Normal", "Weak"),   True),
    (("Rain",     "Mild", "High",   "Strong"), False),
]
t = train_tree(dataset, misclassification)
print(t.predict(("Overcast", "Cool", "Normal", "Strong")))
print(t.predict(("Sunny", "Cool", "Normal", "Strong")))



# dataset = [
#   ((), False),
#   ((), True),
#   ((), True),
#   ((), False)
# ]
# t = train_tree(dataset, misclassification)
# print(t.predict((True, False)))
# print(t.predict((False, False)))

	
dataset = [
  ((True, True), False),
  ((True, False), True),
  ((False, True), True),
  ((False, False), False)
]
t = train_tree(dataset, misclassification)
print(t.predict((True, False)))
print(t.predict((False, False)))
print(t.leaves())

# for j in dataset[0:

dataset = []
with open('nursery.data', 'r') as f:
    for line in f.readlines():
        features = line.strip().split(",")
        dataset.append((tuple(features[:-1]), features[-1]))


t = train_tree(dataset, misclassification)


print(all(t.predict(d) == out for (d, out) in dataset))

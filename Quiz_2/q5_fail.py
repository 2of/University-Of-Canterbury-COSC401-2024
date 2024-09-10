class DTNode(): 
    def __init__(self, decision):
        self.children = []
        self.decision = decision
    

    def predict(self, x): 
        if len(self.children) == 0:
            #is leaf
            return self.decision
        if callable(self.decision):
            m = self.decision(x)
            return self.children[m].predict(x)

        else:
            return self.decision



def get_proportion(classification, dataset):
    return 1 - (len(dataset) - len([x for x in dataset if x[1] == classification])) / len(dataset)


def misclassification(dataset):
    ks = list(set(x[1] for x in dataset))
    classifications = [(x, get_proportion(x, dataset)) for x in ks]
    if not classifications:
        # fix error
        return 0
    
    return 1 - max([x[1] for x in classifications])


def partition_by_feature_value(dataset,feature_index):
    ''' non binary implemementation of question 3'''
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
    return (create_function(feature_index), [lpart, rpart])





def train_tree(dataset, criterion):
    '''
    recursively build dtnodes 
    for tree 
    '''

    labels = [x[1] for x in dataset]
    #base_1
    print("dataset at node" , dataset)





    if all(x == labels[0] for x in labels):
        # print("CALLED")

        return DTNode(labels[0])

    #base_2


    if len(dataset[0][0]) == 0:
        print("CALLED2")
        return DTNode(labels[0]) 
    


    #get best feature 

    impurity = 0
    impurity = float('inf')
    
    for feature_column in range(len(dataset[0][0])):
        decision, datalabels_split = partition_by_feature_value(dataset, feature_column)
        col_impurity = sum([criterion(x) * len(x) / len(dataset) for x in datalabels_split])

        #For optimizations, each node at layer n is computing the same datalabels splts and impurity, we could load that back to some variable somewhere?
        # key on ? 

        


        # notes 3.2 ? 
        # print(col_impurity, datalabels_split)
        if col_impurity < impurity:
            # shouuuld be okay for the case where there are multiple of the same best choices in order
            impurity = col_impurity
            partitions = datalabels_split
            decision_for_node = decision   






    print ("best partitions scheme _ old", datalabels_split)

    Node = DTNode(decision_for_node)
    for partition in partitions:

        Node.children.append(train_tree(partition, criterion))
        print("i", len(partitions))
    print("DONE")
    # print("reach end?")
    return Node
    


	
dataset = [
  ((True, True), False),
  ((True, False), True),
  ((False, True), True),
  ((False, False), False)
]
t = train_tree(dataset, misclassification)
print(t.predict((True, False)))
print(t.predict((False, False)))
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



# import random

# # Generate test data with dependent features and labels
# def generate_test_data(num_points):
#     test_data = []
#     for _ in range(num_points):
#         feature_1 = random.choice([0, 1])
#         feature_2 = feature_1 * 2
#         feature_3 = feature_2 * 2
#         label = random.choice([True, False])
#         test_data.append(((feature_1, feature_2, feature_3), label))
#     return test_data

# # Generate a large test dataset with 1000 data points
# test_data_large = generate_test_data(1000)

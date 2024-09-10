


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




from pprint import pprint
dataset = [
  (("a", "x", 2), False),
  (("b", "x", 2), False),
  (("a", "y", 5), True),
  (("c", "y", 5), False),
]
f, p = partition_by_feature_value(dataset, 1)
pprint(sorted(sorted(partition) for partition in p))
partition_index = f(("b", "y", 5))
# everything in the "y" partition for feature 1 has a y
print(all(x[1]=="y" for x, c in p[partition_index]))


from pprint import pprint
dataset = [
  ((True, True), False),
  ((True, False), True),
  ((False, True), True),
  ((False, False), False),
]
f, p = partition_by_feature_value(dataset,  0)
pprint(sorted(sorted(partition) for partition in p))

partition_index = f((True, True))
# Everything in the "True" partition for feature 0 is true
print(all(x[0]==True for x,c in p[partition_index]))
partition_index = f((False, True))
# Everything in the "False" partition for feature 0 is false
print(all(x[0]==False for x,c in p[partition_index]))






from pprint import pprint
dataset = [
  (("a", "x", 2), False),
  (("b", "x", 2), False),
  (("a", "y", 5), True),
  (("c", "y", 5), False),
]
f, p = partition_by_feature_value(dataset, 0)

for i in p:
     print(i)

print(f(("a", "x", 2)))
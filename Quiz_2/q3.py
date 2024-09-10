def partition_by_feature_value(dataset, feature_index):
    samplefeature = dataset[0][0][feature_index]
    lpart = list(filter(lambda x: x[0][feature_index] == samplefeature, dataset))
    rpart = list(filter(lambda x: x[0][feature_index] != samplefeature, dataset))
    

    def create_function(feauture_index):
            def sepfunc(feature_vec):
                if lpart[0][0][feature_index] == feature_vec[feature_index]:
                     return 0
                return 1
            return sepfunc
    return (create_function(feature_index), [lpart,rpart])





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
f, p = partition_by_feature_value(dataset, 1)
pprint(sorted(sorted(partition) for partition in p))
partition_index = f(("b", "y", 5))
# everything in the "y" partition for feature 1 has a y
print(all(x[1]=="y" for x, c in p[partition_index]))
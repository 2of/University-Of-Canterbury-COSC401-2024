import itertools


def all_possible_functions(X):
    table = list(itertools.product([False, True], repeat=len(X)))
    # domain = X
    def create_function(row):
        # We create a function which returns the row but doesnt care about the input?
        domain = list(X)
        def new_function(x):
            return row[domain.index(x)]
        return new_function
    
    return set(create_function(r) for r in table)



'''
            im a  fucking moron :)

'''

X = {"green", "purple","red"} # an input space with two elements
F = all_possible_functions(X)

# Let's store the image of each function in F as a tuple
images = set()
for h in F:

    images.add(tuple(h(x) for x in X))
    # print([h(x) for x in X] )
    
for image in sorted(images):
    print(image)
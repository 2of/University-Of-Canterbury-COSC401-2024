import itertools


def all_possible_functions(X):
    table = list(itertools.product([False, True], repeat=len(X)))
    
    # domain = X
    def create_function(row,pred):
        # We create a function which returns the row but doesnt care about the input?
        domain = list(X)
        def new_function(x):
            # print("\t testing on ", x, row[domain.index(x)])

            return row[domain.index(x)]
        return new_function
    return set(create_function(r,"green") for r in table)





def version_space2(H,D):
    #additive approach?
    vs = set()
    for h in H:
        for (k,v) in D:
            if (h(k) == v): 
                vs.add(h)
                print("adding ", k,v, "because h(x) is ", h(k))
    return vs


def version_space(H, D):
    # do we want all individual or not?
    vs = set(H) 
    for h in H:
        for (x, y) in D:
            if h(x) != y:
                vs.discard(h)
        
    return vs


X = {"green", "purple"} # an input space with two elements
D = {("green", True)} # the training data is a subset of X * {True, False}
F = all_possible_functions(X)
H = F # H must be a subset of (or equal to) F

VS = version_space(H, D)

print(len(VS))

for h in VS:
    for x, y in D:
        if h(x) != y:
            print("You have a hypothesis in VS that does not agree with the set D!")
            break
    else:
        continue
    break
else:
    print("OK")    
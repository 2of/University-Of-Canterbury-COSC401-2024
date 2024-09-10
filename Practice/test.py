def input_space(domains):
    
    
    
    
    def recurse(domains):
        if len(domains) == 0:
            return [[]]
        
        
        out = []
        
        permutations = recurse(domains[1:])
        
        for param in domains[0]:
            for perm in permutations:
                out.append([param]  +  perm)
                
        return out
    
    return [tuple(a) for a in recurse(domains)]
        

            





domains = [
{0, 1, 2},
{True, False},
]

# for element in sorted(input_space(domains)):
#     print(element)
    
    
import itertools


def all_possible_functions(X):
    table = list(itertools.product([False, True], repeat=len(X)))
    # domain = X
    domain = list(X)
    def create_function(row):
        # We create a function which returns the row but doesnt care about the input?

        print(domain)
        def new_function(x):    
            return row[domain.index(x)]
        return new_function
    return set(create_function(r) for r in table)

#







X = {"green", "purple"} # an input space with two elements
F = all_possible_functions(X)

# Let's store the image of each function in F as a tuple
images = set()
for h in F:
    images.add(tuple(h(x) for x in X))

for image in sorted(images):
    print(image)



X = {('red','large'), ('green', 'large'), ('red', 'small'), ('green', 'small')}
F = all_possible_functions(X)

# Let's store the image of each function in F as a tuple
images = set()
for h in F:
    images.add(tuple(h(x) for x in X))

for image in sorted(images):
    print(image)
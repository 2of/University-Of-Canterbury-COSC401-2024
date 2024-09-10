




import itertools


def decode(coords):
    # table = list(itertools.product([False, True], repeat=len(X)))
    # x1,y1,x2,y2 = coords
    # print (x1,x2,y1,y2)
    # domain = X
    def create_function(coords):
        x1,y1,x2,y2 = coords


        x1,x2 = sorted([coords[0], coords[2]])
        y1,y2 = sorted([coords[1], coords[3]])
        # We create a function which returns the row but doesnt care about the input?
        def new_function(point):
            x,y = point
            return(x >= x1 and x <= x2 and y >= y1 and y <= y2)
        return new_function
    
    
    return create_function(coords)



import itertools

h = decode((-1, -1, 1, 1))

for x in itertools.product(range(-2, 3), repeat=2):
    print(x, h(x))

print("___")
import itertools

h1 = decode((1, 4, 7, 9))
h2 = decode((7, 9, 1, 4))
h3 = decode((1, 9, 7, 4))
h4 = decode((7, 4, 1, 9))


for x in itertools.product(range(-2, 11), repeat=2):
    if len({h(x) for h in [h1, h2, h3, h4]}) != 1:
        print("Inconsistent prediction for", x, h(x))
        break
else:
    print("OK")
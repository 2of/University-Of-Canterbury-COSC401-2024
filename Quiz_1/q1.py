

def input_space(domains):
     
    def input_space_recurse(domains):
            if len(domains) == 0:
                return [[]]
            permutations = input_space_recurse(domains[1:])
            out = []
            for param in domains[0]:
                    for perm in permutations:

                        out.append([param] + perm)
            return out



    return [tuple(b) for b in input_space_recurse(domains)]



 

domains = [
{"green", "purple"},
{True, False}
]

for element in sorted(input_space(domains)):
    print(element)
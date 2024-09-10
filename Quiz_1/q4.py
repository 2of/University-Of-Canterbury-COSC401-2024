
def less_general_or_equal2(ha, hb, X): 
    # if ha == hb:
    #     return True

    ha_t = sum([ha(x) for x in X])

    hb_t = sum([hb(x) for x in X])



    return ha_t <= hb_t



def less_general_or_equal(ha, hb, X):
    # okay, this is the only way I can satisfy the h2 => h3 false and h3 => h2 false clause
    for x in X:
        if ha(x) > hb(x):
            return False
    return True

X = list(range(1000))

def h2(x): return x % 2 == 0
def h3(x): return x % 3 == 0
def h6(x): return x % 6 == 0

H = [h2, h3, h6]

for ha in H:
    for hb in H:
        print(ha.__name__, "<=", hb.__name__, "?", less_general_or_equal(ha, hb, X))


        https://r.revera.bieszczady.pl/firstbestshop12/
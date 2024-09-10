def linear_regression_1d(data):
    def dot_product(v1,v2):
        return sum(a * b for a, b in zip(v1, v2))
    n = len(data)
    
    x = [a[0] for a in data]
    y = [a[1] for a in data]
    sum_x = sum(x)
    sum_y = sum(y)
    
    m = (n * dot_product(x,y) - sum_x * sum_y)/(n * dot_product(x,x) - (sum_x)**2)
    c = (sum_y - m*sum_x) / n 
    return (m,c)


    return (m, c)
data = [(1, 4), (2, 7), (3, 10)]
m, c = linear_regression_1d(data)
print(m, c)
print(4 * m + c)
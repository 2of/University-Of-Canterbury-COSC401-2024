from math import pi, exp, sqrt

def likelihood(sample, mu, sigma):
    
    
    
    

    def normal_pdf(x, mu, sigma):
        a = 1 / (sqrt(2 * pi) * sigma)
        b = -((x - mu) ** 2) / (2 * sigma ** 2)
        pdf_value = a * exp(b)
        return pdf_value
    
    
    result = 1
    
    
    #whoops, summed instead of product-ed, fixed
    for prob in [normal_pdf(a, mu, sigma) for a in sample]:
        result *= prob
        
    return result







mu = 0
sigma = 1
samples = [0.2]
print(f"{likelihood(samples, mu, sigma):.4f}")

x


mu = 0
sigma = 1
samples = [-2.2]
print(f"{likelihood(samples, mu, sigma):.4f}")




from statistics import NormalDist
import random
random.seed(0xc0ffee)
mu = 0
sigma = 1
distribution = NormalDist(mu, sigma)
print(f"{likelihood(distribution.samples(5), mu, sigma):.4f}")




from statistics import NormalDist
import random
random.seed(0xc0ffee)
mu = 0
sigma = 1
distribution = NormalDist(mu, sigma)
print(f"{likelihood(distribution.samples(10), mu, sigma):.4e}")
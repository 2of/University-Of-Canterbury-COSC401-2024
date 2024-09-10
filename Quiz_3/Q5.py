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



def most_likely(samples, distributions):
    max_likelihood = -1
    max_mu = -1
    max_sigma = -1
    
    for i, (mu, sigma) in enumerate(distributions):
        lh = likelihood(samples, mu, sigma)
        if lh > max_likelihood:
            max_likelihood = lh
            max_mu = mu
            max_sigma = sigma
    return (max_mu, max_sigma)


samples = [0.1]
distributions = [(0, 1), (-2, 3)]
mu, sigma = most_likely(samples, distributions)
print(f"Sample most likely has mean {mu} and standard deviation {sigma}")



samples = [0.5]
distributions = [(0, 1), (0, 0.5)]
mu, sigma = most_likely(samples, distributions)
print(f"Sample most likely has mean {mu} and standard deviation {sigma}")
samples = [-2.1, -2.01, -1.98, -1.72, -2.11, 0.1, 2.1]
distributions = [(2, 1), (-2, 1), (3, 2)]
mu, sigma = most_likely(samples, distributions)
print(f"Sample most likely has mean {mu} and standard deviation {sigma}")


	
from statistics import NormalDist
from random import seed
from itertools import product
seed(0x5eeded)
mus = range(-10, 11)
sigmas = range(1, 3)
distributions = product(mus, sigmas)
true = NormalDist(mu=3.1, sigma=1.9)
mu, sigma = most_likely(true.samples(20), distributions)
print(f"Sample most likely has mean {mu} and standard deviation {sigma}")

from math import sqrt

def max_log_likelihood_estimator(samples):
    n = len(samples)
    
    def mu_star_func(xs,n):
        coefficient1 = 1/n
        return coefficient1 * sum(x for x in samples)
        #this feels wrong, algebra?
    
    def sigma_star_func(xs,n, sigma_star):
        coefficient1 = 1/n
        under_root_sign = sum((x-sigma_star)**2 for x in samples)
        return sqrt(coefficient1 * under_root_sign)

    mu_star = mu_star_func(samples,n)
    sigma_star = sigma_star_func(samples,n, mu_star)
    
    
    return(mu_star,sigma_star)




samples = [-0.5, 0.5]
mu, sigma = max_log_likelihood_estimator(samples)
print(mu == 0, sigma == 0.5)



import numpy as np
samples = np.full(100, -0.25)
mu, sigma = max_log_likelihood_estimator(samples)
print(mu == -0.25, sigma == 0)


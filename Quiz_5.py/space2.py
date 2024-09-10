import random
import numpy as np

class weighted_bootstrap:
    def __init__(self, dataset, weights, sample_size, seed=0):
        self.dataset = dataset
        self.weights = weights
        self.sample_size = sample_size
        random.seed(seed)

    def __iter__(self):
        return self

    def __next__(self):
        i = random.choices(range(len(self.dataset)), weights=self.weights, k=self.sample_size)
        sample = self.dataset[i]
        return sample
    
    
def adaboost(learner, dataset, n_models):
    
    x,y = dataset[:, :-1], dataset[:, -1]
    
    sample_size = len(dataset)
    models = []
    alphas = []
    weights = np.ones(sample_size) / sample_size
    
    for t in range(n_models):
        

        bootstrap = weighted_bootstrap(dataset, weights, sample_size)
        sample_dataset = next(bootstrap)
        model = learner(sample_dataset)
        models.append(model)
        predictions = np.array([model(x[i, :]) for i in range(sample_size)])
        misclassified = (predictions != y)
        
    
        
        error = np.sum(weights[misclassified])
        
        
        
        if error == 0 or error >= 0.5:
            break
        
        
        alpha = error / (1-error)
        alphas.append(alpha)
    
        # Update weights
        for i in range(sample_size):
            if misclassified[i]:
                pass
            else:
                weights[i] *= np.exp(alpha)

        # Normalize weights
        weights /= np.sum(weights)
        
        
    def classifier(x):
        class_weights = {cls: 0 for cls in np.unique(y)}

        # For each model t
        for model, alpha in zip(models, alphas):
            predicted_class = model(x)
            class_weights[predicted_class] += -np.log(alpha / (1 - alpha))

        final_pred = max(class_weights, key=class_weights.get)
        return final_pred

 
    return classifier
        
        
    
    #could also normalize maybe?
    
    
    
    
    
    
    print(len(weights), sample_size)
    
    for t in range(n_models):
        pass
        

    
    
    
    pass    
    
import sklearn.datasets
import sklearn.utils
import sklearn.linear_model

digits = sklearn.datasets.load_digits()
data, target = sklearn.utils.shuffle(digits.data, digits.target, random_state=3)
train_data, train_target = data[:-5, :], target[:-5]
test_data, test_target = data[-5:, :], target[-5:]
dataset = np.hstack((train_data, train_target.reshape((-1, 1))))

def linear_learner(dataset):
    features, target = dataset[:, :-1], dataset[:, -1]
    model = sklearn.linear_model.SGDClassifier(random_state=1, max_iter=1000, tol=0.001).fit(features, target)
    return lambda v: model.predict(np.array([v]))[0]

boosted = adaboost(linear_learner, dataset, 10)
for (v, c) in zip(test_data, test_target):
    print(int(boosted(v)), c)
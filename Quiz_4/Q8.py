from collections import namedtuple

class ConfusionMatrix(namedtuple("ConfusionMatrix",
                                "true_positive false_negative "
                                "false_positive true_negative")):

    def __str__(self):
        elements = [self.true_positive, self.false_negative,
                self.false_positive, self.true_negative]
        return ("{:>{width}} " * 2 + "\n" + "{:>{width}} " * 2).format(
                    *elements, width=max(len(str(e)) for e in elements))
                    
def confusion_matrix(classifier, dataset):
    
    fp = 0
    tp = 0
    fn = 0
    tn = 0
    
    for feats, goal in dataset:
        result = classifier(feats)
        
        if goal == 0:
            if result == 0:
                tn += 1
            elif result == 1:
                fp += 1
        if goal == 1:
            if result == 1:
                tp += 1
            elif result == 0:
                fn += 1
                
    a = ConfusionMatrix(tp, fn, fp, tn)
    return a

	
print(confusion_matrix(lambda x: x, []))

dataset = [
    ((0.8, 0.2), 1),
    ((0.4, 0.3), 1),
    ((0.1, 0.35), 0),
]
print(confusion_matrix(lambda x: 1, dataset))
print()
print(confusion_matrix(lambda x: 1 if x[0] + x[1] > 0.5 else 0, dataset))
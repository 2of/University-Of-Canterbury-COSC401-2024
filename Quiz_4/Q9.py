from collections import namedtuple

class ConfusionMatrix(namedtuple("ConfusionMatrix",
                                "true_positive false_negative "
                                "false_positive true_negative")):


    def __str__(self):
        elements = [self.true_positive, self.false_negative,
                self.false_positive, self.true_negative]
        return ("{:>{width}} " * 2 + "\n" + "{:>{width}} " * 2).format(
                    *elements, width=max(len(str(e)) for e in elements))
                    



def dominates(m_1, m_2):
    if (m_1.true_positive > m_2.true_positive and
        m_1.false_negative < m_2.false_negative and
        m_1.false_positive < m_2.false_positive and
        m_1.true_negative > m_2.true_negative):
        return True
    return False
    
def roc_non_dominated(classifiers):
    ret = []
    for label, matrix in classifiers:
        is_dominated = False
        for _, matrix2 in classifiers:
            if matrix2 != matrix:
                if dominates(matrix2, matrix):
                    is_dominated = True
                    break
        if not is_dominated:
            ret.append((label, matrix))
    return ret
        






# # Example similar to the lecture notes

classifiers = [
    ("h1", ConfusionMatrix(60, 40, 
                            20, 80)),
    ("h2", ConfusionMatrix(40, 60, 
                            30, 70)),
    ("h3", ConfusionMatrix(80, 20, 
                            50, 50)),
]
print(sorted(label for (label, _) in roc_non_dominated(classifiers)))






import csv

classifiers = []
with open("performance-data-small.csv") as file:
    data = csv.reader(file)
    header = next(data)
    for row in data:
        model_config, *performance = row
        tp, fn, fp, tn = map(int, performance)
        classifiers.append((model_config, ConfusionMatrix(tp, fn, fp, tn)))

names = [name for name, _ in roc_non_dominated(classifiers)]
for name in sorted(names):
    print(name)
    
    
classifiers = [
    ("h1", ConfusionMatrix(5, 5,
                                 3, 7)),
]
print([l for (l, _) in roc_non_dominated(classifiers)])
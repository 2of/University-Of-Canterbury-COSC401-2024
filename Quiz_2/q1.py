class DTNode(): 
    def __init__(self, decision):
        self.children = []
        self.decision = decision
    

    def leaves(self):
        if len(self.children) == 0:
            return 1
        return sum([self.children[x].leaves() for x in range(0,len(self.children))])



        return len(self.children)

    def predict(self, x): 
        # print(self.__class__.__name__)
        # print("PREDICT GOT", x)
        if len(self.children) == 0:
            #is leaf
            return self.decision
        if callable(self.decision):
            m = self.decision(x)
            return self.children[m].predict(x)
            pass

        else:
            return self.decision



yes_node = DTNode("Yes")
no_node = DTNode("No")
tree_root = DTNode(lambda x: 0 if x[2] < 4 else 1)
tree_root.children = [yes_node, no_node]

print(tree_root.predict((False, 'Red', 3.5)))
print(tree_root.predict((False, 'Green', 6.1)))


# The following (leaf) node will always predict True
node = DTNode(True) 

# Prediction for the input (1, 2, 3):
x = (1, 2, 3)
print(node.predict(x))

# Sine it's a leaf node, the input can be anything. It's simply ignored.
print(node.predict(None))


print("My own test-----------")



n0 = DTNode(lambda x: 0 if x <= 9 else 1)

n1 = DTNode(lambda x: 0 if x % 5 != 0 else 1)
n2 = DTNode(lambda x: 0 if x > 100 else 1)
n3 = DTNode("end - n3")
n4 = DTNode(lambda x: 0 if x <= 20 else 1)
n5 = DTNode("end - n5")
n6 = DTNode("end - n6")
n7 = DTNode("end - n7")
n8 = DTNode("end - n8")


n4.children = [n7,n8]
n1.children = [n3,n4]
n2.children = [n5,n6]
n0.children = [n1,n2]

print(n0.predict(4))
print(n0.predict(5))
print(n0.predict(6))





n = DTNode(True)
print(n.leaves())


t = DTNode(True)
f = DTNode(False)
n = DTNode(lambda v: 0 if not v else 1)
n.children = [t, f]
print(n.leaves())



	
tt = DTNode(False)
tf = DTNode(True)
ft = DTNode(True)
ff = DTNode(False)
t = DTNode(lambda v: 0 if v[1] else 1)
f = DTNode(lambda v: 0 if v[1] else 1)
t.children = [tt, tf]
f.children = [ft, ff]
n = DTNode(lambda v: 0 if v[0] else 1)
n.children = [t, f]

print(n.leaves())
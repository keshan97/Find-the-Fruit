from sklearn import tree

# smooth = 1 and bumpy =0
features = [[140, 1], [130, 1], [150, 0], [170, 0],
            [135, 1], [142, 1], [151, 1], [165, 0]]

# apple = 0 and oranges = 1
labels = [0, 0, 1, 1, 0, 0, 0, 1]

# making the classifier
cf = tree.DecisionTreeClassifier()


# Set Values to the classifier
cf = cf.fit(features, labels)

x = int(input("Enter the Weight "))
y = int(input("Enter the physical feature ; Smooth = 1 & Bumpy = 0 "))


pred = cf.predict([[x, y]])

if (pred == 1):
    print('An Orange is identified')
elif (pred == 0):
    print('An Apple is identified')
else:
    print('Undefined Fruit!')

print()
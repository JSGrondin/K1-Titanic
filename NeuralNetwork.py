# Load relevant packages and modules
import pandas as pd
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from sklearn.metrics import accuracy_score
from keras.optimizers import SGD

# Load cleaned and formatted train and test data files (see Clean_and_format.py)
train = pd.read_csv('train_cleaned.csv')
test = pd.read_csv('test_cleaned.csv')

# Create the features numpy arrays
X_train = train[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked_0', 'Embarked_1', 'FamilySize', 'IsAlone', 'Title']].values
X_test = test[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked_0', 'Embarked_1', 'FamilySize', 'IsAlone', 'Title']].values

# Convert the target to categorical (which is what is needed by the Neural Network
target = train['Survived']
Y_train = to_categorical(target)

# Calculate # of features
n_cols = X_train.shape[1]

# Specify the model
model = Sequential()
model.add(Dense(200, activation='relu', input_shape = (n_cols,)))
model.add(Dense(200, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X_train, Y_train)

# Calculate predictions for train and test samples
train_prediction = model.predict(X_train)
my_prediction = model.predict(X_test)

# Create a data frame with two columns: PassengerId & Survived. Survived contains my predictions
PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame((my_prediction[:,1] > 0.5).astype(np.int), PassengerId, columns = ["Survived"])
print(my_solution)
print(accuracy_score(train['Survived'].values, (train_prediction[:,1] > 0.5).astype(np.int)))

# Write Solution to a csv file with the name my_solution.csv
my_solution.to_csv('my_solution.csv', index_label=['PassengerId'])
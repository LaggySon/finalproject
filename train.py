import pandas as pd
import numpy as np
df = pd.read_csv('./data/2018_03.csv')
df = df.loc[df['type'] == 'NJ Transit']
newdata = df.dropna()
X = newdata[['from_id', 'to_id']]
y = newdata['delay_minutes']

# from sklearn.feature_extraction import DictVectorizer
# vec = DictVectorizer(sparse=False, dtype=int)
# print(vec.fit_transform(df))



from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import SGDRegressor
model = SGDRegressor()
model.fit(Xtrain,ytrain)
y_model = model.predict(Xtest)

from joblib import dump, load 
dump(model, 'mymodel.joblib') #save  
model2 = load('mymodel.joblib')  #load

[0,1,0,0,0,0,0,0,0,0,0,5]
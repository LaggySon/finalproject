import pandas as pd
import numpy as np
import os
import glob
files = os.path.join('./data/', '20*.csv')
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
data = df[['line','stop_sequence','delay_minutes']]
newdata = data.dropna()

newdata_dict = newdata.to_dict(orient='records') # turn each row as key-value pairs

from sklearn.feature_extraction import DictVectorizer
# instantiate a Dictvectorizer object for X
dv_newdata = DictVectorizer(sparse=False) 
# sparse = False makes the output is not a sparse matrix
# apply dv_X on X_dict
newdata_encoded = dv_newdata.fit_transform(newdata_dict)

X = newdata_encoded[:,1:]
y = newdata_encoded[:,0]

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.20, random_state=1)

from sklearn.linear_model import SGDRegressor
model = SGDRegressor(loss='huber')
model.fit(Xtrain,ytrain)

from joblib import dump, load
dump(model, 'mymodel.joblib') #save
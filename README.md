## ABOUT

predict delay from the line name, origin, and destination of the trip
predict 'delay_minutes' from 'line', 'from' and 'to'

# Step 1:

Clean data - remove all data that doesn't have delay_minutes

- anything with type=Amtrak
- remove all unecessary columns

# Step 2:

Our y will be 'delay_minutes' and our X will be 'line', 'from', and 'to'

# Step 3:

We chose SGDRegressor as our model (using https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)

# Step 4:

Use pandas to get data from csv and input to model

- split data into train and test subsets (80% train, 20% test)

# Step 5:

Predict and plot

# Step 6:

deploy

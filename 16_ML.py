import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from joblib import Parallel, delayed 
import joblib 
import streamlit as st
st.header(':blue[PREDICT OCCUPANCY BASED ON HISTORICAL DATA]', divider="gray")
st.subheader('We have a synthetic data of 2023. Based on that we use Descision Tree regression to predict occupancy on a given day')
st.subheader(':red[Historical data of 2023:]')
occu = pd.read_excel(f'scheduller/schedule.xlsx',sheet_name="2023")
st.write(occu)

# occu.DAY.unique()


# Replace multiple values at once
occu.replace({'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}, inplace=True)
# Replace multiple values at once
occu.replace({True: 1, False: 0}, inplace=True)



predictor_var= occu.drop(["DATE", "OCCUPANCY"], axis=1) #all columns except the last one
target_var= occu["OCCUPANCY"] #only the last column
X = occu.drop(["DATE", "OCCUPANCY"], axis=1)
y = occu["OCCUPANCY"]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)

param_grid = [{"max_depth":[3,4,5, None], "max_features":[2,3]}]
gs = GridSearchCV(estimator=DecisionTreeRegressor(random_state=123),param_grid = param_grid,cv=10)


gs.fit(X_train, y_train)

# gs.cv_results_['params']
# gs.cv_results_['rank_test_score']

tree = gs.best_estimator_

predictions = tree.predict(X_test)

df=pd.DataFrame({'Actual':y_test, 'Predicted':predictions})
#df.head(5) #Check the top 5 predictions and actual values.


# Save the model as a pickle in a file 
joblib.dump(tree, 'model.pkl') 
  
# Load the model from the file 
dtree_from_joblib = joblib.load('model.pkl') 
  
# Use the loaded model to make predictions 
predictions3=dtree_from_joblib.predict(X_test) 

df=pd.DataFrame({'Actual':y_test, 'Predicted3':predictions3})
df.head(5) #Check the top 5 predictions and actual values.


from sklearn import metrics
# st.write('Mean Absolute Error:', metrics.mean_absolute_error(y_test,predictions))
# st.write('Mean Squared Error:', metrics.mean_squared_error(y_test,predictions))
# st.write('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test,predictions)))
# st.write('r2_score:', metrics.r2_score(y_test,predictions))


# tree.feature_importances_
# st.write(pd.Series(tree.feature_importances_,index=predictor_var.columns).sort_values(ascending=False))

st.subheader(':red[Select the Day Month and Check if its a Public Holiday:]')

days_list=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

month_sel=[1,2,3,4,5,6,7,8,9,10,11,12]


public_hol=['YES','NO']

sel_day=st.selectbox("Select day",days_list)

sel_public_hol=st.selectbox("Select if its public holiday or no",public_hol)

sel_month=st.selectbox("Select the month",month_sel)

# initialize data of lists.
data = {'MONTH': [sel_month],
        'DAY': [sel_day],
        'PUBLIC HOLIDAY':[sel_public_hol]
        }

# Create DataFrame
input_data = pd.DataFrame(data)


# st.write(input_data)

# Replace multiple values at once
input_data.replace({'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}, inplace=True)
# Replace multiple values at once
input_data.replace({'YES': 1, 'NO': 0}, inplace=True)

# st.write(input_data)


predicted_occupancy=(dtree_from_joblib.predict(input_data))

st.write("Predicted Occupancy: "+str(int(predicted_occupancy[0]))+" %")


if predicted_occupancy[0]<25:
    st.write(":blue[Run Fewer buses on this day]")
elif predicted_occupancy[0]>=25 and predicted_occupancy[0]<=100:
    st.write(":green[Keep the Schedule same]")
else:
    st.write(":red[Run More busses on this route and increase frequency]")



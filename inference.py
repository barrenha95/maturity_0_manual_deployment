import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression


#new data example
new_data = {
    'CreditScore'    : [686],
    'Geography'      : ['Spain'],
    'Age'            : [27],
    'Tenure'         : [8],
    'Balance'        : [2953.00],
    'NumOfProducts'  : [2],
    'HasCrCard'      : [1],
    'IsActiveMember' : [0],
    'EstimatedSalary': [11745.29]
}

# transforming new data into pandas dataframe
df_new_data = pd.DataFrame(new_data)

# encoding string column
country_dict = {"France" : 1,
                "Germany": 2,
                "Spain"  : 3}

df_new_data["Geography"] = df_new_data.Geography.apply(lambda x: country_dict[x])

# applying scaler
scaler_lr = joblib.load('scaler_lr.pkl')
df_new_data = scaler_lr.transform(df_new_data)

# running model
lr_model = joblib.load('lr_model_v1.pkl')
prediction = lr_model.predict(df_new_data)

# interpreting the result
if prediction > 0.50:
    print("This customer will probably not become a churn!")
else:
    print("This customer will probably become a churn!")






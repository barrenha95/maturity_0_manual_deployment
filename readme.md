This repository was created to demonstrate skills in machine learning deployment, specifically showing how a deployment is made with the level 0 of maturity, or in other words, the simplest way possible:
- manually running each deployment 
- manually processing each run request

## Objetcives
- Show the simplest way to deploy a churn machine learning model applied to a bank scenario
- **The objective is not to make the best model.** The focus of this project is to show how a deployment of a machine learning model is made. In other words, the statistical part of the model is there only as a fast example.


## Content 
*Direct from the Kaggle page*

Data obtained from:
https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers?resource=download

- RowNumber: corresponds to the record (row) number and has no effect on the output.
- CustomerId: contains random values and has no effect on the customer leaving the bank.
- Surname: The surname of a customer has no impact on their decision to leave the bank.
- CreditScore: can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.
- Geography: a customer’s location can affect their decision to leave the bank.
- Gender: It’s interesting to explore whether gender plays a role in a customer leaving the bank.
- Age: This is certainly relevant, since older customers are less likely to leave their bank than younger ones.
- Tenure: refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.
- Balance: also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.
- NumOfProducts: refers to the number of products that a customer has purchased through the bank.
- HasCrCard: denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank.
- IsActiveMember: Active customers are less likely to leave the bank.
- EstimatedSalary: As with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.
- Exited: whether or not the customer left the bank.


## Steps
To make the project more similar to real-life problems, I split it into small tasks.
As the project progresses, I will add the time spent on each task. 

1. Problem Selection & Setup: Choose a simple dataset (e.g., Iris, Titanic), define objective (classification or regression), set up local environment (Python, Jupyter). **41 minutes**
2. Data Exploration & Cleaning: Load the data, do basic cleaning (missing values, types), and basic EDA (plots, stats). **45 minutes**
3. Feature Engineering & Selection: Select relevant features, do basic encoding or scaling, create train/test split. **38 minutes**
4. Model Training: Train a simple model (e.g., Logistic Regression or Decision Tree), evaluate it using basic metrics. **57 minutes**
5. Manual Inference Script: Write a Python script that loads the model and takes manual input (or reads a file) to make predictions.
6. Manual "Deployment": Create a local folder structure and document the steps to run: train, evaluate, and predict. Nothing is automated.
7. Documentation: Write a README explaining how to run each script manually. Mention which files to edit or execute.
8. Testing the Manual Process: Simulate being a user: clone the project, run everything manually from scratch, and fix any issues.
9. Reflection & Publication Prep: Write a summary (for LinkedIn or blog): what this maturity level is, what you did, what’s missing, and the next steps.
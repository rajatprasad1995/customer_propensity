# customer_propensity
This repository contains the code for creating a flask application that deploys a machine learning model that predicts whether a customer will accept an offer for a new credit card. The file **predictor.py** contains the code for the application.

An excel file **NewCashCard_assignment.xlsx** that is available in the data directory contains data of all the customers that accepted or rejected the offer in the past.

This dataset was used to build a logistic regression model that calculated the propensity of a customer willing to accept the credit card. The model is saved in the directory **model** and is called **finalized_model.sav**

The notebook **notebook/notebook_for_modeling.ipynb** is where I analyzed the data and trained the machine learning model.

Initially the model was built by one variable and then other variables were included until the performance of the model stopped improving.

The threshold was decided based on the cost matrix. If there are too many false positives the bank would lose money, 20$ to be exact as that is the cost of offering the credit card. If there is false negative, the loss is much higher. Hence
a low threhold was decided.

You can find the application deployed at the link given below and do checkout the notebook **notebook/notebook_for_modeling.ipynb** used to build the model. 

<https://bank-logit.herokuapp.com/>

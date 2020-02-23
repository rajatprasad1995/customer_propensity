# customer_propensity
This repository contains the code for creating a flask application that deploys a machine learning model that calculates propensity of acceptance by a customer for a credit card offer.

Data set that accounted for all the customers in the bank that accepted or rejected the credit card offered by the bank. You can find the data set in the excel file included in this repository.
This dataset was used to build a logistic regression model that calculated the propensity of a customer willing to accept the credit card.

Initially the model was built by one variable and then other variables were included until the performance of the model stopped improving.

The threshold was decided based on the cost matrix. If there are too many false positives the bank would lose money, 20$ to be exact as that is the cost of offering the credit card. If there is false negative, the loss is much higher. Hence
a low threhold was decided.

You can find the application at the link given below and do checkout the notebook used to build the model. 

<https://bank-logit.herokuapp.com/>

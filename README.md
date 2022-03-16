# Capstone-SBPS
Project submitted as part of Upgrad's PGDAIML Course - Feb 2021

# Sentiment Based Product Recommendation System

## Problem Statement:
Ebuss has captured a huge market share in many fields, and it sells the products in various categories such as household essentials, books, personal care products, medicines, cosmetic items, beauty products, electrical appliances, kitchen and dining products and health care products.

With the advancement in technology, it is imperative for Ebuss to grow quickly in the e-commerce market to become a major leader in the market because it has to compete with the likes of Amazon, Flipkart, etc., which are already market leaders.

As a senior ML Engineer, you are asked to build a model that will improve the recommendations given to the users given their past reviews and ratings.

## Approach:
In order to do this, we plan to build a sentiment-based product recommendation system, which includes the following key steps.

* Step 1 : Data sourcing and sentiment analysis
* Step 2 : Building a recommendation system
* Step 3 : Improving the recommendations using the sentiment analysis model
* Step 4 : Deploying the end-to-end project with a user interface

Following are the details of tasks to be performed Under Step 1:

* Exploratory data analysis
* Data cleaning
* Text preprocessing
* Feature extraction - Extract features from the text data, we have an option to choose from any of the methods, (including bag-of-words, 
TF-IDF vectorization)

---------
Our choice here would be to use TF-IDF vectorization
---------

* Training a text classification model - At least three out of the following four models need to be built (Post handling class imbalance and perform hyperparameter tuning).

* Logistic regression
* Random forest
* XGBoost
* Multinomial Naive Bayes

Our choice here would be to build Logistic Regression, Naive Bayes(Multinomial) and Random Forest models. We will then select the best performing models among these based on Recall. This best sentiment model will then be used for product recommendation.

Rationale : Recall in the current context is the number of correct recommendations divided by the number of recommendations that should have been returned. Here, we would like to maximize Recall as this can translate to better conversion rates for our e-commerce company.

Following are the details of tasks to be performed Under Step 2 & Step 3:

## Build the following Recommendation Systems

* User-based recommendation system
* Item-based recommendation system
We will analyse the recommendation systems and select the one that is best suited in this case.

Once we get the best-suited recommendation system, the next task is to recommend 20 products that a user is most likely to purchase based on the ratings.

Post this , we will filter out the 5 best products based on the sentiments of the 20 recommended product reviews.


## Heroku app (Flask Deployment)
We will build a web application using Flask framework,To make the web application public, we'll use Heroku.

The following features will be provisioned on the user interface.

* TextBox to Take any of the existing usernames as input.
* A submit button to submit the username.
* Once you press the submit button, it will recommend 5 products based on the entered username.

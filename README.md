# CreditCard

This code allows a website to charge user for products using credit card. Stripe is used as the platform to perform transaction. Each Transaction is based on a user, i.e a person has to login and create an account to complete a trasaction, on signing up a stripe ID is associated with the user and all transactions are based on that stripe ID. 

To Run the project 

** Fire the django Server 

** Navigate to http://127.0.0.1:8000/ in browser and you will hit the home page.

** Sign up on the home page 

** Navigate to http://127.0.0.1:8000/checkout/ to create a credit card transaction

** use card number as 4242424242424242 this is a test Card number provided by Stripe and make a transaction. 

** 10$ will be charged to the card and will reflect in users Stripe account


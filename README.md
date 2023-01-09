# Applied Data Science Pricing Competition

# INTRODUCTION
The purpose of this project was to participate in a class pricing competition based on the previous knowledge of demand estimation, revenue maximization, and pricing learned from the class. The project consists of two parts. Part one requires our team to come up with a pricing strategy based on the user valuation of an arbitrary product, opponent price, and history of sale. Part two requires our team to train a machine learning model and complete the tasks of demand estimation based on three user covariants, and revenue maximization to output the optimal price. Then based on this optimal price, we combine our strategy from part one to compete for customers. Each game will consist of two teams bidding prices for one customer without capacity constraints, the team with lower price under the valuation will win that round and gain revenue. Overall, the team with the most revenue across games will win the competition. As a result, we need to anticipate the moves of the opponent, and handle different situations with our algorithm. 

Specific techniques and strategies will be discussed extensively in the report below. 

# A: Demand estimation and price optimization (without competition)
For part two, demand estimation and price optimization, our goal was to train a machine learning model and complete the tasks of demand estimation based on three user covariants, and do revenue maximization to output the optimal price. Then based on this optimal price, we combine our strategy from part one to compete for customers.
Find Price Set and demand estimation
We built a logistic regression model, whose input was covariates and prices, and the output was -1, 0 or 1, which represented which item users bought. We trained the model using all the training data and got the demand result by using  predict_proba(). 
We wanted to find a set of prices which can be used in the calculation of max revenue. Thus, we plotted the demand curves of item_0 and item_1 which are shown below. We found that in the training set, for both item_0 and item_1, when the price goes larger than 30, the demand decreases to almost 0. Therefore, we set the price range to 0.1 to 30.


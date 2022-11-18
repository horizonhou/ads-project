import random
import pickle
import os
import numpy as np


class Agent(object):
    def __init__(self, agent_number, params={}):
        self.this_agent_number = agent_number  # index for this agent
        self.opponent_number = 1 - agent_number  # index for opponent
        self.project_part = params['project_part'] #useful to be able to use same competition code for each project part
        self.n_items = params["n_items"]

        self.alpha = 1.0
        self.iteration = 0

    def _process_last_sale(self, last_sale, profit_each_team):
        did_customer_buy_from_me = last_sale[1] == self.this_agent_number
        if did_customer_buy_from_me:  # can increase prices compared to itself
            self.alpha *= 1.05
        else:  # should decrease prices
            self.alpha *= 0.95

        # did_customer_buy_from_opponent = last_sale[1] == self.opponent_number
        # which_item_customer_bought = last_sale[0]
        # print("Did customer buy from me: ", did_customer_buy_from_me)
        # print("Did customer buy from opponent: ",
        #       did_customer_buy_from_opponent)
        # print("Which item customer bought: ", which_item_customer_bought)

        # my_current_profit = profit_each_team[self.this_agent_number]
        # opponent_current_profit = profit_each_team[self.opponent_number]
        # print("My current profit: ", my_current_profit)
        # print("Opponent current profit: ", opponent_current_profit)

        # my_last_prices = last_sale[2][self.this_agent_number]
        # opponent_last_prices = last_sale[2][self.opponent_number]
        # print("My last prices: ", my_last_prices)
        # print("Opponent last prices: ", opponent_last_prices)



    def action(self, obs):
        self.iteration += 1

        # For Part 1, new_buyer_covariates will simply be a vector of length 1, containing a single numeric float indicating the valuation the user has for the (single) item
        new_buyer_covariates, last_sale, profit_each_team = obs
       
        if self.project_part == 1:
            if self.iteration%3==0: #every now and then set the price higher to hike it up 
                self._process_last_sale(last_sale, profit_each_team)
                return [new_buyer_covariates[0]+1]
            elif self.iteration%100==0 and not self.iteration==0: #every 100 round reset alpha
                self.alpha = 1
                self._process_last_sale(last_sale, profit_each_team)
                return [new_buyer_covariates[0]*self.alpha]
            else: # adaptive
                self._process_last_sale(last_sale, profit_each_team)   
                return [new_buyer_covariates[0]*self.alpha]
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


    def action(self, obs):
        new_buyer_covariates, last_sale, state = obs
        self._process_last_sale(last_sale, new_buyer_covariates)
        return [random.random()*new_buyer_covariates[0]]

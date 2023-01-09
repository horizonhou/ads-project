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


    def action(self, obs):
        new_buyer_covariates, last_sale, profit_each_team = obs
        if self.iteration % 2 == 0:
            return [-10000000]
        else:
            return [new_buyer_covariates[0]-0.01]
        

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
        self.beta = 1.0
        self.iteration = 0
        self.alpha_competitor = []
        self.if_good = True

    def _process_last_sale(self, last_sale, profit_each_team, new_buyer_covariates):
        did_customer_buy_from_me = last_sale[1] == self.this_agent_number
        if did_customer_buy_from_me:  # can increase prices compared to itself
            self.alpha *= 1.1
        else:  # should decrease prices
            self.alpha *= 0.9
        
        self.price_me.append(last_sale[2][self.this_agent_number][0])
        self.price_competitor.append(last_sale[2][self.opponent_number][0])
        if self.iteration > 0:
            if last_sale[1] != self.this_agent_number:
                self.beta = self.price_competitor[-1]/self.buyer[-1]
            else:  # tit-or-tat
                self.beta = self.beta*1.1
        else:
            self.beta = 0.9
        self.alpha_competitor.append(self.price_competitor[-1]/self.buyer[-1])
        self.buyer.append(new_buyer_covariates[0])


    def action(self, obs):
        self.iteration += 1
        try: 
            new_buyer_covariates, last_sale, profit_each_team = obs

            if self.project_part == 1:
                if self.iteration==100: #check mean competitor alpha
                    self.alpha_competitor = [x for x in self.alpha_competitor if x<=1 and x>=0]
                    mean_competitor_alpha = np.mean(self.alpha_competitor)
                    self.if_good = (mean_competitor_alpha >= 0.5)
                    if not self.if_good :# evil team
                        self.alpha = mean_competitor_alpha*0.7
                
            
                self._process_last_sale(last_sale, profit_each_team, new_buyer_covariates)
                if self.if_good and self.iteration%100==0 and not self.iteration==0: #every 100 round, if the team is good, reset alpha
                    self.alpha = 1 
                if new_buyer_covariates[0]<5: #if valuation is low we allow opponent to win this round -> increase their alpha
                    return [new_buyer_covariates[0]+100000]
                elif self.alpha_competitor[-1]>1 or self.alpha_competitor[-1]<=0.85 or abs(self.alpha_competitor[-1]-self.alpha_competitor[-2])/self.alpha_competitor[-2]>0.2: # when they're evil use adaptive
                    return [new_buyer_covariates[0]*self.alpha]
                else:  # when they're rational use tit_for_tat
                    return [new_buyer_covariates[0]*(self.beta*0.9)]
        except:
            return [new_buyer_covariates[0]-0.001]

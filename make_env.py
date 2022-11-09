"""
From here mostly: https://github.com/openai/multiagent-particle-envs/blob/master/make_env.py
"""
from settings import *


import algopricing_opy.MultiAgentEnv_algopricing as MultiAgentEnv_algopricing
from algopricing_opy.MultiAgentEnv_algopricing import MultiAgentEnv_algopricing

# import algopricing.MultiAgentEnv_algopricing as MultiAgentEnv_algopricing
# from algopricing.MultiAgentEnv_algopricing import MultiAgentEnv_algopricing

def make_env_agents(agentnames, project_part = 1, params=None, first_file=None, second_file=None):
    import agents

    if project_part == 1 and params is None:
        params = default_params_1
    elif project_part == 2 and params is None:
        params = default_params_2

    agents = [
        agents.load(name + ".py").Agent(en, params)
        for en, name in enumerate(agentnames)
    ]
    env = MultiAgentEnv_algopricing(
        params, agentnames, project_part, len(
            agentnames), first_file, second_file
    )
    return env, agents

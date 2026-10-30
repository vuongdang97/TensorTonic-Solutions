import numpy as np

def value_iteration_step(values: list, transitions: list, rewards: list, gamma: float) -> list[float]:
    """
    Returns one updated floating-point value for every state.
    """
    # Write code here
    values = np.asarray(values)
    transitions = np.asarray(transitions)
    rewards = np.asarray(rewards)

    value_new = []
    dim_a = rewards.shape[1]
    dim_s = rewards.shape[0]
    for i in range(dim_s): 
        reward_curr = float('-inf')
        for j in range(dim_a):
            temp = rewards[i, j]
            temp = temp + gamma*np.dot(transitions[i, j, :], values)
            reward_curr = max(reward_curr, temp)
        value_new.append(reward_curr)
    return value_new
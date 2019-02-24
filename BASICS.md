# Basics and Defintions

- What is reinforcement learning(RL)?  
RL is a kind of machine learning in which the agent learns to behave
in an environment by observing the results of its actions.
- There are 3 approaches to RL: value based, policy based and model based.

### Definitions
- Agent: The entity which takes action is known as the agent(basically our algorithm!)
- Action(A): Actions are the set of all possible moves that an agent can make.
- Environment: The world in which the agent takes action(in model-based RL, this can
be considered as a black box which we must attempt to approximate).
- State(S): The instantaneous configuration of the environment.
- Reward(R): Feedback by which we measure the success or failure of the agent's actions.
Rewards can be immediate or delayed. When we just say reward, we usually mean the immediate one.
- Discount(\gamma): This is basically a fight against delayed gratification. Powers of \gamma are multiplied
by future rewards discovered by the agent to decrease their influence on the action which the agent chooses.
- Policy(\pi): Strategy that the agent employees to determine the next action based on
the current state. A policy maps a state to action(s). The policy can be deterministic or stochastic.  
Value(V): The expected long-term{as opposed to R, which is immediate} return with discount. V\pi(s) is defined as the expected long-term return
of the current state under policy \pi.
Q-value(aka action value): Similar to value, but it takes an extra parameter, the action 'a' as well.
Q\pi(s) refers to the long term return of the current state s, taking action a under policy pi.
Task: Instances of RL problems are called tasks. They can be episodic or continuous.
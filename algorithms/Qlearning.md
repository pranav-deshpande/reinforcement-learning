# Q learning

Make a table of dimensions no. of states × actions that can be taken at that state. Initialize the table. There are multiple ways to do so(either randomly or using the epsilon greedy strategy).
Then use the Bellman equation to update the table.  

The algorithm can be described briefly as follows:
1. Init Qtable with zeros.
2. Start an episode: [now we are at start pos]
3. Choose an action 'a' from the set of actions A(To choose this: we use the epsilon greedy strategy).
    - Define a number epsilon such that 0 < epsilon < 1
    - If value in table is less than epsilon, then choose a random action.
    - Else choose the action with the maximum reward.    
4. Perform action 'a'
5. Measure the reward R.
6. Update the Q table using the Bellman equation.
7. Keep repeating till we reach the end of the episode
8. Start again from (2) and repeat for the desired number of episodes.

Note that the Bellman Equation is given by:

![https://cdn-images-1.medium.com/max/800/1*2APPuDNSpWMlaiin7R0C9g.png](resources/bellman_equation.png)

### Deep Q Learning
Use a neural network  to approximate the Q learning table.
The network outputs [action, reward] pairs when a state is given as input.
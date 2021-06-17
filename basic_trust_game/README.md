# mTree Basic Trust Game Tutorial

This tutorial will step you through the development of a trust game experiment. The idea is that you will have a number of agents that will get paired with one another. One agent will then be given a sum of money to to then divide and they will then forward some to the other agent. When the money goes to the other agent, it will be multipled by some factor. This agent will then get a chance to send back some sum and keep some amount.

This tutorial will aim to help you understand how to pair agents off and then manage their actions. This will extend your knowledge of the address book and will help prepare you for human subject experiments

# Background to the Trust Game

[Original Trust Game Paper](https://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf)

# Sequence Diagram for the Trust Game

![Basic Auction Sequence Diagram](https://raw.githubusercontent.com/gmucsn/mTree_learning_exercises/main/basic_trust_game/trust_game_diagram.svg)

# Steps to build this tutorial

Prereqs. Step 0 - In this step you will simply need to create the corresponding directories for your code

1. Step 1 - In this step we will define our initial code files for an environment, an institution, and an agent

2. Step 2 - We will complete the code for the environment. This will be the place where you initialize a random ized pairing of the agents. 

3. Step 3 - We will now provide minimal code for our institution to deliver funds to the first agent.

4. Step 4 - We will now code the agents to be able to handle being the receiver of funds

5. Step 5 - We will now code the institution to receive the first agents decision, then multiply the funds, and send them along to the second agent

6. Step 6 - We will modify the agents to receive the multiplied funds and decide how to divide and return them.

7. Step 7 - We will modify the institution to return the funds to player 1.

8. Step 8 - We will modify the agent to receive the funds from the player's division and also to close out the round.

9. Step 9 - You will experiment with different agent implementations for divind funds.

10. Step 10 - You will extend the code so that multiple rounds can be run with different agent pairings.
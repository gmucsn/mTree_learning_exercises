# mTree Clock Auction Tutorial - Step 6

In this Step you'll be working on improving the agents bidding procedure. In the current implementation the agents simply bid from a starting point and then increment their bids based on some formula. One thing we can do is to alter the bid increments, bid the max amount immediately, change the starting bid, or randomly choose a higher price for bidding. The project here will follow the same steps as you did with modifying the institution and agents in the past. You'll copy the agent file and then you'll modify the make_bid method to whatever you like. Finally, you'll modify the configuration file. 

You might want to create several copies of your configuration file. In you're configuration file you'll be able to add multiple agent types and numbers to your simulation and see how they perform against each other or other types of agents.

Specifically, you'll modify this line of your configuration: `"agents": [{"agent_name": "clock_simple_agent.ClockSimpleAgent", "number": 5}]`. Inside the list, you can add more dictionaries with the agent name of your new agent and how many you would like to participate in the simulation. You might try different combinations of agents to see what results you get.

Now you should be able to run your new MES. 

Go ahead and make these changes and continue to [step_7](../step_7) to see our solution.            
            
        

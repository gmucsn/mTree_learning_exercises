# mTree Basic Auction Tutorial - Step 5

At this point, we have an auction that will start and received bids, but it will not determine the winner of the auction and alert them. To accomplis this, we will extend our institution code and create a directive in our agent to receive news if they won. We will also generate a configuration file that we can use to run our current code and test it.

First, we'll need to go and update our `bid_for_item` method in our institution to identify when all agents
have submitted a bid.

```
@directive_decorator("bid_for_item")
def bid_for_item(self, message: Message):
    bidder = message.get_sender()
    bid = int(message.get_payload()["bid"])
        
    self.bids.append((bidder, bid))

    if len(self.bids) == len(self.address_book.select_addresses({"component_type": "Agent"})):
        self.complete_auction()
```

Now we will add a complete `complete_auction` method that will determine the winner. In order to determine the
winner we will sort the bid list by the bid value and pick the highest bidder. Only this bidder will get 
information on the actual price of the item. We will then send message to the agents that did not win the
auction. Finally, we will send a message back to the institution to start the next auction.

```
def complete_auction(self):
        
        bids = sorted(self.bids, key=lambda elem: elem[1] ,reverse=True)

        winner = bids.pop(0)
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("auction_result")
        new_message.set_payload({"status": "winner", "real_value": self.item_for_auction_price})

        self.send(winner[1], new_message)  # receiver_of_message, message

        for agent in bids:
            new_message = Message()  # declare message
            new_message.set_sender(self.myAddress)  # set the sender of message to this actor
            new_message.set_directive("auction_result")
            new_message.set_payload({"status": "loser"})
            self.send(agent[1], new_message)  # receiver_of_message, message

        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("start_auction")
        self.send(self.myAddress, new_message)  # receiver_of_message, message
```

Now, we will have to modify our agents and add a method to receive the messages concerning who won and lost
the auction.

```
@directive_decorator("auction_result")
def auction_result(self, message: Message):
    if message.get_payload()["auction_result"] == "winner":
        real_value = essage.get_payload()["real_value"]
        self.auction_history.append(("Win", self.bid, real_value))
    else:
        self.auction_history.append(("Loss", self.bid, 0))
```


Now that we have code for every component of our MES, we can run our experiment. In order to run our experiment we will need to build a configuration file. This is a json file that contains information about the components we will be using in our experiment.

We will create a new file in the config directory. We will call this file base_simulation.json. The contents of this file will look like:

```
{"mtree_type": "mes_simulation_description",
   "name":"Basic Auction Run",
   "id": "1",
   "environment": "basic_auctions.BasixEnvironment",
   "institution": "basic_auctions.BasicInstitution",
   "number_of_runs": 1,
   "agents": [{"agent_name": "basic_auction_agent.BasicAgent", "number": 5}],
   "properties": {}
 }
```

The key components of this configuration file are the environment, institution, and agents properties. For the environment we will specify the file and class name of our environment, in this case basic_auction_environment.BasicAuctionEnvironment. We will do the same for our institution by specifying basic_auction_institution.BasicInstitution. Finally, we will add our agent as a dictionary in the agents property. The agents property actually allows us to specify different types of agents and the number of the agents we would like to be in our MES. Here we will specify the agent_name as basic_auction_agent.BasicAuctionAgent and the number is 5.

In order then to run this we will run the following command in the command line in the root direction of this tutorial `mTree_runner`. This will launch a command line interface that will allow you to run the step_5 MES.

While this simulation will run, we will want to add log messages to understand what is happening throughout the experiment.



            
            
        
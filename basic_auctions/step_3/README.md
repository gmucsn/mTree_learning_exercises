# mTree Basic Auction Tutorial - Step 3

We will be adding code to auction_institution.py in our mes folder. We will be implementing a directive handler for start_auction which is a message we will receive from the environment. Finally, we will then implement a directive handler for handling bids from agents.

Starting with the start_auction directive handler we will then implement a method that will determine the common_value of the item and the value_estimmate to provide to each agent at the start of the auction. We will then create a method to record the bids from the agents.


```
@directive_decorator("start_auction")
def start_auction(self, message:Message):
    if self.num_auctions_remaining > 0:
        self.num_auctions_remaining -= 1

        self.common_value = random.randint(self.min_item_value, self.max_item_value)

        self.bids = []
        self.start_bidding()
```

We will use the start_bidding method because we can then reuse the method for alerting all agents of price changes.

In this case we will randomly determine the price estimate provided to each agent by selecting a number between the +/- sum `self.price` and the error bound `self.error`. In later steps, we will set these with configuration parameters.

```
def start_bidding(self):
    agents = self.address_book.select_addresses({"component_type": "Agent"})
    for agent in agents:
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("start_bidding")
        value_estimate = random.uniform(self.common_value - self.error, self.common_value + self.error)
        new_message.set_payload({"value_estimate": value_estimate, "error": error})
        self.send(agent["address"], new_message)
```

Finally, we will implement a directive handler for accepting bids from agents. This will handle the "bid_for_item" directive. This method identifies the bidder that sent the messsage and the bid amount from the bidder. 

```
@directive_decorator("bid_for_item")
def bid_for_item(self, message: Message):
    bidder = message.get_sender()
    bid = int(message.get_payload()["bid"])
        
    self.bids.append((bidder, bid))
```

Also, we will specify some properties for our class in the __init__ method. 

```
def __init__(self):
    self.num_auctions_remaining = 10

    self.min_item_value = 20
    self.max_item_value = 45


    self.common_value = None
    self.error = 4

    self.value_estimate = None

    self.bids = []
```
When you are finsihed go to [Step_4](../step_4).




            
            
        

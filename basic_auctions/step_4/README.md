# mTree Basic Auction Tutorial - Step 4

In this step, we will be setting up our agent code. We will also generate a configuration file that we can use to run our current code and test it.

Here we will implement two directive handlers: set_endowment and start_bidding. 

The set_endowment directive handles a message from the environment that specifies the endowment for the agent. All we need to do here is take the endowment specified by the environment and save it to the agent.

```
@directive_decorator("set_endowment")
def set_endowment(self, message: Message):
    self.endowment = message.get_payload()["endowment"]
```

Next, we will want to implement the directive for handling the start_bidding directive coming from the institution. In our implementation the agent will see the  price estimate and the error on the estimate.
It will then make a decision about how much to bid.

```
@directive_decorator("start_bidding")
def start_bidding(self, message: Message):
    self.price_estimate = message.get_payload()["price_estimate"]
    self.error = message.get_payload()["error"]
    self.institution = message.get_sender()
    self.make_bid()
```

Next, we will write our code to make a bid. In this case the agent will take the price estimate and simply bid that value.

```
def make_bid(self):
    self.bid = self.price_estimate

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("bid_for_item")
    new_message.set_payload({"bid": self.bid})
    self.send(self.institution, new_message) 
```

In order to support these functions we will be updating our __init__ method to specify certain properties.  In particular, we will have a property for the agent's endowment and will also specify the max_bid and bid_increment we would like to use.

```
def __init__(self):
    self.endowment = None
    self.institution = None
    
    self.bid = None

    self.auction_history = []

```

        

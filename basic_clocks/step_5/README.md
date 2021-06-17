# mTree Clock Auction Tutorial - Step 5

At this point, you'll probably be aware that the auction doesn't stop. That is, there is nothing that alerts the auction to finally close.

In this step, we will add some code to close the auction after some amount of time. To accomplish this, we will have to use the notion of clocks to time things. In this case, we want the auction to close after 15 seconds.

To do this, we will need alert the institution to close at that time. To accomplish this, we will actually send a message to the institution that will be delivered in some number of seconds. We will be adding this code to our start_auction method in our institution. We will add the following code.

```
@directive_decorator("start_auction", message_schema=["agents"], message_callback="send_agents_start")
def start_auction(self, message:Message):
    if self.num_auctions_remaining > 0:
        self.num_auctions_remaining -= 1
        self.agents = message.get_payload()["agents"]
        self.bids = []
        self.starting_price = random.randint(self.min_item_value, self.max_item_value)
        self.alert_agents_of_price(self.starting_price)

        wakeup_message = Message()  # declare message
        wakeup_message.set_sender(self.myAddress)  # set the sender of message to this actor
        wakeup_message.set_directive("check_auction_close")
        self.wakeupAfter( datetime.timedelta(seconds=15), payload=wakeup_message)
```

What you see in this code are 4 lines at the bottom. This consists of a normal message and then a new method being used on the last line. The last line which includes `self.wakeupAfter` basically will deliver a message in whatever time you'd like. In this case we set it so that it delivers the message to itself in 15 seconds. We also include the wakeup_message to ensure that the appropriate directives get triggered.

We will now need to add our check_auction_close method.

```
@directive_decorator("check_auction_close")
def check_auction_close(self, message:Message):
    # closing auction
    winner = self.bids[-1]
    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("auction_result")
    new_message.set_payload({"auction_result": "winner"})
    self.send(winner[1], new_message)  # receiver_of_message, message

    losers = [address for address in self.address_book.select_addresses({"address_type": "institution"}) if address["address"] != winner[1]]

    for agent in losers:
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("auction_result")
        new_message.set_payload({"auction_result": "loser"})
        self.send(agent["address"], new_message)  # receiver_of_message, message

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("start_auction")
    self.send(self.myAddress, new_message)  # receiver_of_message, message

```

At the end of this we will send a message to start the next auction.

Go ahead and make these changes and continue to [step_6](../step_6) to see our solution.
        

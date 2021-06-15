# mTree Basic Auction Tutorial - Step 7

In this Step you'll be working on changing the institution and analyzing data. If you look at the previous implementation of the institution you'll notice that the value the agent who wins the auction is the highest bid. This is what is called a first price auction. Other auctions use a second price. That is, the price the winner pays will be equal to the second highest bid. In this exercise you'll be working on the institution to change the closing rule of the auction to use the second price.

To do this you'll want to actually copy your institution file. Call it `second_price_auction_institution.py`. 

In this new file, you'll want to focus on the complete_auction method.

```
def complete_auction(self):
        
        bids = sorted(self.bids, key=lambda elem: elem[1] ,reverse=True)

        winner = bids.pop(0)
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("auction_result")
        new_message.set_payload({"status": "winner", "common_value": self.common_value})

        self.send(winner[0], new_message)  # receiver_of_message, message
```

In here you'll notice that there is a bids variable create that is sorted by the values. So to get the second price you'll have to interact with this list in some way.

You'll also need to copy your configuration file. So take basic_auction_simulation.json and copy it with a name like second_price_auction_simulation.json. In this file you'll want to change `"institution": "basic_auction_institution.AuctionInstitution"` to reflect the new institution you've created. So change the value of this to your new file. The first part of the institution name will be the name of your new institution file and the second part after the period will be the name of the class.

Now you should be able to run your new MES. 

For your data analysis exercise, you'll want to see how this closing rule affects perhaps the average price per auction and compare it to the MES with the regular institution.

One thing you'll notice, of course, is that the agents using a pretty unsophisticated way of bidding. In following steps you will be creating additional agents that using different techniques to bid.

When you are finsihed go to [Step_8](../step_8).

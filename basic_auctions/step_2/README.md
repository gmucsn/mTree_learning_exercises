# mTree Basic Auction Tutorial - Step 2

We will now be adding code to auction_environment.py in our mes folder.

In particular, we will need to add a directive handler to respond to messages of "start_environment." 

A directive inside a message identifies the directive handler that will handle the receiving and processing of messages from other components in the MES. You will use a decorator like `@directive_decorator("start_environment")` immediately above your class method to indicate what directive the method will handle.

As you work on the methods in the different classes be sure to add a docstring documenting what the method does and explaining any key variables or arguments being used and what self.variables are being changed or data being returned.  You should also document what the message being received is and if a message(s) is(are) being sent.  Here is the start_enviornment method without a docstring.
```
@directive_decorator("start_environment")
def start_environment(self, message:Message):
    self.provide_endowment()
    self.start_auction()
```

Now we will write code to both provide an endowment to each agent and code to start the auction.

The provide_endowment method will contact all agents and provide an initial endowment of 30 (or whatever number you'd like... you can even randomly generate the endowments if you'd prefer). We will use an address book to send a message to all the agents in the MES.

```
def provide_endowment(self):
    endowment = 30
    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("set_endowment")  # Set the directive (refer to 3. Make Messages) - has to match receiver decorator
    new_message.set_payload({"endowment": endowment})
    self.address_book.broadcast_message({"component_type": "Agent"}, new_message)
    
```

In this method, notice the use of the Message object. These Message objects are how communications are handled in mTree. You will create a new message and minimally set the directive for the message. You can also include a payload in the message which the recipient can examine. 

You'll notice here how we use the `address_book` property on the component. This keeps all the address of all the components in the MES and allows us to use a selector to identify who we want to broadcast messages to.

<!---
#TODO we need a better explanation of the address book and how selector usage works.
#TODO for example below we have "short name", which I understand but someone new will not.
--->

Finally, we will write the code to send a start auction message to the institution in your MES. 
```
def start_auction(self):
    self.address_book.forward_address_book({"short_name": "AuctionInstitution"})

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("start_auction")
    self.send(self.address_book.select_addresses({"short_name": "AuctionInstitution"}), new_message)  
```

In this method we first forward the addresses of all agents to the institution. To accomplish this we will use the method `self.address_book.forward_address_book`. The component selector, {"short_name": "AuctionInstitution", chooses the institution that will be running the auction.

We then construct a message and use the send method, `self.send(recipient, message_object)` to send the "start_auction" directive to the AuctionInstitution, which will be running the auction.

In this case, we will use the selector `{"short_name": "AuctionInstitution"}` to get the address of the institution as we will only be using one institution here. The short name of the component will typically just be the class name of the component itself. 

When you have saved these python files go to [Step_3](../step_3).

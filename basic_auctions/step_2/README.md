# mTree Basic Auction Tutorial - Step 2

In this step, we will be setting up our environment's code. 

We will then be adding code to auction_environment.py in our mes folder.

In particular, we will need to add a directive handler to respond to messages of "start_environment." 

Directives identify the code that will handle the receiving and processing of messages from other components in the MES. You will use a decorator like `@directive_decorator("start_environment")` immediately above your class method to indicate what directive the method will handle.

Minimally, for our environment we will need to respond to the "start_environment" directive. So we will add this code to our class:
```
@directive_decorator("start_environment")
def start_environment(self, message:Message):
    self.provide_endowment()
    self.start_auction()
```

Now we will need to provide code for both providing the endowment to our agents and also to start the auction.

The provide_endowment method will contact all agents and provide them with an initial endowment. We will set the endowment to 30 (or whatever number you'd like... you can even randomly generate the endowments if you'd prefer). We will be using the address book mechanism to send a message to all the agents in the MES.

```
def provide_endowment(self):
    endowment = 30
    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("set_endowment")  # Set the directive (refer to 3. Make Messages) - has to match reciever decorator
    new_message.set_payload({"endowment": endowment})
    self.address_book.broadcast_message({"component_type": "Agent"}, new_message)
    
```

In this method, notice the use of the Message object. These Message objects are how communications are handled in mTree. You will create a new message and minimally set the directive for the message. You can also include a payload in the message which the recipient can examine. 

You'll notice here how we use the `address_book` property on the component. This keeps all the address of all the components in the MES and allows us to use a selector to identify who we want to broadcast messages to.

Finally, we'll send a start auction message to the institution in your MES. 
```
def start_auction(self):
    self.address_book.forward_address_book({"short_name": "AuctionInstitution"})

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("start_auction")
    self.send(self.address_book.select_addresses({"short_name": "AuctionInstitution"}), new_message)  
```

In this case we will also be forwarding the addresses of all agents to the institution. The institution will then have the addresses of all the agents that will be participating in the auction. To accomplish this we will use the method `self.address_book.forward_address_book`. This will allow us to use a component selector to figure out who should receive the address book. In this case, we are targeting the institution that will be running the auction.

When you've constructed your message you will then be able to use the send method. `self.send(recipient, message_object)` will send a message to the recipient you provide an address for. In this case, we are using the address book to look up the address for the Institution itself that will be running the auction.

In this case, we will use the selector `{"short_name": "AuctionInstitution"}` to get the address of the institution as we will only be using one institution here. The short name of the component will typically just be the class name of the component itself. 


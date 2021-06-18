# mTree Basic Trust Game Tutorial - Step 2

In this step, we will be setting up our initial environment. 

The environment will receive a message with the `start_environment` direcrtive. This will kick things off by providing all agents an identical endowment. It will then send its address book to the institution and tell the institution to start the trust game.

You'll notice this code is similar to other environments seen in the learning exercises.

```
@directive_decorator("start_environment")
def start_environment(self, message:Message):
    self.provide_endowment()
    self.start_trust_game()
```

We will then need to send the endowments to all agents in the MES. To do so we will implement the `provide_endowment` method.

```
def provide_endowment(self):
    endowment = 10
    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("set_endowment")  # Set the directive (refer to 3. Make Messages) - has to match receiver decorator
    new_message.set_payload({"endowment": endowment})
    self.address_book.broadcast_message({"address_type": "agent"}, new_message)
```

Now that all agents have been given an endowment we will need to alert the institution to break up the agents into groups of two and then begin the trust game. 

```
def start_trust_game(self):
    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("start_trust")
    new_message.set_payload({"address_book": self.address_book.get_addresses()})
    self.send(self.address_book.select_addresses({"address_type": "institution"}), new_message) 
```

In the next step we will be updating our institution to actually make up the pairings of agents.
# mTree Basic Trust Game Tutorial - Step 4

In this step, we will be setting up our basic agent code. 

We will need to implement several directive here. In particular, we will need to be able to handle the `set_endowment`, `make_sender`, and `make_receiver` directives.

Our endowment initializeation directive handler will look like others.

```
@directive_decorator("set_endowment")
    def set_endowment(self, message: Message):
        self.prepare_agent()
        self.endowment = message.get_payload()["endowment"]
```

Seeing this we will notice that we also need to define a `prepare_agent` method.

```
def prepare_agent(self):
    self.endowment = None
    self.institution = None
    self.group_name = None
    self.role = None
    self.split_amount = None
```

This will simply store basic information for our agent.

The next two directives will be fairly similar to each other. We will start with the `make_receiver` which will simply alert the agent that they will be a reciever.

```
@directive_decorator("make_receiver")
def make_receiver(self, message: Message):
    self.group_name = message.get_payload()["group_name"]
    self.institution = message.get_sender()
    self.role = "receiver"
```

This directive handler simply records that the agent is a reciever. It will wait until the sender forwards their split amount before continuing. One thing you will notice in this and the next directive is that it records the group name for the sender and the receiver. This is intended to help keep track of which agent is in what group.

The next directive handler is for the sender. This will both configure them as a sender and will then trigger a method `decide_split` to determine how much of their endowment to splt.

```
@directive_decorator("make_sender")
    def set_endowmake_senderment(self, message: Message):
        self.group_name = message.get_payload()["group_name"]
        self.institution = message.get_sender()
        self.role = "sender"
        self.decide_split()
```

This directive handler reocrds the group name, remembers the institution address, specifies its role as a send, and then fires the `decide_split` method.

In the `decide_split` method we have the agent look at their endowment and identify how much to send. In our case we randomly select an integer between 0 and the endowment amount to send back.

```
def decide_split(self):
    self.split_amount = random.randint(0, self.endowment)
    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("send_amount")
    new_message.set_payload({"send_amount": self.split_amount, "group_name": self.group_name})
    self.send(self.institution, new_message)  
```

We will then send this decision result back to the institution along with the group name in the payload to make it easier to track things.

In the next step we will be updating our institution code to receive the split amount and then multiply the funds and send to the receiver.
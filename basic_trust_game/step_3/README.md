# mTree Basic Trust Game Tutorial - Step 3

In this step, we will be setting up our initial institution. 

The institution will receive a message with the `start_trust` direcrtive. This will start the institution off. 

```
@directive_decorator("start_trust")
    def start_trust(self, message:Message):
        if message.get_payload()is not None:            
            self.prepare_trust_game()
            temp_address_book = message.get_payload()["address_book"]
            self.address_book.merge_addresses(temp_address_book)
        else:
            self.address_book.reset_address_groups()
            

        if self.rounds_remaining > 0:
            self.rounds_remaining -= 1

            # code for making groups
            agents = self.address_book.select_addresses({"address_type": "agent"})
            for i in range(0, len(agents), 2): # get pairs of agents in order
                group_name = self.address_book.create_address_group()
                self.address_book.add_address_to_group(group_name, agents[i])
                self.address_book.add_address_to_group(group_name, agents[i+1])
            
            self.groups_remaining = len(self.address_book.get_all_groups())

            for group in self.address_book.get_all_groups():
                group_members = group[1]
                sender = group_members[0]
                receiver = group_members[1]

                new_message = Message()  # declare message
                new_message.set_sender(self.myAddress)  # set the sender of message to this actor
                new_message.set_payload({"group_name": group[0]})
                new_message.set_directive("make_sender")
                self.send(sender["address"], new_message)  
        
                new_message = Message()  # declare message
                new_message.set_sender(self.myAddress)  # set the sender of message to this actor
                new_message.set_payload({"group_name": group[0]})
                new_message.set_directive("make_receiver")
                self.send(receiver["address"], new_message)  
```

As you can see this method is rather long. What this method does is detect whether the start_trust message is coming from the environment or itself. If it's from the environment it will prepare the institution for the trust game. This will fire the `prepare_trust_game` method.

The `prepare_trust_game` method is pretty straightforward. It will specify the multiplier and the number of rounds to play.

```
def prepare_trust_game(self):
    self.multiplier = 3
    self.groups_remaining = None
    self.rounds_remaining = 10
```

After preparing the institution, the institution determines how many rounds are remaining. As long as there are rounds remaining it will start to break the list of addresses up into groups of two which will be the sender and receiver in the individual game.

```
# code for making groups
agents = self.address_book.select_addresses({"address_type": "agent"})
for i in range(0, len(agents), 2): # get pairs of agents in order
    group_name = self.address_book.create_address_group()
    self.address_book.add_address_to_group(group_name, agents[i])
    self.address_book.add_address_to_group(group_name, agents[i+1])

self.groups_remaining = len(self.address_book.get_all_groups())
```

Looking at this code, you'll notice the somewhat odd `range` usage. This is intended to grab agents by groups of two. Thus, it will simply grab the agents in order and will not randomize the order of the groups. So each round that is played the same agents should be playing against each other. We can think about this process and improve upon it in later exercises.

After we have made up the groups of senders and receivers we will need to alert the agents as to which role they will play. 

```
for group in self.address_book.get_all_groups():
    group_members = group[1]
    sender = group_members[0]
    receiver = group_members[1]

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_payload({"group_name": group[0]})
    new_message.set_directive("make_sender")
    self.send(sender["address"], new_message)  

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_payload({"group_name": group[0]})
    new_message.set_directive("make_receiver")
    self.send(receiver["address"], new_message)
```

In this instance we will iterate over all the groups of users by using the `address_book.get_all_groups()` method. Once we start iterating over these groups we simply make the first player the sender and the second the receiver. We send both different messages indicating what role they will play.


In the next step we will be updating our agent code to initialize themselves.
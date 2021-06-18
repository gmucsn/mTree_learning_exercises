# mTree Basic Trust Game Tutorial - Step 7

In this step, we will be setting up our institution to take the split amount and then assign the final allocation to both the sender and receiver.

We will need to respond to the split_amount directive and we will be able to do all necessary steps in one method.

Our method will look like:

```
@directive_decorator("split_amount")
def split_amount(self, message:Message):
    group_name = message.get_payload()["group_name"]
    return_amount = message.get_payload()["return_amount"]
    keep_amount = message.get_payload()["keep_amount"]
    
    sender = self.address_book.address_groups[group_name][0]    
    receiver = self.address_book.address_groups[group_name][1]

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_payload({"return_amount": return_amount})
    new_message.set_directive("allocate_sender_split")
    self.send(sender["address"], new_message)  

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_payload({"keep_amount": keep_amount})
    new_message.set_directive("allocate_receiver_split")
    self.send(receiver["address"], new_message)
    
    self.groups_remaining -= 1
    self.log_message("groups " + str(self.groups_remaining))
    if self.groups_remaining == 0:
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("start_trust")
        self.send(self.myAddress, new_message)
```        

In this case we will grab the group_name so as to be able to send the final funds to the sender and receiver.

We will then send a message to the sender to indicate what their return_amount is.

Next we will send a message to the receiver allocating their split amount that they will keep.

Finally, we will look at how many groups neeed to return their allocations. Once all groups have sent in their decisions we will send the institution a message to begin the next round if necessary.

In the next step we will be updating our agent to receive the final allocated funds.
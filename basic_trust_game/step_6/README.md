# mTree Basic Trust Game Tutorial - Step 6

In this step, we will be setting up our agents designated as receivers to receive the multiplied funds and identify how much to send back.

We will need to respond to the allocate_receiving directive and we will be able to do all necessary steps in one method.

Our method will look like:

```
@directive_decorator("allocate_receiving")
def allocate_receiving(self, message: Message):
    multiplied_amount = message.get_payload()["multiplied_amount"]
    return_amount = random.randint(0, multiplied_amount)
    keep_amount = multiplied_amount - return_amount

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_directive("split_amount")
    new_message.set_payload({"return_amount": return_amount, "keep_amount": keep_amount, "group_name": self.group_name})
    self.send(self.institution, new_message)  
```        

In this case we will grab the group_name of the sender to then pull the appropriate group list to forward the split amout back to the sender. 

We will then take the multiplied amount and select a random amount between 0 and the multiplied amount to send to the sender. We will then send a message to the sender. 

In the next step we will be updating our institution to send the final fund allocations to the sender and receiver.
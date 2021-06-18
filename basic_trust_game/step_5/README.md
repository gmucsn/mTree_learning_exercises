# mTree Basic Trust Game Tutorial - Step 5

In this step, we will be setting up our institution to receive the split amount, multiply it, and then forward to the receiver. 

We will need to respond to the send_amount directive and we will be able to do all necessary steps in one method.

Our method will look like:

```
@directive_decorator("send_amount")
def send_amount(self, message:Message):
    group_name = message.get_payload()["group_name"]
    amount_sent = message.get_payload()["send_amount"]
    multiplied = amount_sent * self.multiplier
    
    receiver = self.address_book.address_groups[group_name][1]

    new_message = Message()  # declare message
    new_message.set_sender(self.myAddress)  # set the sender of message to this actor
    new_message.set_payload({"multiplied_amount": multiplied})
    new_message.set_directive("allocate_receiving")
    self.send(receiver["address"], new_message)  
```        

In this case we will grab the group_name of the sender to then pull the appropriate group list to forward the send amount to the receiver. 

We will also take the amount_sent and simply multiply it by the multiplier we stored earlier.

Finally, we will send a message to the identified receiver. In order to find this we will simply pull the address_groups by their name and then select the 2 element of the list.



In the next step we will be updating our agent code to receive the multiplied funds and then make a determination about how much funds to return.
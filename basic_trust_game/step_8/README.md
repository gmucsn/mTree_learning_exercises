# mTree Basic Trust Game Tutorial - Step 8

In this step, we will be setting up our agents to receive their final funds allocations.

We will need to implement a directive handler for both allocate_sender_split and allocate_receiver_split. This will simply record how much their final fund allocation is and add it to their endowment.

Our allocate_sender_split will look like:

```
@directive_decorator("allocate_sender_split")
def allocate_sender_split(self, message: Message):
    return_amount = message.get_payload()["return_amount"]
    self.endowment += return_amount
    self.log_message("New Endowment: " + str(self.endowment) + " Return Amount: " + str(return_amount))
```

Our allocate_receiver_split directive handler will look like:

```
@directive_decorator("allocate_receiver_split")
def allocate_receiver_split(self, message: Message):
    keep_amount = message.get_payload()["keep_amount"]
    self.endowment += keep_amount
    self.log_message("New Endowment: " + str(self.endowment) + " Keep Amount: " + str(keep_amount))
```        

In the next step we will suggest different agent decision strategies you can consider implementing.
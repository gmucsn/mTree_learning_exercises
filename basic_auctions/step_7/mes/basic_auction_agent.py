from mTree.microeconomic_system.environment import Environment
from mTree.microeconomic_system.institution import Institution
from mTree.microeconomic_system.agent import Agent
from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
import math
import random
import logging
import time
import datetime

@directive_enabled_class
class AuctionAgent(Agent):
    def prepare_agent(self):
        self.endowment = None
        self.institution = None
        
        self.bid = None

        self.auction_history = []

    @directive_decorator("set_endowment")
    def set_endowment(self, message: Message):
        self.prepare_agent()
        self.endowment = message.get_payload()["endowment"]
        
    @directive_decorator("start_bidding")
    def start_bidding(self, message: Message):
        self.value_estimate = message.get_payload()["value_estimate"]
        self.error = message.get_payload()["error"]
        self.institution = message.get_sender()
        self.make_bid()

    def make_bid(self):
        bid = self.value_estimate
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("bid_for_item")
        new_message.set_payload({"bid": bid})
        
        self.send(self.institution, new_message) 
        

    @directive_decorator("auction_result")
    def auction_result(self, message: Message):
        self.log_message(message.get_payload())
        if message.get_payload()["auction_result"] == "winner":
            self.log_message(message.get_payload())
            common_value = message.get_payload()["common_value"]
            self.auction_history.append(("Win", -1, common_value))
        else:
            self.auction_history.append(("Loss", 0, 0))
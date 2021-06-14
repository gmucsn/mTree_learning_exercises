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
class AuctionInstitution(Institution):
    def __init__(self):
        self.num_auctions_remaining = 10

        self.min_item_value = 20
        self.max_item_value = 45


        self.common_value = None
        self.error = 4

        self.value_estimate = None

        self.bids = []

    @directive_decorator("start_auction")
    def start_auction(self, message:Message):
        if self.num_auctions_remaining > 0:
            self.num_auctions_remaining -= 1

            self.common_value = random.randint(self.min_item_value, self.max_item_value)

            self.bids = []
            self.start_bidding()

    def start_bidding(self):
        agents = self.address_book.select_addresses({"component_type": "Agent"})
        for agent in agents:
            new_message = Message()  # declare message
            new_message.set_sender(self.myAddress)  # set the sender of message to this actor
            new_message.set_directive("start_bidding")
            value_estimate = random.uniform(self.common_value - self.error, self.common_value + self.error)
            new_message.set_payload({"value_estimate": value_estimate, "error": error})
            self.send(agent["address"], new_message)

    @directive_decorator("bid_for_item")
    def bid_for_item(self, message: Message):
        bidder = message.get_sender()
        bid = int(message.get_payload()["bid"])
            
        self.bids.append((bidder, bid))
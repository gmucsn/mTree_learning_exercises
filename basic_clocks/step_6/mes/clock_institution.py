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
class ClockInstitution(Institution):
    def prepare_auction(self):
        self.num_auctions_remaining = 10
        self.min_item_value = 10
        self.max_item_value = 100

        self.last_bid = 0
        self.last_bid_time = 0

        self.starting_price = None
        self.bids = []

    @directive_decorator("start_auction", message_schema=["agents"], message_callback="send_agents_start")
    def start_auction(self, message:Message):
        if message.get_payload() is not None:
            self.prepare_auction()
            temp_address_book = message.get_payload()["address_book"]
            self.address_book.merge_addresses(temp_address_book)


        if self.num_auctions_remaining > 0:
            self.num_auctions_remaining -= 1
            self.bids = []
            self.starting_price = random.randint(self.min_item_value, self.max_item_value)
            self.alert_agents_of_price(self.starting_price)

            wakeup_message = Message()  # declare message
            wakeup_message.set_sender(self.myAddress)  # set the sender of message to this actor
            wakeup_message.set_directive("check_auction_close")
            self.wakeupAfter( datetime.timedelta(seconds=5), payload=wakeup_message)
            
    def alert_agents_of_price(self, current_price):
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("current_price")
        new_message.set_payload({"current_price": current_price})
        self.address_book.broadcast_message({"address_type": "agent"}, new_message)


    @directive_decorator("bid_for_item", message_schema=["bid"])
    def bid_for_item(self, message: Message):
        bidder = message.get_sender()
        bid = int(message.get_payload()["bid"])
        if bid > self.last_bid:
            self.last_bid = bid
            self.last_bid_time = time.time()
            self.bids.append((bid, bidder))
            self.alert_agents_of_price(self.last_bid)
            
    @directive_decorator("check_auction_close")
    def check_auction_close(self, message:Message):
        # closing auction
        winner = self.bids[-1]
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("auction_result")
        new_message.set_payload({"auction_result": "winner"})
        self.send(winner[1], new_message)  # receiver_of_message, message
        self.log_data("----->sent message to winner")

        losers = [address for address in self.address_book.select_addresses({"address_type": "agent"}) if address["address"] != winner[1]]
        self.log_data("----->abou to sent message to losers")
        for agent in losers:
            new_message = Message()  # declare message
            new_message.set_sender(self.myAddress)  # set the sender of message to this actor
            new_message.set_directive("auction_result")
            new_message.set_payload({"auction_result": "loser"})
            self.send(agent["address"], new_message)  # receiver_of_message, message

        # reset
        self.last_bid = 0

        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("start_auction")
        self.send(self.myAddress, new_message)  # receiver_of_message, message
                
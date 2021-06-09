# mTree Basic Auction Tutorial - Step 1

In this step, we will be setting up our initial python files for our MES. 

We will need to create three files for our MES components of an environment, institution, and agents.

To do this open Visual Studio Code and navigate to this folder in your repo. 

In the mes directory create the following files:

- auction_environment.py
- auction_institution.py
- auction_simple_agent.py

In each of these files we will need to specify a few imports. These imports are:
```
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
```

Then for the environment, institution, and agent, you will need to setup a directive enabled class that subclasses from their respective MES component.

The environment class code after the import statements will then look like this:
```
@directive_enabled_class
class AuctionEnvironment(Environment):
    def __init__(self):
        pass
```

In particular, notice the use of the @directive_enabled_class decorator. This is necessary in mTree for your component to work.

When you have saved these python files go to [Step_2](../step_2).

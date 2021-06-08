# mTree Basic Auction Tutorial - Step 6

We now have a working MES, but we don't have data we can readily analyze. In this step, we will start to introduce how to add log messages, and then we will provide a challenge.

In mTree there are two types of logs. There are experiment logs and data logs. The experiment logs are meant to provide messages to the experimenter to indicate what is going on in the experiment itself. This is where you can put debugging messasges and what not in order to understand how the MES is working. At the same time, you can also log data that will become available to the experimenter in a readily digestible format.

After you run your MES you should notice a new directory will appear in the whatever MES directory you arunning that is titled `logs`. This directory will contain log files for your experiment. One thing you will notice is that you will start to see pairs of files created each time you run the MES. The format of the log file names is currently the epoch time (an integer representation of time since the release of Unix) followed by a hyphen and then followed by either experiment.log or data.log. These two log files are created for each run. The larger the number at the beginning of the file, the more recent the run.

Inside the files, you will notice that each line contains a timestamp followed by a line of whatever data you want. 

In order to log to these files, you only need to use one of two functions: `self.log_data()` and `self.log_message()`

Both of these functions alow you to insert whatever data you'd like as the first parameter. This data will be output into the log files.

For example: 

```
self.log_message("Agent submitted bid: " + str(self.bid))
```

For this Step, you will want to add log messages you deem appropriate for analyzing bidding behavior. For example, you might want to create log statements in the agent class in the `auction_result` method to capture who won and what their bid was relative to the actual price of the good.

As a next task for this Step you will want to create a new version of the Institution so that it provides a different auction closing rule. In this case, you will want your auction to have the winner pay the second highest price and not the highest price. 

Once you've done this you should be then able to create two separate log files for each institutional arrangement and then analyze whether the change in closing rules results in a difference in outcomes across all agents.

In following steps you will be creating additional agents and also configuring parameters.


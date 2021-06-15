# mTree Clock Auction Tutorial - Step 7

In this step you will want to modify your institution. In particular, you will want to specify a closing time for the auction but then you will only close the auction if there hasn't been a bid in the last 5 seconds. 

To accomplish this you will need to incorporate both the current wakeupAfter technique, but then you will also want to incorporate some mechanism to record the last bid time and see if that is within the last 5 seconds before you close the auction. If there is a new high bid in the last 5 seconds, you will then not close the auction and will then extend the auction for another 15 seconds.

You will need to modify the institution to accomplish this. So you'll want to copy the institution and change the closing mechanism out. In particular, you will want to record bid times in the bid_for_item method along with check_auction_close.

Now you should be able to run your new MES. 

Since you also have different institutions, you might also consider varying your agent and institutions to see what overall effects things have.


            
            
        

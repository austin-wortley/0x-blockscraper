# 0x-blockscraper
Approach for pulling block information 0x protocol fillOrder events

The first part of this challenge was to implement a function that will pull in all the details of ERC20 token transfers given a certain block. My code, written in python, queries Infura with the ‘eth_getlogs’ json_rpc, searching for the LogFill event that is triggered from the successful transfer action of tokens on the 0x contract. It searches for the log fill with the variable q and the block number based, and then outputs a CSV with certain fields including Maker, and Taker (which can be contracts), the token and Token Type, all in my output.txt are of type _zrxToken, and the protocol used. 

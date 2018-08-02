import requests
import json
from web3 import Web3, HTTPProvider, IPCProvider
from web3.auto import w3
import csv

from ethereum_input_decoder import ContractAbi, Utils

def request(num):
    q = '0x0d0b9391970d9a25552f37d436d2aae2925e2bfe1b2a923754bada030c498cb3'
    f = hex(num)
    # print(str(f))
    h = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    r = requests.get('https://api.infura.io/v1/jsonrpc/mainnet/eth_getLogs', params='params=%5B%7B%22fromBlock%22%3A%22'+ str(f) +'%22%2C%22topics%22%3A%5B%22'+ q +'%22%5D%7D%5D', headers=h )

    ca = loader('abi.txt')
    j = r.json()

    # transaction_counter = 0

    with open('output.csv', 'w') as f:
        f.write("Maker,Taker,Tokens,Tokentype,Token,ProxyType,Proxy\n")
        for result in j['result']:
            out = ""
            topics = result['topics']
            r = desc_contr(result['data'], ca)
            r1 = string_editor(r)

            r2 = r[r.find(',')+11:r.find('returns')-3].split("=")

            out += topics[1] + "," + topics[2] + ","+ topics[3] + "," + r1[0] + "," + r1[1] + ","+ r2[0] + "," + r2[1] + "\n"
            f.write(out)

    f.close()
            # transaction_counter+=1
            # if transaction_counter > 10:
            #     f.close()
            #     break



def loader(s):
    with open('abi.txt', 'r') as f:
        abi = f.read()

    return ContractAbi(json.loads(abi))

def hexDecoder(x):
    web3 = Web3(IPCProvider())
    return str(web3.toText(x))

def desc_contr(s, ca):
    return str(ca.describe_constructor(Utils.str_to_bytes(s)))

def string_editor(s):
    q = s[s.find("address") + 8:s.find(',')].split("=")
    for i in q:
        i.replace(" ", "")
    return q


if __name__ == "__main__":

    print("Please choose a block: " )
    request(int(input()))
    # request(5971129)

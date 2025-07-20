import sys
import yaml
from web3 import Web3

with open('info.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)    

def main():

 INFURA_API_KEY = data['infura_api']
 provider_url = f"https://sepolia.infura.io/v3/{INFURA_API_KEY}"
 
 w3 = Web3(Web3.HTTPProvider(provider_url))
 account_from = '0xAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
 account_to   = '0xAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

 priv_key     =  data['privk']

 if w3.isAddress(account_from) and w3.isAddress(account_to):

  wallet_from = w3.toChecksumAddress(account_from)
  wallet_to   = w3.toChecksumAddress(account_to)
  
  nonce = w3.eth.getTransactionCount(wallet_from)
  print(nonce)
  tx = {
         'nonce':    nonce,
         'from':     wallet_from,
         'to':       wallet_to,
         'value':    w3.toWei(.00001, 'ether'),
         'gas':      21000,
         'gasPrice': w3.toWei(40, 'gwei')
		
  }
  
  signed_tx = w3.eth.account.signTransaction(tx, priv_key)
  tx_hash   = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
  txid      = tx_hash.hex()

  print(tx_hash)
  print(txid)

 else:
  print('at least one address is not valid')
 
 
if __name__=="__main__":
 main()
 

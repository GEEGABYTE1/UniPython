from web3 import Web3, EthereumTesterProvider



class ViewCoin:
   w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/bb00f20d72fe41ddb707d1b562365919'))
   count = 0
   def view_coin(self):
       result = self.w3.isConnected()
       if result == True:
           if self.count == 0:
            user_block_num = str(input('Transaction Hash of Root Token: '))
           else:
               user_block_num = str(input('Transaction Hash of Desired Token: '))
           user_block_num = user_block_num.strip(' ')
           info = self.w3.eth.get_block(user_block_num)
           return_hash = info['hash']
           self.count += 1
           return return_hash 

       else:
           return None


session = ViewCoin()
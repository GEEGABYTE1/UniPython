from termcolor import colored
from uniswap import Uniswap


# ENV Var 
import os 
os.environ['PROVIDER'] = 'https://rinkeby.infura.io/v3/bb00f20d72fe41ddb707d1b562365919'


class Script:
    address = 'None'
    private_key = 'None'
    version = 2
    provider = os.environ.get('PROVIDER')           # Switch back to None for Production
    

    def __init__(self):
        address = str(input('Address: '))
        self.address = address.strip(" ")
        private_key = str(input('Private Key: '))
        self.private_key = private_key.strip(' ')
        version = str(input('Desired Uniswap Version: '))
        version = version.strip(' ')
        try:
            int_version = int(version)
            if int_version > 3:
                print(colored("That Version is undefined", 'red'))
            else:
                self.version = int_version
        except:
            pass
        web3_provider = str(input("Web3 Provider (in HTTP Format): "))
        self.provider = web3_provider.strip(' ')
        self.uniswap = Uniswap(address=self.address, private_key=self.private_key, version=self.version, provider=self.provider)




test = Script()
print(test)
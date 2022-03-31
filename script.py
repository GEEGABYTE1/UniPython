from termcolor import colored
from uniswap import Uniswap



# ENV Var 
import os 
os.environ['PROVIDER'] = 'https://mainnet.infura.io/v3/bb00f20d72fe41ddb707d1b562365919'


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
        #web3_provider = str(input("Web3 Provider (in HTTP Format): "))
        #self.provider = web3_provider.strip(' ')
        self.uniswap = Uniswap(address=self.address, private_key=self.private_key, version=self.version, provider=self.provider)
        
        while True:
            prompt_string = colored(': ', 'green')
            user_prompt = str(input(prompt_string))
            user_prompt.strip(' ')
            user_prompt = user_prompt.lower()

            if user_prompt == '/rate':
    
                result = str(input('Root Token: '))         # Address, [coin_name]
                result = result.split(', ')
                result_address = result[0]
                result_string = result[-1]
                result2 = str(input('Desired Token Address: '))
                result2 = result2.split(', ')
                result2_address = result2[0]
                result2_string = result2[-1]
                if result == None or result2 == None:
                    print("Transaction not found")
                else:
                    price_input = self.uniswap.get_price_input(result2_address, result_address, 10**18)
                    print("1 {} = {} {}".format(result_string, price_input, result2_string))
        
            elif user_prompt == '/conversion':
                result = str(input('Root Token: '))
                result = result.split(', ')
                result_address = result[0]
                result_string = result[-1]
                result2 = str(input('Desired Token Address: '))
                result2 = result2.strip(', ')
                result2_address = result2[0]
                result2_string = result2[-1]
                if result == None or result2 == None:
                    print("Token not found")
                else:
                    user_amount = int(input('How many {} would you like to convert to {}: '.format(result_string, result2_string)))
                    price_output = self.uniswap.get_price_output(result-address, result2_string, user_amount * 10**18)
                    print('{root} {root_val} = {des} {des_val}'.format(root=result_string, root_val=1, des=result2_string, des_val=user_amount))
                    



test = Script()
print(test)
from termcolor import colored
from uniswap import Uniswap
from quicksort import quicksort, returned_lst
import random



# ENV Var 
import os 
os.environ['PROVIDER'] = 'https://mainnet.infura.io/v3/bb00f20d72fe41ddb707d1b562365919'


class Script:
    address = 'None'
    private_key = 'None'
    version = 2
    provider = os.environ.get('PROVIDER')           # Switch back to None for Production
    past_inserts = []

    def fetch_indexes(self):
        root_idx = None 
        desired_idx = None 
        while True:
            random_idx = random.randint(0, len(self.past_inserts))
            if random_idx % 2 == 0:
                self.root_idx = random_idx
            if random_idx % 2 == 1:
                self.desired_idx = random_idx 
            if self.desired_idx != None and self.root_idx != None:
                break

            
            
    

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
                    root_dictionary = {'Address': result_address, 'Name':result_string}
                    desired_dictionary = {'Address': result2_address, 'Name': result2_string}
                    self.past_inserts.append(root_dictionary)
                    self.past_inserts.append(desired_dictionary)
                    user_amount = int(input('How many {} would you like to convert to {}: '.format(result_string, result2_string)))
                    price_output = self.uniswap.get_price_output(result-address, result2_string, user_amount * 10**18)
                    print('{root} {root_val} = {des} {des_val}'.format(root=result_string, root_val=1, des=result2_string, des_val=user_amount))
            
            elif user_prompt == '/sbv'  :        # Sort by Val
                desired_root = str(input('Desired Token Address: '))          # Address, [coin_name]
                if not ',' in desired_root or not ', ' in desired_root:
                    print("Invalid Command")
                else:
                    result2 = desired_root.split(', ')
                    result2_address = result2[0]
                    result2_string = result2[-1]
                    time_range = int(input('How many transactions would you like to sort: '))
                    values = []
                    for i in range(time_range):
                        transaction_hash = str(input('Token Metadata: '))                 # Address, [coin_name]
                        transaction_string = transaction_hash.split(', ')
                        transaction_string_name = transaction_string[-1]
                        transaction_hash = transaction_string[0]
                        result = self.uniswap.get_price_input(result2_address, transaction_hash, 10**18)
                        dictionary = {'name': transaction_string_name, 'Transaction': transaction_hash, 'Conversion':result}
                        values.append(dictionary)
                    
                    numerical_val = []
                    for val in values:
                        conversion = val['Conversion']
                        numerical_val.append(conversion)
                    
                    start = 0 
                    end = len(numerical_val) - 1
                    quicksort(numerical_val, start, end)
                    sorted_results = numerical_val
                    
                    
                    count = 1 
                    if len(sorted_results) == None:
                        print("Nothing was found")
                    else:
                        print('\n')
                        print(colored('*'*24), 'white')
                        print(colored("Rates for 1 {}".format(result2_string), 'cyan'))
                        print('\n')
                        for result in sorted_results:
                            for dict in values:
                                if dict['Conversion'] == result:
                                    print('-'*24)
                                    print('{count}: {name} - {conversion}'.format(count=count, name=dict['name'], conversion=result))
                                    count += 1
                                else:
                                    continue 
                                                
                            
                        
                

                    
                    

                    


test = Script()
print(test)
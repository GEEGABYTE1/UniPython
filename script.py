
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
    provider = None
    past_inserts = []

    def fetch_indices(self):
        if len(self.past_inserts) == 0:
            return None
        root_idx = None 
        desired_idx = None 
        while True:
            random_idx = random.randint(0, len(self.past_inserts))
            if random_idx % 2 == 0:
                root_idx = random_idx
            if random_idx % 2 == 1:
                desired_idx = random_idx 
            if desired_idx != None and root_idx != None:
                break
    
        return root_idx, desired_idx

            
    def history_sbv(self):
        goal_indices = self.fetch_indices()
        values = []
        if goal_indices == None:
            return None
        else:
            token_hash = self.past_inserts[goal_indices[-1]]['Address']
            token_name = self.past_inserts[goal_indices[-1]]['Name']
            for dictionary_idx in range(len(self.past_inserts)):
                dictionary = self.past_inserts[dictionary_idx]
                if dictionary_idx % 2 == 1:
                    continue 
                else:
                    dictionary_hash = dictionary['Address']
                    dictionary_name = dictionary['Name']
                    result = self.uniswap.get_price_input(dictionary_hash, token_hash, 10**18)
                    result_dict = {'Token': dictionary_name, 'Conversion Rate': result}
                    values.append(result_dict)
        
        quicksort(values, 0, len(values) - 1)
        for dictionary in values:
            print('\n')
            print(colored('Rates to Convert: {}'.format(token_name)), 'green')
            print('-'*24)
            print('{name} ~ {rate}'.format(name=dictionary['Token'], rate=dictionary['Conversion Rate']))
    
        
    

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
        try:
            self.uniswap = Uniswap(address=self.address, private_key=self.private_key, version=self.version, provider=self.provider)
        except:
            print(colored('Account not Found', 'red'))
        
        while True:
            sbv_prompt = self.history_sbv()
            if sbv_prompt == None:
                pass 
            else:
                print('\n')
            prompt_string = colored(': ', 'green')
            user_prompt = str(input(prompt_string))
            user_prompt.strip(' ')
            user_prompt = user_prompt.lower()

            if user_prompt == '/rate':
    
                result = str(input('Root Token: '))         # Address, [coin_name]
                if ',' not  in result:
                    print(colored('Syntax Error', 'red'))
                else:
                    result = result.split(', ')
                    result_address = result[0]
                    result_string = result[-1]
                    result2 = str(input('Desired Token Address: '))
                    if ',' not in result2:
                        print(colored('Syntax Error', 'red'))
                    else:
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
                if ',' not in result:
                    print(colored('Syntax Error', 'red'))
                else:
                    result = result.split(', ')
                    result_address = result[0]
                    result_string = result[-1]
                    result2 = str(input('Desired Token Address: '))
                    if ',' not in result2:
                        print(colored("Syntax Error", 'red'))
                    else:
                        result2 = result2.split(', ')
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
                            price_output = self.uniswap.get_price_output(result_address, result2_address, user_amount * 10**18)
                            print('{root} {root_val} = {des} {des_val}'.format(root=result_string, root_val=1, des=result2_string, des_val=price_output))

            elif user_prompt == '/sell' and self.veresion == 3:
                transaction_done = False
                try:
                    sell_hash = str(input('Hash of Token wanted to Convert: ')) #Address, [coin_name]
                    sell_hash = sell_hash.strip(' ')
                    sell_hash_lst = sell_hash.split(', ')
                    desired_hash = str(input('Desired Token Hash: '))
                    desired_hash = desired_hash.strip(' ')
                    desired_hash_lst = desired_hash.split(', ')

                    sell_hash_address = sell_hash_lst[0]
                    sell_hash_name = sell_hash_lst[-1]
                    desired_hash_address = desired_hash_lst[0]
                    desired_hash_name = desired_hash_lst[-1]

                    user_quantity = str(input("Amount: "))
                    if len(user_quantity) > 1:
                        user_quantity = float(user_quantity)
                    else:
                        user_quantity = int(user_quantity)

                    while True:
                        user_send_prompt = str(input('Would you like to send resulting conversion to an address? type (y/n): '))
                        user_send_prompt = user_send_prompt.strip(' ')
                        if user_send_prompt == 'y':
                            user_address = str(input('Desired User Hash: '))
                            user_address = user_address.strip(' ')
                            fee_prompt = str(input('Would you like to add a fee pool? type(y/n)? '))
                            if fee_prompt == 'y':
                                fee = 500
                                transaction = self.uniswap.make_trade(sell_hash_address, desired_hash_address, user_quantity * 10 ** 18, user_address, fee=fee)
                            else:
                                transaction = self.uniswap.make_trade(sell_hash_address, desired_hash_address, user_quantity * 10 ** 18, user_address)
                            print(colored('{amount} of {root} was sold for {desired} and sent to {address}'.format(amount=user_quantity, root=sell_hash_name, desired=desired_hash_name, address=user_address), 'green'))
                            transaction_done = True
                            break 
                        elif user_send_prompt == 'n':
                            break 
                        else:
                            continue 
                    
                    if transaction_done == True:
                        pass 
                    else:
                        fee_prompt = str(input('Would you like to add a fee pool? type(y/n)? '))
                        if fee_prompt == 'y':
                            fee = 500
                            transaction = self.uniswap.make_trade(sell_hash_address, desired_hash_address, user_quantity * 10 ** 18, fee=fee)

                        else:
                            transaction = self.uniswap.make_trade(sell_hash_address, desired_hash_address, user_quantity * 10 ** 18)
                        print(colored('{amount} of {root} was sold for {desired}'.format(amount=user_quantity, root=sell_hash_name, desired=desired_hash_name), 'green'))

                except:
                    print(colored('Something Went Wrong', 'red'))
            
            elif user_prompt == '/sell' and self.version != 3:
                transaction_done = False
                try:
                    sell_hash = str(input('Hash of Token wanted to Convert: ')) #Address, [coin_name]
                    sell_hash = sell_hash.strip(' ')
                    sell_hash_lst = sell_hash.split(', ')
                    desired_hash = str(input('Desired Token Hash: '))
                    desired_hash = desired_hash.strip(' ')
                    desired_hash_lst = desired_hash.split(', ')

                    sell_hash_address = sell_hash_lst[0]
                    sell_hash_name = sell_hash_lst[-1]
                    desired_hash_address = desired_hash_lst[0]
                    desired_hash_name = desired_hash_lst[-1]

                    user_quantity = str(input("Amount: "))
                    if len(user_quantity) > 1:
                        user_quantity = float(user_quantity)
                    else:
                        user_quantity = int(user_quantity)

                    while True:
                        user_send_prompt = str(input('Would you like to send resulting conversion to an address? type (y/n): '))
                        user_send_prompt = user_send_prompt.strip(' ')
                        if user_send_prompt == 'y':
                            user_address = str(input('Desired User Hash: '))
                            user_address = user_address.strip(' ')
                            transaction = self.uniswap.make_trade(sell_hash_address, desired_hash_address, user_quantity * 10 ** 18, user_address)
                            print(colored('{amount} of {root} was sold for {desired} and sent to {address}'.format(amount=user_quantity, root=sell_hash_name, desired=desired_hash_name, address=user_address), 'green'))
                            transaction_done = True
                            break 
                        elif user_send_prompt == 'n':
                            break 
                        else:
                            continue 
                    
                    
                    if transaction_done == True:
                        pass 
                    else:
                        transaction = self.uniswap.make_trade(sell_hash_address, desired_hash_address, user_quantity * 10 ** 18)
                        print(colored('{amount} of {root} was sold for {desired}'.format(amount=user_quantity, root=sell_hash_name, desired=desired_hash_name), 'green'))


                except:
                    print(colored('Something Went Wrong', 'red'))
                    
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
                                                
            
            elif user_prompt == '/buy' and self.version != 3:
                transaction_done = False
                try:
                    desired_hash = str(input('Desired Token Hash: '))   # Addres, [coin_name]
                    desired_hash.strip(' ')
                    desired_hash_lst = desired_hash.split(', ')
                    current_hash = str(input('Hash of Token that will be Used to Buy: '))
                    current_hash = current_hash.strip(' ')
                    current_hash_lst = current_hash.split(', ')


                    desired_hash_address = desired_hash_lst[0]
                    desired_hash_name = desired_hash_lst[-1]
                    current_hash_address = current_hash_lst[0]
                    current_hash_name = current_hash_lst[-1]

                    user_quantity = str(input('Amount: '))
                    if len(user_quantity) > 1:
                        user_quantity = float(user_quantity)
                    else:
                        user_quantity = int(user_quantity)
                    
                    while True:
                        user_send_prompt = str(input('Would you like to send the bought token to a user? type (y/n): '))
                        if user_send_prompt == 'y':
                            user_address = str(input('Desired User Hash: '))
                            user_address = user_address.strip(' ')
                            transaction = self.uniswap.make_trade_output(desired_hash_address, current_hash_address, user_quantity*10**18, user_address)
                            print('{amount} of {desired} was bought with {current} and sent to {address}'.format(amount=user_quantity, desired=desired_hash_name, current=current_hash_name, address=user_address))
                            transaction_done = True 
                            break 
                        elif user_send_prompt == 'n':
                            break 
                        else:
                            continue 
                    if transaction_done == True:
                        pass 
                    else:
                        transaction = self.uniswap.make_trade_output(desired_hash_address, current_hash_address, user_quantity*10**18)
                        print('{amount} of {desired} was bought with {current}'.format(amount=user_quantity, desired=desired_hash_name, current=current_hash_name))
                except:
                    print(colored('Something Went Wrong', 'red'))

            elif user_prompt == '/cv_uni':
                desired_uni_version = str(input('Please insert the desired version (1 - 3): '))
                try:
                    version = int(desired_uni_version)
                    self.version = version
                    self.uniswap = Uniswap(address=self.address, private_key=self.private_key, version=self.version, provider=self.provider)
                    print(colored('Version has been successfully changed to: {}'.format(self.version), 'green'))
            
                except:
                    print(colored('Incorrect Command', 'red'))
            elif user_prompt == '/buy' and self.version == 3:
                transaction_done = False
                try:
                    desired_hash = str(input('Desired Token Hash: '))   # Addres, [coin_name]
                    desired_hash.strip(' ')
                    desired_hash_lst = desired_hash.split(', ')
                    current_hash = str(input('Hash of Token that will be Used to Buy: '))
                    current_hash = current_hash.strip(' ')
                    current_hash_lst = current_hash.split(', ')


                    desired_hash_address = desired_hash_lst[0]
                    desired_hash_name = desired_hash_lst[-1]
                    current_hash_address = current_hash_lst[0]
                    current_hash_name = current_hash_lst[-1]

                    user_quantity = str(input('Amount: '))
                    if len(user_quantity) > 1:
                        user_quantity = float(user_quantity)
                    else:
                        user_quantity = int(user_quantity)
                    
                    while True:
                        user_send_prompt = str(input('Would you like to send the bought token to a user? type (y/n): '))
                        if user_send_prompt == 'y':
                            user_address = str(input('Desired User Hash: '))
                            user_address = user_address.strip(' ')
                            fee_prompt = str(input('Would you like to add a fee pool? type(y/n)? '))
                            if fee_prompt == 'y':
                                fee = 500
                                transaction = self.uniswap.make_trade_output(desired_hash_address, current_hash_address, user_quantity*10**18, user_address, fee=fee)
                            else:
                                transaction = self.uniswap.make_trade_output(desired_hash_address, current_hash_address, user_quantity*10**18, user_address, fee=fee)
                            print('{amount} of {desired} was bought with {current} and sent to {address}'.format(amount=user_quantity, desired=desired_hash_name, current=current_hash_name, address=user_address))
                            transaction_done = True 
                            break 
                        elif user_send_prompt == 'n':
                            break 
                        else:
                            continue 
                    if transaction_done == True:
                        pass 
                    else:
                        fee_prompt = str(input('Would you like to add a fee pool? type(y/n)? '))
                        if fee_prompt == 'y':
                            fee = 500
                            transaction = self.uniswap.make_trade_output(desired_hash_address, current_hash_address, user_quantity*10**18, fee=fee)
                        else:
                            transaction = self.uniswap.make_trade_output(desired_hash_address, current_hash_address, user_quantity*10**18)
                        print('{amount} of {desired} was bought with {current}'.format(amount=user_quantity, desired=desired_hash_name, current=current_hash_name))
                except:
                    print(colored('Something Went Wrong', 'red'))

            elif user_prompt == '/eth_balcon' and self.version == 1:      # Fetches balance of Eth in an Exchange Contral
                desired_user_contract = str(input('Desired User Contract: '))  # Address, [coin_name]
                desired_user_contract.strip(' ')
                desired_user_contract = desired_user_contract.split(', ')
                desired_user_address = desired_user_contract[0]
                desired_user_name = desired_user_contract[-1]
    
                result = self.uniswap.get_ex_eth_balance(desired_user_address)
                print('{desired} = {bal} ETH'.format(desired=desired_user_name, bal=result))
            
            elif user_prompt == '/bal_contract' and self.version == 1:  # Fetches Balance of a Token in an Exchange Contract
                desired_user_contract = str(input('Desired User Contract: '))     # Address, [coin_name] 
                desired_user_contract.strip(' ')
                desired_user_contract = desired_user_contract.split(', ')
                desired_user_address = desired_user_contract[0]
                desired_user_name = desired_user_contract[-1]
                result = self.uniswap.get_exchange_rate(desired_user_address)
                result = self.uniswap.get_ex_token_balance(desired_user_address)
                print('{desired} = {result}'.format(desired=desired_user_name, result=result))

            elif user_prompt == '/ex_eth' and self.version == 1:                            # Address, [coin_name]
                desired_user_contract = str(input('Desired User Contract: '))          # Exchange rate for Eth
                desired_user_contract.strip(' ')
                desired_user_contract = desired_user_contract.split(', ')
                desired_user_address = desired_user_contract[0]
                desired_user_name = desired_user_contract[-1]
                result = self.uniswap.get_exchange_rate(desired_user_address)
                print('{bal}/ETH = {result}'.format(bal=desired_user_name, result=result))
            
            elif user_prompt == '/add_li' and self.version == 1:
                desired_user_contract = str(input('Desired User Contract Hash: '))     #Address, [coin_name]
                desired_user_contract = desired_user_contract.split(', ')
                desired_user_address = desired_user_contract[0]
                desired_user_name = desired_user_contract[-1]
                try:
                    self.uniswap.add_liquidity(desired_user_address, 1*10**18)
                    print(colored('Liquidity Added to {} successfully!'.format(desired_user_name)))
                except:
                    print(colored('Liquidity Unsuccessful', 'red'))
            
            elif user_prompt == '/remove_li' and self.version == 1:
                desired_user_contract = str(input('Desired User Contract Hash: '))     #Address, [coin_name]
                desired_user_contract = desired_user_contract.split(', ')
                desired_user_address = desired_user_contract[0]
                desired_user_name = desired_user_contract[-1]
                try:
                    self.uniswap.remove_liquidity(desired_user_address, 1*10**18)
                    print(colored('Liquidity Removed from {} successfully!'.format(desired_user_name)))
                except:
                    print(colored('Liquidity Unsuccessful', 'red'))
            
            elif user_prompt == '/quit':
                break

            else:
                print(colored('Invalid Command', 'red'))

                                


                        
                

                    
                    

                    


test = Script()
print(test)
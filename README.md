# UniPython 

A Program to interact with UniSwap protocols locally. 

Commands include viewing conversion/rates, selling, buying, adding/removing liqudity and adding pool rates.

# First Steps

The program will prompt the user to manually type in their account address and private key of their Ethereum Wallet. This can be either on MetaMask or some other platform, but it is necessary to type it in correctly as the terminal will not be able to call the MetaMask client. 

Users can choose versions ranging from `1 - 3`. UniSwap versions 1 and 3 have different selling and buying methods, where pool fees are taken into consideration, liquidity, and pooling methods are present. It should be noted that the base version that the program runs on by default is `2` for stability, but the user can choose another version if needed.

Moreover, it is necessary that the user has a Web3 Provider (such as Infura) on the *mainnet*. They must type their HTTP Mainnet Server when prompted.

## Errors

Possible errors include typing either crediential wrong, or having typed the wrong the version greater than 3. If this happens, the user should make sure that their credientails (account, and private key) and the version is typed correctly in reference to what the program takes in.


# Conversions/Rates

Users can look at a rate of a token relative to another token of desire.

Syntax: `/conversion`
Syntax Command When Prompted: `TokenHash, [coin_name]`

The program will output the conversion between the desired and root token specified. After the program runs, the typed token hashes will be added to an underlying array, which computes sample rates based on prices for a given desired token inputted during the runtime for reference. View (Sbv) for more information.

## Errors

Errors include if either the token hash cannot be found or the command is typed incorrectly. It is recommended that token hashes are obtained either on Uniswap platform or on EtherScan.


# Selling 

Users can sell a desired token and convert it into another contract token. 

Syntax: `/sell`
Syntax When Prompted: `TokenHash, [coin_name]`

The user can specify a certain amount that they want to trade.

If the user is running on UniSwap v3, the user has the option to add a 0.05% pool fee to their transaction. This is optional.

## Errors

There are multiple ways where a user may face an issue. The most common ones include where the user types the command wrong or the hash of a token is not found. This can be fixed by double checking  the command and copying the token hash on the UniSwap platform. Another problem that the user may face is if they have insufficient amounts of funds for a certain token. If this happens, the transaction will be interrupted, and thus, the user should make note of how many tokens they have before selling.

If the user wants to send the sold token to another user, they can input the user's token hash, but can prompt an error as well if typed incorrectly.


# Buying

Similar to selling, users can also buy a desired token using one of the tokens they already have.

Syntax: `/buy`
Syntax When Prompted: `TokenHash, [coin_name]`

The user can specify the amount of tokens they want to buy

Once again, similar to selling, if the user is running on UniSwap v3, the user has the option to add a 0.5% pool fee to their transaction, which is optional.

The user may also the have the option to gift the transaction to another user, which is compatiable with *all* versions.

## Errors

There are multiple ways where a user may face an issue. The most common ones include where the user types the command wrong or the hash of a token is not found. This can be fixed by double checking  the command and copying the token hash on the UniSwap platform. Another problem that the user may face is if they have insufficient amounts of funds for a certain token they will use to buy. If this happens, the transaction will be interrupted, and thus, the user should make note of how many tokens they have before buying.

If the user wants to send the sold token to another user, they can input the user's token hash, but can prompt an error as well if typed incorrectly.

# Search By Value (SBV)

Users can create and view a sorted table of multiple rates of different tokens of one desired token.

Syntax: `/buy`
Syntax When Prompted: `TokenHash, [coin_name]`

The user may be prompted the number of tokens they want to compare, and with the use of quicksort, the program fetches exchange rates for reference.

A similar algorithm runs in the background on every type the user types `/conversion.` The program does runs a similar algorithm and fetches a table of sorted conversion rates based on a random sample of desired tokens specified when the user had initially inputted in `/conversion`. 

The user can fetch the History SBV by typing the command `/hsbv`. It should be mentioned that the command returns nothing if the command `/conversion` was not used at all.

## Errors

One of the most common errors that may arise when executing this function is typing the token hashes incorrectly. It is recommended that the user copies the tokne hashes from the UniSwap protocol.

# Pooling 

There are three methods that allow the user to pool with Eth. However, before running the command, the user must be on version `1` of the UniSwap Protocol.

Syntax: `/eth_balcon`: Fetches the balance of Eth in an Exchange Contract
Syntax: `bal_contract`: Fetches the balance of a token in an Exchange Contract
Syntax: `/ex_eth`: Exchange Rate for Eth
Syntax When Prompted: `Address, [coin_name]`

*Note*: These commands are ran separately. 


## Errors

The only possible error that my arise is that if the user types the TokenHash incorrectly or a syntax error of the command. It is recommended that the user uses UniSwap to fetch the correct TokenHash.


# Liquidity 

Users can add and remove liquidity to their exchange contract. The user must be on UniSwap Version 1.

Syntax to add liquidity: `/add_li`
Syntax to remove liquidity: `/remove_li`
Syntax When Prompted: `Address, [coin_name]`


## Errors

The only possible error that my arise is that if the user types the TokenHash incorrectly or a syntax error of the command. It is recommended that the user uses UniSwap to fetch the correct TokenHash.


# More Information

If users wish to change their UniSwap version, they can do so with `/cv_uni`, which allows the program to switch versions.

The `/rate` command allows for users to find the rate between their root and desired root token quickly. The syntax of `Address, [coin_name]` remains the same.

The phrase `Syntax When Prompted` represents the syntax when the program prompts a message like `Root Token: ` or `Desired Token Address: `, or anything related to fetching a token.

If there are any questions or concerns, feel free to reach out (website: www.jaivalpatel.com). 

Made by Jaival Patel 🦖